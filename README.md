\# BÀI TẬP AN TOÀN VÀ BẢO MẬT THÔNG TIN



\## Người thực hiện

Họ tên: Đinh Văn Trường  

MSSV: K235480106074



\---



\# 1. Thuật toán DES



DES (Data Encryption Standard) là thuật toán mã hóa đối xứng.



Đặc điểm:

\- Sử dụng cùng một khóa để mã hóa và giải mã.

\- Kích thước khối dữ liệu: 64 bit.

\- Khóa hiệu dụng: 56 bit.

\- Thực hiện 16 vòng biến đổi.

\- Hiện nay DES không còn được xem là an toàn do khóa quá ngắn.



Quy trình cơ bản:



Plaintext

→ Initial Permutation

→ 16 vòng Feistel

→ Final Permutation

→ Ciphertext



Giải mã DES thực hiện tương tự nhưng sử dụng các khóa con theo thứ tự ngược lại.



\---



\# 2. Thuật toán AES



AES (Advanced Encryption Standard) là thuật toán mã hóa đối xứng hiện đại.



AES hỗ trợ các độ dài khóa:



\- AES-128

\- AES-192

\- AES-256



AES xử lý dữ liệu theo khối 128 bit.



Các bước chính trong mỗi vòng AES gồm:



1\. SubBytes

2\. ShiftRows

3\. MixColumns

4\. AddRoundKey



Trong bài thực hành này sử dụng AES-256 ở chế độ CBC.



File thực hành:



```text

aes\_demo.py

