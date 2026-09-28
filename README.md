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

DES (Data Encryption Standard)
Tên gọi: DES - thuật toán mã hoá đối xứng theo khối (block cipher), ra đời 1977, chuẩn của NIST.

Mô tả thuật toán:

Khối dữ liệu: 64 bit. Khoá: 56 bit hiệu dụng (64 bit gồm 8 bit parity).
Cấu trúc Feistel: chia khối 64 bit thành 2 nửa L và R, lặp qua 16 vòng (round).
Mỗi vòng dùng 1 khoá con (subkey) 48 bit sinh ra từ khoá gốc qua thuật toán sinh khoá (key schedule).
Quy trình mã hoá:

Hoán vị khởi tạo (Initial Permutation - IP) trên khối 64 bit.
Qua 16 vòng Feistel: R_i = L_{i-1} XOR F(R_{i-1}, K_i); L_i = R_{i-1}.
Hàm F gồm: mở rộng (Expansion) 32->48 bit, XOR với subkey, thay thế qua 8 hộp S-box 6->4 bit, hoán vị P.
Hoán vị đảo (Final Permutation - IP^-1) cho ra bản mã.
Quy trình giải mã: Giống hệt mã hoá nhưng dùng thứ tự subkey ngược lại (K16 -> K1).

Nhận xét: DES hiện không còn an toàn do khoá 56 bit quá ngắn, dễ bị brute-force với máy tính hiện đại. Ngày nay dùng AES thay thế.

AES (Advanced Encryption Standard)
Tên gọi: AES - chuẩn mã hoá đối xứng hiện đại, NIST công bố 2001, dựa trên thuật toán Rijndael.

Mô tả thuật toán:

Khối dữ liệu cố định: 128 bit (16 byte), tổ chức thành ma trận trạng thái (state) 4x4 byte.
Độ dài khoá: 128 / 192 / 256 bit tương ứng 10 / 12 / 14 vòng lặp (round).
Cấu trúc SPN (Substitution-Permutation Network), không phải Feistel như DES.
Quy trình mã hoá (mỗi round, trừ round cuối bớt MixColumns):

AddRoundKey: XOR state với round key.
SubBytes: thay từng byte qua hộp thế S-box (dựa trên nghịch đảo trong GF(2^8)).
ShiftRows: dịch vòng trái các hàng của ma trận state (hàng i dịch i byte).
MixColumns: trộn dữ liệu theo cột bằng phép nhân ma trận trong GF(2^8).
Lặp lại đủ số round, round cuối cùng bỏ bước MixColumns.
Quy trình giải mã: Làm ngược lại theo thứ tự round key ngược, dùng các phép nghịch đảo: InvShiftRows, InvSubBytes, AddRoundKey, InvMixColumns.

Nhận xét: AES nhanh, an toàn, không có tấn công thực tế nào phá được AES-128 trở lên tính đến nay.

Cài đặt AES bằng C++
Sử dụng thư viện tiny-AES-c, mã hoá/giải mã theo chế độ CBC.

Mã nguồn: aes/cpp

Kết quả chạy demo (./aes_demo):
<img width="965" height="454" alt="image" src="https://github.com/user-attachments/assets/8060d843-948a-422a-861a-9da3888804e4" />
<img width="955" height="419" alt="image" src="https://github.com/user-attachments/assets/4c83f7b7-9ff4-4102-a346-63aa6cbfb207" />
Bài tập 2 — RSA
Nguyên lý RSA (Rivest-Shamir-Adleman)
Tên gọi: RSA - thuật toán mã hoá bất đối xứng (mã hoá công khai), công bố 1977 bởi 3 tác giả Ron Rivest, Adi Shamir, Leonard Adleman. Dựa trên độ khó của bài toán phân tích thừa số nguyên tố của số rất lớn.

Nguyên lý sinh cặp khoá bí mật - công khai:

Chọn 2 số nguyên tố lớn, khác nhau: p, q.
Tính n = p * q (n dùng làm modulo, là phần của cả khoá công khai và bí mật).
Tính phi(n) = (p-1)(q-1) (hàm Euler).
Chọn số e sao cho 1 < e < phi(n) và gcd(e, phi(n)) = 1 (e nguyên tố cùng nhau với phi(n)). → Khoá công khai: (e, n)
Tính d là nghịch đảo modulo của e theo phi(n): d * e ≡ 1 (mod phi(n)). → Khoá bí mật: (d, n)
Mã hoá: Bản rõ M (số nguyên < n): C = M^e mod n

Giải mã: Bản mã C: M = C^d mod n

Vì sao an toàn: Biết (e, n) rất khó suy ra d nếu không biết p, q (phải phân tích n thành thừa số nguyên tố - với n đủ lớn, hiện chưa có thuật toán hiệu quả để làm việc này trong thời gian hợp lý bằng máy tính thông thường).
<img width="1027" height="496" alt="image" src="https://github.com/user-attachments/assets/44427b37-146b-4032-a49d-bb532f0d1437" />
Bài tập 3 — Mô hình áp dụng, so sánh, kết hợp
3 mô hình áp dụng RSA
Mô hình 1 - Xác thực người nhận (bảo mật / confidentiality) Người gửi mã hoá dữ liệu bằng KHOÁ CÔNG KHAI của người nhận. Chỉ người nhận (giữ khoá bí mật tương ứng) mới giải mã được.

Sơ đồ: Gửi --[mã hoá bằng public key B]--> Bản mã --[giải mã bằng private key B]--> Nhận

Mục đích: đảm bảo chỉ đúng người nhận B mới đọc được nội dung (bảo mật), không xác thực được ai là người gửi.

Mô hình 2 - Xác thực người gửi (chữ ký số / authentication) Người gửi "mã hoá" (thực chất là ký) dữ liệu (hoặc mã băm của dữ liệu) bằng KHOÁ BÍ MẬT của chính mình. Bất kỳ ai có khoá công khai của người gửi đều giải mã (xác minh chữ ký) được, qua đó xác nhận đúng là người gửi A đã tạo ra.

Sơ đồ: Gửi --[ký bằng private key A]--> Chữ ký --[xác minh bằng public key A]--> Nhận

Mục đích: xác thực nguồn gốc (đúng là A gửi), chống chối bỏ (non-repudiation), không đảm bảo bí mật vì ai cũng có public key A để "giải mã" xem nội dung.

Mô hình 3 - Kết hợp cả 2 (bảo mật + xác thực)

Người gửi A:

Ký lên dữ liệu (hoặc hash của dữ liệu) bằng private key của A.
Mã hoá (dữ liệu + chữ ký) bằng public key của người nhận B.
Người nhận B:

Giải mã bằng private key của B → lấy lại (dữ liệu + chữ ký).
Xác minh chữ ký bằng public key của A → xác nhận đúng A gửi và dữ liệu không bị sửa.
Mục đích: vừa đảm bảo bí mật (chỉ B đọc được), vừa xác thực người gửi (chắc chắn là A). Đây là mô hình dùng phổ biến trong thực tế (email ký số + mã hoá, HTTPS/TLS...).

So sánh thời gian mã hoá/giải mã AES vs RSA
Kết luận
AES nhanh, phù hợp mã hoá dữ liệu lớn, nhưng phải chia sẻ khoá bí mật trước.
RSA giải quyết bài toán trao đổi khoá an toàn nhưng chậm với dữ liệu lớn.
Kết hợp AES + RSA (Hybrid Encryption) tận dụng ưu điểm cả hai — đây là mô hình được dùng phổ biến trong thực tế như HTTPS/TLS, PGP/GPG.

