from Crypto.Cipher import AES

secret_key = 'this is secret:)'
message = 'Awesome python!!'

crypto = AES.new(secret_key)

cipher_data = crypto.encrypt(message)
print(cipher_data)
original_message = crypto.decrypt(cipher_data)
print(original_message)
