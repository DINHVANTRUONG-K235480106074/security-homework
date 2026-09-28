from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(32)

data = b"Hello AES - Bai tap An toan va bao mat thong tin"

cipher = AES.new(key, AES.MODE_CBC)

ciphertext = cipher.encrypt(
    pad(data, AES.block_size)
)

print("=== MA HOA AES ===")
print("Du lieu goc :", data.decode())
print("Key        :", key.hex())
print("IV         :", cipher.iv.hex())
print("Ciphertext :", ciphertext.hex())

decipher = AES.new(
    key,
    AES.MODE_CBC,
    iv=cipher.iv
)

plaintext = unpad(
    decipher.decrypt(ciphertext),
    AES.block_size
)

print("\n=== GIAI MA AES ===")
print("Du lieu sau giai ma:", plaintext.decode())