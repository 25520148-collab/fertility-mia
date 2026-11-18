# Protocol và kiểm tra trước khi có dữ liệu pilot

Các tệp trong [protocols](protocols/implementation-guide.md) ghi cách đếm PFR, gán nhãn, chấm score và suy luận. Fixture dùng trường hợp giả để kiểm các định nghĩa và phép tính đã có. Chạy từ thư mục gốc với Python 3:

```bash
python analysis/protocols/fixtures.py
```

[Kết quả fixture tham chiếu](protocols/fixtures-output.json) là số tổng hợp. Kết quả thực nghiệm của nhóm có vị trí trong [khung bản thảo](../paper/manuscript-outline.md) sau khi có artifact đã kiểm và được duyệt chia sẻ.
