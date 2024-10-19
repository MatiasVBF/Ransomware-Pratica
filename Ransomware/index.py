import os
import pyaes


## abrir o arquivo criptografado

file-name = 'teste.txt.ransowaretroll'
file = open(file-name,'rb')
file-data = file.read()
file.close()

## chave de descriptografia

key= b'testeransomware'
aes = pyaes.AESmodeOfOperationCTR(key)
decrypt)data = aes.decrypt(file-data)

## remover o arquivo descriptografado

os.remove(file-name)

## criar um novo arquivo descriptografado

new-file = 'teste.txt'
new-file = open(f'{new-file}','wb')
new-file.write(decrypt-data)]new-file.close()