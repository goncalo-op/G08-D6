import datetime
import os
import sqlite3
from sqlite3 import Error
from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID, ExtensionOID, ExtendedKeyUsageOID
import prettytable

def print_main_menu():
    print("-------------------------------")
    print("[1] Certificate Signing Requests (CSR)")
    print("[2] Certificate Revocation (CRL)")
    print("[3] List Issued Certificates")
    print("[0] Exit")
    print("-------------------------------")

def is_ca_already_setup():
    try:
        ca_exists = os.path.isfile("./ca.crt")
        if ca_exists:
            return True
        else:
            os.makedirs("./requests", exist_ok=True)
            os.makedirs("./certs", exist_ok=True)
            return False
    except Exception as e:
        print(f"Error checking CA setup: {e}")
        return False

def setup_new_ca():
    try:
        # Use environment variables or defaults
        country_name = os.getenv("COUNTRY_NAME", "PT")
        state_name = os.getenv("STATE_NAME", "Lisboa")
        locality_name = os.getenv("LOCALITY_NAME", "Lisboa")
        org_name = os.getenv("ORG_NAME", "Iscte-Sintra")
        common_name = os.getenv("COMMON_NAME", "MyCA")

        # Generate CA key
        print("Creating CA keypair...")
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096
        )

        with open("./ca.key", "wb") as f:
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        # Create CA certificate
        print("Creating CA certificate...")
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country_name),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state_name),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, org_name),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name)
        ])

        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.datetime.now(datetime.timezone.utc)
        ).not_valid_after(
            datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=5*365)
        ).add_extension(
            x509.BasicConstraints(ca=True, path_length=None),
            critical=True
        ).add_extension(
            x509.KeyUsage(
                key_cert_sign=True,
                content_commitment=False,
                key_agreement=False,
                key_encipherment=False,
                crl_sign=True,
                data_encipherment=False,
                decipher_only=False,
                digital_signature=True,
                encipher_only=False
            ),
            critical=True
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName("example.local")]),
            critical=False
        ).sign(key, hashes.SHA256())

        with open("./ca.crt", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))

        print("CA setup completed successfully!")
        return key, cert
    except Exception as e:
        print(f"Error setting up CA: {e}")
        return None, None

def read_ca_key():
    try:
        print("Reading CA key...")
        with open("./ca.key", "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None
            )
        return private_key
    except FileNotFoundError:
        print("Error: CA key file not found")
        return None
    except Exception as e:
        print(f"Error reading CA key: {e}")
        return None

def read_ca_cert():
    try:
        print("Reading CA certificate...")
        with open("./ca.crt", "rb") as f:
            certificate = x509.load_pem_x509_certificate(f.read())
        return certificate
    except FileNotFoundError:
        print("Error: CA certificate file not found")
        return None
    except Exception as e:
        print(f"Error reading CA certificate: {e}")
        return None

def create_connection():
    try:
        conn = sqlite3.connect('certs.db')
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    try:
        sql_create_certs_table = """CREATE TABLE IF NOT EXISTS certs (
                                        serial INTEGER PRIMARY KEY,
                                        dns TEXT NOT NULL,
                                        status_date TEXT NOT NULL,
                                        status TEXT NOT NULL,
                                        cert TEXT NOT NULL
                                    );"""
        c = conn.cursor()
        c.execute(sql_create_certs_table)
        conn.commit()
    except Error as e:
        print(f"Error creating table: {e}")

def certificate_issuance(c, ca_key, ca_issuer):
    try:
        while True:
            list_of_csr = list_requests()
            print("[1] Issue certificate")
            print("[0] Exit")
            choice = input("--> ")
            if choice == "0":
                return True
            elif choice == "1":
                cert_csr_option = input("Enter the CSR number [0 - to cancel]: ")
                if cert_csr_option == "0":
                    continue
                if cert_csr_option not in list_of_csr:
                    print("Invalid CSR number")
                    continue
                csr = list_of_csr[cert_csr_option]
                if csr.is_signature_valid:
                    print("CSR signature is valid!")
                    print(f"Subject -> {csr.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}")
                    common_name = str(csr.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value)
                    new_cert_dn = str(csr.subject)
                    issue_choice = input("Issue the Certificate [Y][N] --> ")
                    if issue_choice.lower() == "y":
                        sn = get_last_serial_number(c)
                        cert = issue_certificate(sn, csr, ca_key, ca_issuer)
                        if cert:
                            save_certificate_db(c, sn, new_cert_dn, cert)
                            delete_csr_file(common_name)
                    else:
                        continue
                else:
                    print("CSR signature is invalid!")
            else:
                continue
    except Exception as e:
        print(f"Error during certificate issuance: {e}")
        return False
    return True

def save_certificate_db(c, sn, new_cert_dn, cert):
    try:
        sql = '''INSERT INTO certs(serial, dns, status_date, status, cert) VALUES(?,?,?,?,?)'''
        cur = c.cursor()
        date_issued = str(datetime.datetime.now(datetime.timezone.utc))
        status = "ISSUED"
        certificate = (sn, new_cert_dn, date_issued, status, cert.public_bytes(serialization.Encoding.PEM).decode())
        cur.execute(sql, certificate)
        c.commit()
        return True
    except Error as e:
        print(f"Error saving certificate to database: {e}")
        return False

