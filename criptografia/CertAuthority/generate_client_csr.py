import os
from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID

def generate_client_csr():
    try:
        # Use environment variables or defaults
        country_name = os.getenv("COUNTRY_NAME", "PT")
        state_name = os.getenv("STATE_NAME", "Lisboa")
        locality_name = os.getenv("LOCALITY_NAME", "Lisboa")
        org_name = os.getenv("ORG_NAME", "Iscte-Sintra")
        common_name = os.getenv("COMMON_NAME", "client.example.local")

        # Generate key
        print(f"Creating keypair for {common_name}...")
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096
        )

        # Save key
        with open(f"./{common_name}.key", "wb") as f:
            f.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        # Create CSR
        print(f"Creating CSR for {common_name}...")
        subject = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country_name),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, state_name),
            x509.NameAttribute(NameOID.LOCALITY_NAME, locality_name),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, org_name),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name)
        ])

        csr = x509.CertificateSigningRequestBuilder().subject_name(
            subject
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName(common_name)]),
            critical=False
        ).add_extension(
            x509.ExtendedKeyUsage([ExtendedKeyUsageOID.CLIENT_AUTH]),
            critical=False
        ).sign(key, hashes.SHA256())

        with open(f"./{common_name}.csr", "wb") as f:
            f.write(csr.public_bytes(serialization.Encoding.PEM))

        print("Client CSR and key generated successfully!")
        return True
    except Exception as e:
        print(f"Error generating client CSR: {e}")
        return False

if __name__ == '__main__':
    if generate_client_csr():
        print(f"Output files: {os.getenv('COMMON_NAME', 'client.example.local')}.csr, {os.getenv('COMMON_NAME', 'client.example.local')}.key")
    else:
        print("Failed to generate CSR and key")