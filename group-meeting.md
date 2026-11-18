# Phiếu họp nhóm · kế hoạch fertility-mia v2.14

Đọc trước [kế hoạch](plan.md), [hướng dẫn minh hoạ](analysis/protocols/implementation-guide.md) và hàng RQ phụ trách trong [phụ lục bài báo](analysis/protocols/literature-application-map.md). Dùng 45 phút. Điền tên và quyết định ngay trong biên bản của nhóm sau cuộc họp.

## Chuẩn bị và chương trình họp

| Phút | Nội dung | Đầu ra cần có |
|---|---|---|
| 0–8 | Người đã chạy pilot mở notebook/Drive và kiểm run gốc | Ai giữ text/split/labels, checkpoint/adapter/cache và đề cương. Ngày trao quyền đọc, hash hoặc vị trí nội bộ |
| 8–18 | Methods trình ví dụ cùng nội dung và cùng token count | Chọn population và outcome của RQ1. Quy định khi nào RQ1 adjusted hoặc calibration chỉ là mô tả |
| 18–27 | Data/compute trình 1, 2, 3 model cùng cap | Chọn panel dự kiến, yêu cầu intersection/coverage, seed floor, exposure unit và profiling |
| 27–36 | Đội detector đối chiếu R1/R2/R3/R18 và đề xuất RQ3 | Chốt ai rà native implementation, ứng viên phi-likelihood, variant RQ3 và inference input |
| 36–45 | Writing ghi claims, nguồn và chốt người/hạn | Mỗi đầu việc một người chịu trách nhiệm và một người kiểm. Ghi ngày C-prep/C-final và các mục cần dữ liệu mới |

## Phiếu quyết định

| Mục cần chốt | Đề xuất để thảo luận | Bằng chứng cần trước khi ký | Quyết định / người / ngày |
|---|---|---|---|
| Exact pilot | Tái lập nếu manifest tái dựng được. Nếu thiếu, chọn rerun có version hoặc làm hồ sơ phương pháp | Các tệp P01, hashes, label join và run IDs | |
| Nhãn và overlap | Direct vs verified family-unexposed làm cohort chính, translation-only là nhánh transfer | Cho ví dụ một family theo các view và biểu diễn nào đã vào optimizer. Chốt partial, unknown và count kiểm chứng | |
| RQ1 | Native AUC(after) trên tập comparable content, ΔAUC bổ trợ. Length-matched là sensitivity, test hai phía | Intersection, PFR theo phiên bản, support, proxy tiền LoRA, CI/power theo mẫu thật | |
| Chuyển ngưỡng | Pooled calibration với trọng số cố định. Absolute FPR gap. Report reference matrix bổ trợ | Số negatives calibration/test theo ô, achieved FPR/ties, CI và α có lý do | |
| Panel/adapter/dose | So một backbone sâu, hai backbone định hướng replication, hoặc 3×8 nếu đủ nguồn lực. Ghi dose theo actual stream | Bảng chi phí và capability. Chọn kiểu adapter, sham nếu cần, max wall time/VRAM/storage, seed floor | |
| RQ2 | Min-K20 và Min-K%++ cùng mẫu. Phi-likelihood có input contract, hoặc nhóm duyệt partial | Implementations và test fixtures, source và score direction | |
| RQ3 | Một variant dev, SD giảm + mean NI + low-group cải thiện. Xác định q, δ, CI, coverage | Minh họa rank đã đổi, input lúc inference, disjoint dev/cal/test | |
| Phạm vi bảo vệ | Báo seed-specific và per-language. Nếu muốn bảo vệ mọi ngôn ngữ, thêm biên giảm tối đa theo ngôn ngữ | Nhóm chốt biên có ý nghĩa và simultaneous uncertainty trước test | |
| Claim và phạm vi | Bài báo về added exposure và độ nhạy đo lường trên panel khảo sát | Claim ledger và kiểm Related Work trước khi chốt lời giới thiệu | |
| Ký chạy | Chọn cap, mốc, phân công, phiên bản protocol và analysis commit | Điền đủ các mục ở trên hoặc ghi phạm vi mô tả tương ứng | |

### Bảy ngày tới

- Ngày 1–2. Họp và mở tài sản pilot. Ghi ai giữ từng file, phạm vi chia sẻ và ngày nhận.
- Ngày 2–4. Chuẩn bị tokenizer/corpus manifest cho P02b, mở đúng phần Method của R5/R21, đối chiếu giải thích trong phụ lục.
- Ngày 3–5. Rà native scoring và đầu vào Min-K%++. Chuẩn bị ca thử score sign, selection/ties và short texts.
- Ngày 5–7. Nếu có split, kiểm leakage/overlap và trình bảng số family theo ô/lớp. Nếu thiếu, lập danh sách chặn và phương án rerun. Ghi một quyết định tạm về panel để lên lịch profiling.
