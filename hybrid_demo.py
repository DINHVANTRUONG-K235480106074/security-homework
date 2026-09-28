from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# =========================
# 1. Sinh cap khoa RSA
# =========================

rsa_key = RSA.generate(2048)

public_key = rsa_key.publickey()
private_key = rsa_key


# =========================
# 2. Sinh khoa AES
# =========================

aes_key = get_random_bytes(32)


# =========================
# 3. Ma hoa du lieu bang AES
# =========================

data = b"Du lieu bi mat - ket hop AES va RSA"

cipher_aes = AES.new(aes_key, AES.MODE_CBC)

ciphertext = cipher_aes.encrypt(
    pad(data, AES.block_size)
)

iv = cipher_aes.iv


# =========================
# 4. Ma hoa khoa AES bang RSA
# =========================

cipher_rsa = PKCS1_OAEP.new(public_key)

encrypted_aes_key = cipher_rsa.encrypt(aes_key)


print("=== GUI DU LIEU ===")

print("Du lieu goc:")
print(data.decode())

print("\nAES ciphertext:")
print(ciphertext.hex())

print("\nKhoa AES da ma hoa bang RSA:")
print(encrypted_aes_key.hex())


# =========================
# 5. Giai ma khoa AES bang RSA
# =========================

decipher_rsa = PKCS1_OAEP.new(private_key)

decrypted_aes_key = decipher_rsa.decrypt(
    encrypted_aes_key
)


# =========================
# 6. Dung khoa AES vua lay lai
#    de giai ma du lieu
# =========================

decipher_aes = AES.new(
    decrypted_aes_key,
    AES.MODE_CBC,
    iv=iv
)

plaintext = unpad(
    decipher_aes.decrypt(ciphertext),
    AES.block_size
)


print("\n=== NHAN DU LIEU ===")

print("Khoa AES da khoi phuc:")
print(decrypted_aes_key.hex())

print("\nDu lieu sau giai ma:")
print(plaintext.decode())