from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt

eth_k = generate_eth_key()
sk_hex = eth_k.to_hex()  # hex string
pk_hex = eth_k.public_key.to_hex()  # hex string
data = b'this is a test'
encrypt_str = encrypt(pk_hex, data)
print(encrypt_str)

decrypt_str = decrypt(sk_hex, encrypt_str)

print(decrypt_str)

secp_k = generate_key()
sk_bytes = secp_k.secret  # bytes
pk_bytes = secp_k.public_key.format(True)  # bytes
encrypt_str = encrypt(pk_bytes, data)
print(encrypt_str)

decrypt_str = decrypt(sk_bytes, encrypt_str)

print(decrypt_str)

