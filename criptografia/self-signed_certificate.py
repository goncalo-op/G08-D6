import datetime
import os
from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

def generate_self_signed_cert():
    try:
        # Use environment variables or defaults
        country_name = os.getenv("COUNTRY_NAME", "PT")
        state_name = os.getenv("STATE_NAME", "Lisboa")
        locality_name = os.getenv("LOCALITY_NAME", "Lisboa")
        org_name = os.getenv("ORG_NAME", "Iscte-Sintra")
        common_name = os.getenv("COMMON_NAME", "example.local")

        # Generate private key
        print("Generating private key...")
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096
        )

        # Save private key (no encryption for Kubernetes automation)
        with open("./example.local.key", "wb") as f:
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        # Create subject and issuer
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country_name),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state_name),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, org_name),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name)
        ])

        # Generate certificate
        print("Generating self-signed certificate...")
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
            datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365)
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName("example.local")]),
            critical=False
        ).add_extension(
            x509.ExtendedKeyUsage([x509.oid.ExtendedKeyUsageOID.SERVER_AUTH]),
            critical=False
        ).sign(key, hashes.SHA256())

        # Save certificate
        with open("./example.local.crt", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))

        print("Self-signed certificate and key generated successfully!")
        return True
    except Exception as e:
        print(f"Error generating self-signed certificate: {e}")
        return False

if __name__ == "__main__":
    if generate_self_signed_cert():
        print("Output files: example.local.crt, example.local.key")
    else:
        print("Failed to generate certificate and key")