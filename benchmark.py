import time

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# So lan lap de do toc do
LOOPS = 1000

# Du lieu mau
data = b"Hello - Bai tap benchmark AES va RSA"


# =========================
# AES
# =========================

aes_key = get_random_bytes(32)

start = time.perf_counter()

for _ in range(LOOPS):
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)

    ciphertext_aes = cipher_aes.encrypt(
        pad(data, AES.block_size)
    )

    decipher_aes = AES.new(
        aes_key,
        AES.MODE_CBC,
        iv=cipher_aes.iv
    )

    plaintext_aes = unpad(
        decipher_aes.decrypt(ciphertext_aes),
        AES.block_size
    )

aes_time = time.perf_counter() - start


# =========================
# RSA
# =========================

rsa_key = RSA.generate(2048)

public_key = rsa_key.publickey()
private_key = rsa_key

start = time.perf_counter()

for _ in range(LOOPS):
    cipher_rsa = PKCS1_OAEP.new(public_key)
    ciphertext_rsa = cipher_rsa.encrypt(data)

    decipher_rsa = PKCS1_OAEP.new(private_key)
    plaintext_rsa = decipher_rsa.decrypt(ciphertext_rsa)

rsa_time = time.perf_counter() - start


# =========================
# KET QUA
# =========================

print("=== SO SANH AES VA RSA ===")
print("So lan lap:", LOOPS)

print("\nAES")
print("Tong thoi gian:", aes_time, "giay")
print("Trung binh:", aes_time / LOOPS, "giay / lan")

print("\nRSA")
print("Tong thoi gian:", rsa_time, "giay")
print("Trung binh:", rsa_time / LOOPS, "giay / lan")

print("\nTy le RSA / AES:")
print(rsa_time / aes_time, "lan")