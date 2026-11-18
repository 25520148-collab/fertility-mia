# Tổng quan nghiên cứu

## Câu hỏi

1. **RQ1.** Fertility có tương quan với AUC và calibration sau khi kiểm soát perplexity không?
2. **RQ2.** Mức ảnh hưởng có khác nhau giữa Min-K%, Min-K%++ và detector không dựa trên likelihood không?
3. **RQ3.** Detector chuẩn hoá theo fertility có thu hẹp khoảng cách AUC giữa các ngôn ngữ không?

## Thiết kế và phạm vi

Cùng một cặp nội dung EN–L, PFR so số token của bản L với bản EN bằng cùng tokenizer revision. Nhóm khảo sát PFR cùng AUROC và khả năng chuyển ngưỡng giữa ngôn ngữ trong một chế độ phơi nhiễm bổ sung có kiểm soát. Phân tích cùng nội dung giúp so detector trên cohort có thể đối chiếu. Phân tích theo độ dài kiểm độ nhạy của kết quả trên vùng có đủ mẫu chung. Mỗi detector được chấm trên mẫu cùng điều kiện khi so ghép cặp.

Kết luận dự kiến áp dụng cho corpus, checkpoint, tokenizer và quy trình phơi nhiễm đã khảo sát. Nhãn trước và sau LoRA cần phân biệt nội dung đã được nhóm thêm vào tập huấn luyện và lịch sử pretraining của model gốc. So giữa các backbone khác nhau còn đi cùng thay đổi model và tập huấn luyện.

## Bằng chứng cần thu

- **Đã có:** protocol v2.14, bảng tra 32 nguồn, kế hoạch họp nhóm và fixture trên dữ liệu giả.
- **Đang chờ xác minh:** notebook pilot, exact split, ledger phơi nhiễm, checkpoint và cache gốc.
- **Chờ nhóm chốt:** outcome chính, panel và liều, quy tắc threshold, phân tích phi-likelihood và ứng viên RQ3.

Chi tiết ở [kế hoạch](plan.md), [hướng dẫn](analysis/protocols/implementation-guide.md) và [phụ lục bài báo](analysis/protocols/literature-application-map.md).
