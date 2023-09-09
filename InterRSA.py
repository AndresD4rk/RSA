import tkinter as tk

# Funciones de encriptación y descifrado (las mismas que proporcionaste)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Función para generar claves RSA
def generate_rsa_keys():
    # Elegir dos números primos
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
    print (ciphertext)
    return ciphertext

# Función para descifrar un mensaje
def decrypt(ciphertext, private_key):
    d, n = private_key    
    decrypted_message = ''.join([chr(pow(int(char), d, n)) for char in ciphertext])
    print (ciphertext)
    return str(decrypted_message)

# Generar claves RSA
public_key, private_key = generate_rsa_keys()
# Función para manejar el botón de cifrado
def encrypt_message():
    message = entry.get()  # Obtiene el mensaje ingresado por el usuario
    ciphertext = encrypt(message, public_key)
    ciphertext_label.config(text="Mensaje cifrado: ")
    ciphertext_array=ciphertext
    ciphertext_data.config(text=str(ciphertext))

# Función para manejar el botón de descifrado
def decrypt_message():
    elementos = ciphertext_data.cget("text").strip("[]").split(", ")
    numeros= [int(elemento)for elemento in elementos]
    # message = int(ciphertext_data.cget("text"))  # Obtiene el mensaje ingresado por el usuario    
    decrypted_message = decrypt(numeros, private_key)
    decrypted_label.config(text="Mensaje descifrado: " + decrypted_message)

# Crear la ventana principal
root = tk.Tk()
root.title("Cifrado y Descifrado RSA")

# Etiqueta y campo de entrada para el mensaje
message_label = tk.Label(root, text="Mensaje:")
message_label.pack()
entry = tk.Entry(root)
entry.pack()

# Botón para encriptar el mensaje
encrypt_button = tk.Button(root, text="Encriptar", command=encrypt_message)
encrypt_button.pack()

# Etiqueta para mostrar el mensaje cifrado
ciphertext_label = tk.Label(root, text="")
ciphertext_label.pack()
ciphertext_data = tk.Label(root, text="")
ciphertext_data.pack()
# Botón para desencriptar el mensaje
decrypt_button = tk.Button(root, text="Desencriptar", command=decrypt_message)
decrypt_button.pack()

# Etiqueta para mostrar el mensaje descifrado
decrypted_label = tk.Label(root, text="")
decrypted_label.pack()

# Ejecutar la aplicación
root.mainloop()
