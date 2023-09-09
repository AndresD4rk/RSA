# Define tu propio vocabulario de sustitución (personalízalo como desees)
substitution_dict = {
    'A': '1',
    'B': '2',
    'C': '3',
    'D': '4',
    'E': '5',
    # Continúa con las demás letras y sus asignaciones
}

# Función para cifrar un mensaje
def encrypt(message, substitution_dict):
    encrypted_message = ""
    for char in message:
        if char in substitution_dict:
            encrypted_message += substitution_dict[char]
        else:
            encrypted_message += char
    return encrypted_message

# Función para descifrar un mensaje cifrado
def decrypt(ciphertext, substitution_dict):
    reverse_dict = {v: k for k, v in substitution_dict.items()}  # Crear un diccionario inverso para descifrar
    decrypted_message = ""
    i = 0
    while i < len(ciphertext):
        char = ciphertext[i]
        if char in reverse_dict:
            decrypted_message += reverse_dict[char]
            i += 1
        else:
            decrypted_message += char
        i += 1
    return decrypted_message

# Mensaje original
message = "ABCDE"

# Cifrar el mensaje
ciphertext = encrypt(message, substitution_dict)
print("Mensaje cifrado:", ciphertext)

# Descifrar el mensaje
decrypted_message = decrypt(ciphertext, substitution_dict)
print("Mensaje descifrado:", decrypted_message)