def list_requests():
    try:
        table = prettytable.PrettyTable(["Number", "CSR", "Subject"])
        number = 1
        table.align = "l"
        list_of_csr = {}
        for csr_file in os.listdir("./requests"):
            if csr_file.endswith(".csr"):
                with open(f"./requests/{csr_file}", "rb") as f:
                    csr = x509.load_pem_x509_csr(f.read())
                table.add_row([number, csr_file, csr.subject])
                list_of_csr[str(number)] = csr
                number += 1
        print(table)
        return list_of_csr
    except Exception as e:
        print(f"Error listing CSRs: {e}")
        return {}

def issue_certificate(sn, csr, key, ca_issuer):
    try:
        cert = x509.CertificateBuilder().subject_name(
            csr.subject
        ).issuer_name(
            ca_issuer
        ).public_key(
            csr.public_key()
        ).serial_number(
            sn
        ).not_valid_before(
            datetime.datetime.now(datetime.timezone.utc)
        ).not_valid_after(
            datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365)
        ).add_extension(
            x509.KeyUsage(
                key_cert_sign=False,
                content_commitment=False,
                key_agreement=False,
                key_encipherment=True,
                crl_sign=False,
                data_encipherment=True,
                decipher_only=False,
                digital_signature=True,
                encipher_only=False
            ),
            critical=True
        ).add_extension(
            x509.ExtendedKeyUsage([ExtendedKeyUsageOID.CLIENT_AUTH, ExtendedKeyUsageOID.SERVER_AUTH]),
            critical=False
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName(csr.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value)]),
            critical=False
        ).sign(key, hashes.SHA256())

        print(f"Writing certificate for {csr.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}...")
        with open(f"./certs/{csr.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}.crt", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        return cert
    except Exception as e:
        print(f"Error issuing certificate: {e}")
        return None

def certificate_revocation(c, ca_key, ca_cert):
    try:
        while True:
            list_certificates_db(c)
            option = input("Certificate to revoke [0 - Back]: ")
            if option == "0":
                break
            if revoke_on_db(c, option):
                create_or_update_crl(c, ca_key, ca_cert, option)
                continue
            else:
                continue
    except Exception as e:
        print(f"Error during certificate revocation: {e}")
        return False
    return True

def revoke_on_db(c, cert_number):
    try:
        option = input(f"Do you really want to revoke certificate {cert_number}? [Y/N]")
        if option.lower() == "y":
            cur = c.cursor()
            cur.execute('UPDATE certs SET status = "REVOKED", status_date=? WHERE serial=?',
                        (str(datetime.datetime.now(datetime.timezone.utc)), cert_number))
            c.commit()
            return True
        return False
    except Error as e:
        print(f"Error revoking certificate: {e}")
        return False

def create_or_update_crl(c, ca_key, ca_cert):
    try:
        builder = x509.CertificateRevocationListBuilder()
        builder = builder.issuer_name(ca_cert.subject)
        builder = builder.last_update(datetime.datetime.now(datetime.timezone.utc))
        builder = builder.next_update(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7))

        if os.path.isfile("./certs.crl"):
            with open("./certs.crl", "rb") as f:
                crl = x509.load_pem_x509_crl(f.read())
            for i in range(len(crl)):
                builder = builder.add_revoked_certificate(crl[i])

        revoked_cert = x509.RevokedCertificateBuilder().serial_number(
            int(cert_serial_number)
        ).revocation_date(
            datetime.datetime.now(datetime.timezone.utc)
        ).build()
        builder = builder.add_revoked_certificate(revoked_cert)

        crl = builder.sign(private_key=ca_key, algorithm=hashes.SHA256())
        with open("./certs.crl", "wb") as f:
            f.write(crl.public_bytes(serialization.Encoding.PEM))
        return True
    except Exception as e:
        print(f"Error creating/updating CRL: {e}")
        return False

def get_last_serial_number(c):
    try:
        cur = c.cursor()
        cur.execute('SELECT max(serial) as ns FROM certs')
        row = cur.fetchone()
        return 1 if row[0] is None else row[0] + 1
    except Error as e:
        print(f"Error getting last serial number: {e}")
        return 1

def list_certificates_db(c):
    try:
        table = prettytable.PrettyTable(["SN", "DN", "Data", "Status"])
        table.align = "l"
        cur = c.cursor()
        cur.execute('SELECT * FROM certs')
        rows = cur.fetchall()
        for row in rows:
            table.add_row([row[0], row[1], row[2], row[3]])
        print(table)
    except Error as e:
        print(f"Error listing certificates: {e}")

def delete_csr_file(filename):
    try:
        csr_path = f"./requests/{filename}.csr"
        if os.path.exists(csr_path):
            os.remove(csr_path)
            return True
        return False
    except Exception as e:
        print(f"Error deleting CSR file: {e}")
        return False

if __name__ == '__main__':
    try:
        if not is_ca_already_setup():
            ca_key, ca_cert = setup_new_ca()
            if not ca_key or not ca_cert:
                print("Failed to setup CA")
                exit(1)
            c = create_connection()
            if c:
                create_table(c)
            else:
                print("Failed to connect to database")
                exit(1)
        else:
            ca_key = read_ca_key()
            ca_cert = read_ca_cert()
            if not ca_key or not ca_cert:
                print("Failed to load CA key or certificate")
                exit(1)
            c = create_connection()
            if not c:
                print("Failed to connect to database")
                exit(1)

        while True:
            print_main_menu()
            choice = input("--> ")
            if choice == "0":
                c.close()
                break
            elif choice == "1":
                certificate_issuance(c, ca_key, ca_cert.subject)
            elif choice == "2":
                certificate_revocation(c, ca_key, ca_cert)
            elif choice == "3":
                list_certificates_db(c)
            else:
                print("Invalid choice")
    except Exception as e:
        print(f"Error in main loop: {e}")
        if 'c' in locals():
            c.close()