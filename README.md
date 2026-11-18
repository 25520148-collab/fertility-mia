# Fertility-MIA

Để làm việc với Claude, mở [prompt nghiên cứu của nhóm](analysis/research-agent-prompt.md), chọn P01, P03/RQ2 hoặc review RQ3 và cung cấp các file ghi trong yêu cầu.

**Tokenizer Fertility as a Confound in Likelihood-Based Contamination Detection**

Dự án nghiên cứu về mối liên hệ giữa số token cần để biểu diễn cùng nội dung bằng nhiều ngôn ngữ và độ nhạy của các detector contamination dựa trên likelihood. Thiết kế hiện hành dùng **phơi nhiễm bổ sung có kiểm soát bằng LoRA**, với nhãn theo từng checkpoint và từng bản văn bản.

**Trạng thái:** kế hoạch v2.14 · tài liệu cập nhật ngày 18/11/2026 · kết quả pilot đang chờ đối chiếu với notebook, split và log gốc.

## Bắt đầu ở đây

| Bạn muốn | Mở |
|---|---|
| Hiểu đề tài, giả thuyết và phạm vi kết luận | [Tổng quan nghiên cứu](research-overview.md) |
| Họp nhóm và phân công | [Phiếu họp 45 phút](group-meeting.md) |
| Xem thiết kế, công việc, đầu ra và các mốc | [Kế hoạch v2.14](plan.md) |
| Biết phải làm gì với dữ liệu, score và bảng kết quả | [Hướng dẫn từng bước](analysis/protocols/implementation-guide.md) |
| Tìm bài nào hỗ trợ phần nào của thiết kế | [Phụ lục 32 bài báo](analysis/protocols/literature-application-map.md) |
| Hiểu PFR, Min-K%++, exposure, AUC và các khái niệm theo từng nguồn | [Sổ tay khái niệm](analysis/protocols/paper-concepts.md) |
| Đối chiếu quy tắc gán nhãn và phép đo | [Protocol PFR và split](analysis/protocols/pfr-and-splits.md) · [Quyết định đo lường](analysis/protocols/measurement-decisions.md) |
| Xem lỗi thiết kế đã được phân tích | [Phản biện v2.13 → v2.14](reviews/codex-2026-11-18-v213.md) |
| Cùng viết bài | [Khung bản thảo](paper/manuscript-outline.md) · [Sổ đối chiếu kết luận](paper/claim-ledger.md) |
| Chạy thử các phép kiểm toy | [Hướng dẫn fixture](analysis/README.md) |

## Làm việc cùng nhau trên GitHub

- Mỗi đầu việc dùng một Issue để ghi người phụ trách, đầu ra và hạn.
- Từ `main`, tạo nhánh riêng cho mỗi đầu việc. Mở Pull Request kèm link Issue, phần thay đổi và cách kiểm. Nhờ một thành viên đối chiếu số liệu hoặc nguồn trước khi merge.
- Khi đổi giả thuyết, chỉ số chính, cohort hoặc cấu hình chạy, ghi quyết định của nhóm trong PR và cập nhật [kế hoạch](plan.md) cùng lượt.
- Repo public dùng cho tài liệu có thể chia sẻ, dữ liệu tổng hợp và kết quả đã được nhóm duyệt công bố. Tài sản pilot nội bộ được theo dõi qua tên artifact hoặc hash. Xem [quy ước đóng góp](CONTRIBUTING.md).
