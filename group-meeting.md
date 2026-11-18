# Phiếu họp nhóm · kế hoạch fertility-mia v2.15

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
| RQ1 | **Đã chốt trong câu RQ:** AUROC sau LoRA là chính, ΔAUROC bổ trợ trên cùng mẫu/nhãn, chuyển ngưỡng ở phần riêng. Length-matched là sensitivity, test hai phía. **Còn mở:** M1 số ngôn ngữ, M2 biến độ khó, M3 thang PFR | Intersection, PFR theo phiên bản, support, proxy tiền LoRA, CI/power theo mẫu thật | |
| Chuyển ngưỡng | Pooled calibration với trọng số cố định. Absolute FPR gap. Report reference matrix bổ trợ | Số negatives calibration/test theo ô, achieved FPR/ties, CI và α có lý do | |
| Panel/adapter/dose | So một backbone sâu, hai backbone định hướng replication, hoặc 3×8 nếu đủ nguồn lực. Ghi dose theo actual stream | Bảng chi phí và capability. Chọn kiểu adapter, sham nếu cần, max wall time/VRAM/storage, seed floor | |
| RQ2 | **Đã chốt trong câu RQ:** đầu ra chính là **độ dốc theo PFR của chênh AUROC**, cùng mẫu/thang/nhãn như RQ1; ca kiểm A hơn B 0,05 phải cho độ dốc 0. B0 kiểm lệch dữ liệu. Phi-likelihood là mở rộng. **Còn mở:** M4 ngưỡng đủ điểm để fit độ dốc | Implementations và test fixtures, source và score direction | |
| RQ3 | **Giữ trong kế hoạch.** Một variant chọn trên dev, ba tiêu chí: SD giảm + mean non-inferior + low-group cải thiện. **Điều kiện cần:** ví dụ tính tay cho thấy công thức đổi được thứ hạng trong cùng ngôn ngữ, và đầu vào có sẵn lúc chấm. **Còn mở:** M5 ứng viên công thức, M6 q/δ/CI/multiplicity | Minh họa rank đã đổi, input lúc inference, disjoint dev/cal/test | |
| Phạm vi bảo vệ | Báo seed-specific và per-language. Nếu muốn bảo vệ mọi ngôn ngữ, thêm biên giảm tối đa theo ngôn ngữ | Nhóm chốt biên có ý nghĩa và simultaneous uncertainty trước test | |
| Claim và phạm vi | Bài báo về added exposure và độ nhạy đo lường trên panel khảo sát | Claim ledger và kiểm Related Work trước khi chốt lời giới thiệu | |
| Ký chạy | Chọn cap, mốc, phân công, phiên bản protocol và analysis commit | Điền đủ các mục ở trên hoặc ghi phạm vi mô tả tương ứng | |

## Quyết định còn mở sau khi chỉnh RQ (18/11)

