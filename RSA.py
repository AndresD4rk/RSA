from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generar un par de claves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Serializar la clave privada en formato PEM (Privacy Enhanced Mail)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Guardar la clave privada en un archivo
with open("private_key.pem", "wb") as key_file:
    key_file.write(private_pem)

# Obtener la clave pública correspondiente
public_key = private_key.public_key()

# Serializar la clave pública en formato PEM
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Guardar la clave pública en un archivo
with open("public_key.pem", "wb") as key_file:
    key_file.write(public_pem)

# Mensaje para cifrar
message = b"HOLA MUNDO O_O"

# Cifrar el mensaje usando la clave pública
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Mostrar el mensaje cifrado
print("Mensaje cifrado:", ciphertext.hex())

# Descifrar el mensaje usando la clave privada
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Mostrar el mensaje descifrado
print("Mensaje descifrado:", plaintext.decode())
