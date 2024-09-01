# Thuật Toán Caesar

Thuật toán Caesar là một trong những phương pháp mã hóa cổ điển và đơn giản nhất. Nó là một dạng mã hóa thay thế, trong đó mỗi ký tự trong bản rõ (plaintext) được thay thế bằng một ký tự khác trong bảng chữ cái, cách nó một số vị trí nhất định. Số vị trí dịch chuyển này được gọi là "khóa" của thuật toán.

## Cách Hoạt Động của Thuật Toán Caesar

1. **Bảng Chữ Cái:** Thuật toán sử dụng một bảng chữ cái cố định, ví dụ là bảng chữ cái tiếng Anh gồm 26 ký tự: `A, B, C, ..., Z`.

2. **Khóa (Key):** Một số nguyên `k` được chọn làm khóa mã hóa. Khóa này xác định số lượng ký tự dịch chuyển. Ví dụ, nếu `k = 3`, mỗi ký tự sẽ được dịch chuyển 3 vị trí trong bảng chữ cái.

3. **Mã Hóa:**
    - Đối với mỗi ký tự trong bản rõ, tìm vị trí của nó trong bảng chữ cái.
    - Dịch chuyển ký tự đó về phía trước trong bảng chữ cái bằng số lượng vị trí tương ứng với khóa.
    - Nếu vượt quá cuối bảng chữ cái, quay vòng lại bắt đầu từ ký tự đầu tiên.
    - Ký tự dịch chuyển mới này chính là ký tự đã được mã hóa.

    **Công Thức:**
    ```plaintext
    C = (P + k) mod 26
    ```
    - `C`: Ký tự đã mã hóa.
    - `P`: Vị trí của ký tự trong bảng chữ cái.
    - `k`: Khóa.

4. **Giải Mã:**
    - Để giải mã một ký tự đã mã hóa, thực hiện quy trình ngược lại: dịch chuyển ký tự đó về phía sau trong bảng chữ cái bằng số lượng vị trí tương ứng với khóa.
    - Nếu vượt quá đầu bảng chữ cái, quay vòng lại từ ký tự cuối cùng.

    **Công Thức:**
    ```plaintext
    P = (C - k) mod 26
    ```
    - `P`: Ký tự sau khi giải mã.
    - `C`: Vị trí của ký tự đã mã hóa trong bảng chữ cái.
    - `k`: Khóa.

## Ví Dụ

Giả sử ta muốn mã hóa từ "HELLO" với khóa `k = 3`:

- H (vị trí 7) -> K (vị trí 10)
- E (vị trí 4) -> H (vị trí 7)
- L (vị trí 11) -> O (vị trí 14)
- L (vị trí 11) -> O (vị trí 14)
- O (vị trí 14) -> R (vị trí 17)

Vậy, bản mã là "KHOOR".

## Ưu Điểm và Nhược Điểm

- **Ưu điểm:** Đơn giản, dễ hiểu và dễ thực hiện.
- **Nhược điểm:** Dễ bị phá mã bằng cách thử khóa (brute force), đặc biệt khi số lượng khóa có thể có là nhỏ (với bảng chữ cái 26 ký tự, chỉ có 25 khóa khác nhau).

## Ứng Dụng

Mặc dù không còn được sử dụng trong các hệ thống mã hóa hiện đại do tính bảo mật thấp, thuật toán Caesar vẫn được sử dụng để giảng dạy các nguyên lý cơ bản của mã hóa, cũng như trong các trò chơi giải đố hoặc mã hóa đơn giản.

## Hướng Dẫn Sử Dụng

1. **Mã Hóa Một Chuỗi:**
    - Nhập chuỗi cần mã hóa.
    - Chọn khóa `k` (số lượng vị trí cần dịch chuyển).
    - Thuật toán sẽ xuất ra chuỗi đã được mã hóa.

2. **Giải Mã Một Chuỗi:**
    - Nhập chuỗi đã mã hóa.
    - Nhập khóa `k` đã sử dụng để mã hóa.
    - Thuật toán sẽ xuất ra chuỗi bản rõ.

## Kết Luận

Thuật toán Caesar là một trong những thuật toán mã hóa đơn giản nhất, chủ yếu được sử dụng để minh họa các nguyên lý cơ bản về mã hóa. Tuy nhiên, do tính bảo mật thấp, nó chỉ thích hợp cho các ứng dụng có yêu cầu bảo mật không cao hoặc trong mục đích giáo dục.

---

This README provides a detailed explanation of the Caesar cipher algorithm, along with examples and guidance on its usage. The simplicity of the Caesar cipher makes it an excellent educational tool for understanding the basic principles of cryptography.
