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
    ciphertext_text = ciphertext_data.cget("text")
    if ciphertext_text and ciphertext_text!="[]":
        elementos = ciphertext_data.cget("text").strip("[]").split(", ")
        numeros= [int(elemento)for elemento in elementos]
        # message = int(ciphertext_data.cget("text"))  # Obtiene el mensaje ingresado por el usuario    
        decrypted_message = decrypt(numeros, private_key)
        decrypted_label.config(text="Mensaje descifrado: " + decrypted_message)
    else:
        decrypted_label.config(text="No hay mensaje cifrado. ")

# Crear la ventana principal
root = tk.Tk()
root.title("Cifrado y Descifrado RSA")

# Configuración del estilo
root.geometry("800x600")  # Tamaño de la ventana
root.configure(bg="#8b00c5")  # Color de fondo

# Título
title_label = tk.Label(root, text="Cifrado y Descifrado RSA", font=("Arial", 24), bg="#8b00c5", fg="white")
title_label.pack(pady=30)

# Etiqueta y campo de entrada para el mensaje
message_label = tk.Label(root, text="Mensaje a cifrar:", font=("Arial", 18), bg="#8b00c5", fg="white")
message_label.pack()
entry = tk.Entry(root, font=("Arial", 18), width=45)
entry.pack(pady=10)

# Botón para encriptar el mensaje
encrypt_button = tk.Button(root, text="Encriptar", font=("Arial", 18), bg="#8b00c5", fg="white", command=encrypt_message)
encrypt_button.pack(pady=10)

# Etiqueta para mostrar el mensaje cifrado
ciphertext_label = tk.Label(root, text="Mensaje cifrado:", font=("Arial", 18), bg="#8b00c5", fg="white")
ciphertext_label.pack(pady=10)
ciphertext_data = tk.Label(root, text="", font=("Arial", 18), bg="#8b00c5", fg="white")
ciphertext_data.pack(pady=10)

# Botón para desencriptar el mensaje
decrypt_button = tk.Button(root, text="Desencriptar", font=("Arial", 18), bg="#8b00c5", fg="white", command=decrypt_message)
decrypt_button.pack(pady=10)

# Etiqueta para mostrar el mensaje descifrado
decrypted_label = tk.Label(root, text="Mensaje descifrado:", font=("Arial", 18), bg="#8b00c5", fg="white")
decrypted_label.pack(pady=10)
decrypted_data = tk.Label(root, text="", font=("Arial", 18), bg="#8b00c5", fg="white")
decrypted_data.pack(pady=10)

# Generar claves RSA
public_key, private_key = generate_rsa_keys()

# Ejecutar la aplicación
root.mainloop()