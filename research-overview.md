# Tổng quan nghiên cứu

## Câu hỏi

1. **RQ1.** Trên tập ngôn ngữ và nội dung tương đương được khảo sát, PFR liên hệ thế nào với AUROC của detector khi phân biệt các đoạn thực sự được đưa vào huấn luyện LoRA với các đoạn đối chứng đã xác minh?
2. **RQ2.** Trên cùng tập mẫu, mối liên hệ giữa PFR và AUROC sau LoRA có khác giữa Min-K% và Min-K%++ không?
3. **RQ3.** Phương pháp chấm có xét fertility, được chọn trên dev, có giảm chênh lệch AUROC giữa các ngôn ngữ trên cùng tập mẫu đánh giá, đồng thời giữ mức suy giảm AUROC trung bình trong biên đã chốt và cải thiện nhóm ngôn ngữ có AUROC thấp được xác định trên dev không?

**Kết quả chính đã chốt trong câu hỏi.** RQ1 dùng **AUROC sau LoRA**; `ΔAUROC = AUROC_sau − AUROC_0×` là bổ trợ trên cùng mẫu và nhãn; chuyển ngưỡng và FPR/TPR ở phần đánh giá riêng. RQ2 dùng **độ dốc theo PFR của chênh AUROC** giữa hai detector, không phải chênh AUROC trung bình. RQ3 dùng ba tiêu chí và chỉ mở test khi có công thức đổi được thứ hạng trong cùng ngôn ngữ. Nếu panel chỉ có Anh–Trung, kết luận giới hạn ở hai ngôn ngữ đó. Lý do và phép đo ở [kế hoạch §1](plan.md).

## Thiết kế và phạm vi

Cùng một cặp nội dung EN–L, PFR so số token của bản L với bản EN bằng cùng tokenizer revision. Nhóm khảo sát PFR cùng AUROC và khả năng chuyển ngưỡng giữa ngôn ngữ trong một chế độ phơi nhiễm bổ sung có kiểm soát. Phân tích cùng nội dung giúp so detector trên cohort có thể đối chiếu. Phân tích theo độ dài kiểm độ nhạy của kết quả trên vùng có đủ mẫu chung. Mỗi detector được chấm trên mẫu cùng điều kiện khi so ghép cặp.

Kết luận dự kiến áp dụng cho corpus, checkpoint, tokenizer và quy trình phơi nhiễm đã khảo sát. Nhãn trước và sau LoRA cần phân biệt nội dung đã được nhóm thêm vào tập huấn luyện và lịch sử pretraining của model gốc. So giữa các backbone khác nhau còn đi cùng thay đổi model và tập huấn luyện.

## Bằng chứng cần thu

- **Đã có:** protocol v2.15, phụ lục 32 nguồn đọc hai chiều (phần việc → bài, bài → vai trò), kế hoạch họp nhóm và fixture trên dữ liệu giả.
- **Đang chờ xác minh:** notebook pilot, exact split, ledger phơi nhiễm, checkpoint và cache gốc.
- **Chờ nhóm chốt:** số ngôn ngữ thật của panel, detector primary của RQ1, thang PFR dùng chung, bin `pfr_i` trong ngôn ngữ, panel và liều, quy tắc threshold, ứng viên RQ3. Danh sách M1–M10 ở [phiếu họp](group-meeting.md).

Chi tiết ở [kế hoạch](plan.md), [hướng dẫn](analysis/protocols/implementation-guide.md) và [phụ lục bài báo](analysis/protocols/literature-application-map.md).
