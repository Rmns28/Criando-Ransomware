import os
import pyaes

## abrir arquivo criptografado
file_name = "exemplo.txt.arquivocriptografado"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"responsabilidade"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover arquivo criptografado
os.remove(file_name)

## criar arquivo descriptografado
new_file = "exemplo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