Ba câu RQ đã sửa trực tiếp trong [plan §1](plan.md#1-câu-hỏi-và-kết-quả-sẽ-báo-cáo) và đồng bộ ở §3. Mười một mục dưới đây **chưa chốt** và chặn các bước tương ứng.

| # | Quyết định còn mở | Chặn gì | Ai quyết / khi nào |
|---|---|---|---|
| M1 | **Panel thật có mấy ngôn ngữ, tên cụ thể.** Danh sách ngôn ngữ của pilot **chưa được xác minh** với notebook và split gốc. Câu RQ1 mới đã có nhánh **Anh–Trung** nhưng nhánh đó chỉ mô tả hai ngôn ngữ | Quyết định RQ1 là **suy luận** hay **chỉ mô tả**; và RQ2 có đủ điểm để ước lượng độ dốc hay không | Người giữ pilot · P01, 22–29/11 |
| M2 | **Biến đo độ khó trước LoRA** — chốt đại lượng nào, đo ở checkpoint nào. RQ1 mới ghi "chỉ thực hiện khi biến đo đã được chốt và dữ liệu đủ để diễn giải" | Ước lượng có điều chỉnh của RQ1. Chưa chốt thì **chỉ báo bản chưa điều chỉnh** kèm lý do | Methods · C-final 13/12 |
| M3 | **Thang PFR dùng chung cho RQ1 và RQ2** (median các tỷ số cặp, ratio-of-totals, hay log) | Độ dốc của RQ2 — đổi thang là đổi đơn vị hệ số | Methods · trước confirmatory test |
| M4 | **Ngưỡng "quá nhỏ để ước lượng độ dốc"** của RQ2. Dưới ngưỡng thì chuyển sang so ghép cặp từng ngôn ngữ và đánh dấu RQ2 chưa trả lời đầy đủ | Khi nào RQ2 được coi là đã trả lời | Cả nhóm · C-final |
| M5 | **Ứng viên công thức RQ3** và kết quả ví dụ tính tay. Giữ RQ3 trong kế hoạch; cần công thức **đổi được thứ hạng trong cùng ngôn ngữ**, đầu vào **có sẵn lúc chấm**, và biên suy giảm `δ` | Mở test RQ3. Chưa có ứng viên thì ghi điều kiện triển khai, không trình như đã trả lời | Đội detector · C-final |
| M6 | **`q`, `δ`, mức CI và quy tắc multi-testing** cho ba tiêu chí RQ3 | CI một phía của `ΔD`, `Δmean`, `Δlow` | Methods · trước test |
| M7 | **Thống nhất tên AUC / AUROC** toàn kế hoạch. Ba RQ mới dùng AUROC; các mục khác còn viết AUC — cùng một đại lượng, chưa đổi đồng loạt để diff nhỏ | Chỉ là nhất quán thuật ngữ trong bản thảo, không chặn phép đo | Writing lead · trước W1 |
| M8 | **Detector primary của RQ1.** Đề xuất Min-K% native `k = 20%` | Chọn detector sau khi xem số là một dạng chọn kết quả. Chưa chốt thì RQ1 chưa có kết quả chính | Methods · C-final, trước khi xem kết quả |
| M9 | **Bin `pfr_i` trong ngôn ngữ**: số bin, biên bin chốt trên dev, số mẫu tối thiểu mỗi lớp mỗi bin | Phân tích bổ trợ trong ngôn ngữ của RQ1 và RQ2. Đặc biệt cần nếu panel chỉ có Anh–Trung | Methods · trước confirmatory test |
| M10 | **Số ngôn ngữ tối thiểu để chạy ba tiêu chí RQ3.** Dưới ngưỡng thì chỉ báo AUROC native và biến thể theo từng ngôn ngữ, đánh dấu RQ3 chưa trả lời | Khi nào RQ3 được coi là đã trả lời | Cả nhóm · C-final |
| M11 | **Lời đóng góp của nhóm còn viết theo câu RQ cũ.** Ví dụ đóng góp gắn với RQ3 vẫn nói "thu hẹp khoảng cách AUC". Phần lời đóng góp do nhóm sở hữu nên agent không tự sửa | Câu đóng góp trong Introduction và abstract phải khớp ba RQ mới | Cả nhóm · trước W1 |

**Hai mục đã được câu RQ mới chốt, ghi lại để không mở lại:** kết quả chính của RQ1 là **AUROC sau LoRA** (ΔAUROC là bổ trợ trên cùng mẫu và nhãn; chuyển ngưỡng và FPR/TPR ở phần đánh giá riêng), và đầu ra chính của RQ2 là **độ dốc theo PFR của chênh AUROC**, không phải chênh AUROC trung bình.

### Bảy ngày tới

- Ngày 1–2. Họp và mở tài sản pilot. Ghi ai giữ từng file, phạm vi chia sẻ và ngày nhận.
- Ngày 2–4. Chuẩn bị tokenizer/corpus manifest cho P02b, mở đúng phần Method của R5/R21, đối chiếu giải thích trong phụ lục.
- Ngày 3–5. Rà native scoring và đầu vào Min-K%++. Chuẩn bị ca thử score sign, selection/ties và short texts.
- Ngày 5–7. Nếu có split, kiểm leakage/overlap và trình bảng số family theo ô/lớp. Nếu thiếu, lập danh sách chặn và phương án rerun. Ghi một quyết định tạm về panel để lên lịch profiling.
