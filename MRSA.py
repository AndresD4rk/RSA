# Función para calcular el máximo común divisor (MCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Función para calcular el inverso modular
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Función para generar claves RSA
def generate_rsa_keys():
    # Elegir dos números primos grandes
    p = 11
    q = 23

    # Calcular el módulo N y la función phi(N)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Elegir un exponente de cifrado e que sea coprimo con phi(N)
    e = 3

    # Calcular el exponente de descifrado d
    d = mod_inverse(e, phi_n)

    # Clave pública: (e, n)
    # Clave privada: (d, n)
    return ((e, n), (d, n))

# Función para cifrar un mensaje
def encrypt(message, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

# Función para descifrar un mensaje
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_message

# Generar claves RSA
public_key, private_key = generate_rsa_keys()

# Mensaje para cifrar
message = "SEGURIDAD"

# Cifrar el mensaje
ciphertext = encrypt(message, public_key)
print("Mensaje cifrado:", ciphertext)

# Descifrar el mensaje
decrypted_message = decrypt(ciphertext, private_key)
print("Mensaje descifrado:", decrypted_message)
