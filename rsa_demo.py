from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Sinh cap khoa RSA 2048-bit
key = RSA.generate(2048)

private_key = key
public_key = key.publickey()

print("=== SINH KHOA RSA ===")
print("Public key:")
print(public_key.export_key().decode())

print("\nPrivate key:")
print(private_key.export_key().decode())

# Du lieu can ma hoa
data = b"Hello RSA - Bai tap An toan va bao mat thong tin"

# Ma hoa bang public key
cipher_rsa = PKCS1_OAEP.new(public_key)
ciphertext = cipher_rsa.encrypt(data)

print("\n=== MA HOA RSA ===")
print("Du lieu goc :", data.decode())
print("Ciphertext :", ciphertext.hex())

# Giai ma bang private key
decipher_rsa = PKCS1_OAEP.new(private_key)
plaintext = decipher_rsa.decrypt(ciphertext)

print("\n=== GIAI MA RSA ===")
print("Du lieu sau giai ma:", plaintext.decode())