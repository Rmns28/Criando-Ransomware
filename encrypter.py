import os
import pyaes

## abrir o arquivo criptografado
file_name = "exemplo.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover arquivo
os.remove(file_name)

## chave de criptografia
key = b"responsabilidade"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar arquivo
crypto_data = aes.encrypt(file_data)

## salvar arquivo criptografado
new_file = file_name + ".arquivocriptografado"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
