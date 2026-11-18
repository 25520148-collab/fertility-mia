# Thẻ ngữ cảnh · fertility-mia v2.14

Đọc [kế hoạch](plan.md), [phiếu họp](group-meeting.md), [phụ lục bài báo](analysis/protocols/literature-application-map.md) và [review mới nhất](reviews/codex-2026-11-18-v213.md). Đọc [tổng quan nghiên cứu](research-overview.md) để xem phạm vi và tiến độ.

- Pilot Qwen2.5-1.5B/OPUS-100 do nhóm báo cáo, đang chờ raw/notebook, exact split, family IDs và exposure/cache manifest. 0× là trước added exposure. Chốt label theo run, span và view. Translation-only có cohort riêng. Freeze 10/01/2027, bản thảo 31/01/2027, T4 Colab.
- RQ1 chính đề xuất association có điều kiện trên panel và comparable content. Length-matched là sensitivity với support, vì cố định cả EN token count và target token count khóa luôn PFR. Covariate NLL cần forward cache và đo rank/support trên panel thực. Outcome AUC hoặc ΔAUC tùy mục tiêu, sử dụng joint bootstrap đánh giá precision.
- RQ2 giữ native Min-K20 và Min-K%++, comparator phi-likelihood chờ feasibility. RQ3 chốt variant trên dev và ba điều kiện cho dispersion, mean và nhóm low-AUC đã khóa.
- P01 thu hồi tài sản và P02b prep chạy song song. P02c cần exact split. C-final 13/12 chốt panel, dose, CI/precision, chi phí, detector và approval record trước D. Bản 3×8 là ứng viên dưới cap.
- Phụ lục v2.14 có 32 nguồn và [sổ tay theo từng bài](analysis/protocols/paper-concepts.md). Xem [hướng dẫn cụ thể theo từng bước](analysis/protocols/implementation-guide.md) trước khi làm. Dùng R22 bản Findings EACL 2026, R3 IEEE SPW 2025 và phân biệt PFR của Petrov với tax của Srivastava. PDF/HTML trước đây dùng để tra lịch sử.
