# Protocol PFR, support và split · v2.14

Đặc tả cho [kế hoạch](../../plan.md). [R5, R13, R17 và R21](literature-application-map.md) xác định thước đo, nguồn song song và giới hạn corpus. [Fixture định nghĩa](fixtures.py) dùng dữ liệu tổng hợp.

## P01 · Manifest và nhãn

| Bảng | Trường bắt buộc |
|---|---|
| Corpus | `corpus_id, source_version, sample_id, en_pivot_id, lang, family_id, source_group_id, text_hash, unicode_policy` |
| Target runs | `target_id, base_revision, tokenizer_revision, adapter_id, seed, dose_id, settings_hash, stream_hash, steps, bytes, tokens` |
| Exposure | `target_id, sample_id, family_id, exposure_role, count, visible_span_hash` và trạng thái direct, translation-only, control hoặc unknown |
| Detector | `target_id, sample_id, family_id, meta_split, score_protocol_id, retained_span_hash, n_tokens, score, invalid_reason` |

Ghép nhãn theo target/run trước khi tính metric. Dùng actual optimizer-visible text, gồm masking/truncation và background. Giữ translation family cùng role trong split cho detector, khóa split trước fit. Near-dup/source grouping ghi version và policy. Với randomized family assignment, lưu seed/strata và xác suất phân nhóm, shuffle nhãn family trong đúng strata nếu làm randomization diagnostic. 0× dùng nhãn intended assignment có ghi provenance. Một EN pivot dùng ở nhiều ngôn ngữ vẫn là cùng block khi resampling.

### Chuyển trạng thái sang nhãn theo estimand

Lưu riêng `assigned`, `direct_scored_span_count`, `related_view_count`, `partial_span_count`, `background_match` và `status_verified`. Ghi scope của phép dò nguồn. Với dữ liệu có nhiễu, bảo toàn ban đầu và ghi lý do vào deviation log.

| View sau kiểm stream | Direct vs family-unexposed | Translation transfer vs verified control |
|---|---|---|
| Direct toàn scored span | Positive | Cohort direct riêng |
| Chỉ bản dịch/biến thể liên quan | Cohort transfer riêng | Positive |
| Đối chứng xác thực chưa thấy family trong run | Negative | Negative |
| Có một phần scored span, background overlap chưa chuẩn hoá, hoặc unknown | Báo count, áp policy thiếu dữ liệu đã khóa | Báo count, áp policy thiếu dữ liệu đã khóa |

Assignment-based analysis nếu thực hiện dùng nhãn dự kiến tại cả hai checkpoint. Bảng compliance công bố tỷ lệ direct/related/partial/unknown theo arm. AUC trước/after của direct analysis sử dụng cùng cohort đủ điều kiện và cùng label map, để việc đổi case không làm thay estimand.

## P02b · Hai phép đo corpus

- Chạy bảng reference FLORES theo cùng IDs ở hai phía, phiên bản tokenizer và NFC hay native được ghi rõ, loại special tokens, giữ full content. Tái tạo protocol của Petrov ở panel kiểm bằng cách nối dev + devtest như code tác giả, tách riêng với sentence-wise protocol của nhóm. Lệch thì đối chiếu code và versions trước khi kết luận.
- Exact OPUS matrix dùng sample IDs của pilot nếu tái lập. Dùng khóa EN pivot + nguồn, disambiguate exact duplicates, báo count đa ngôn ngữ intersection, domain mix, positivity/label coverage sau lọc. Khi tập giao quá nhỏ, chỉ mô tả pairwise corpus composition hoặc chốt nghiên cứu mới.
- Viết `PFR_i=T_L/T_EN`. Báo median, quantiles và ratio-of-totals riêng. Với mẫu số 0 gắn invalid. Whitespace tax là tokens/whitespace-word ở hai ngôn ngữ mỗi dòng, chỉ báo ở scripts thích hợp. Các proxy NLL phát sinh từ checkpoint scoring stage.
- Thiết kế bảng support cho length groups trước test. Với mỗi panel cell/bin báo positives, negatives, unique families, retained coverage, PFR variation và mức thay đổi composition. Bins dựa vào số token đã chấm, PFR chính dùng content chưa truncate. Lưu cả hai count và flags. Báo lengths trước và sau lọc để truy ra selection. Báo khi không đủ hai lớp để tính AUROC.

## P02c · Audit overlap trên exact pilot

1. Tạo view audit NFC có whitespace policy được khóa, giữ raw text và hashes.
2. Với mỗi language/target, kiểm exact, near-dup và cross-family translation link theo exposure, background và eval role. Tính một thống kê directional overlap đã khóa, ví dụ số char n-grams khác biệt của heldout xuất hiện trong exposed index chia tổng n-grams khác biệt của câu heldout. Chọn n trước và báo số câu ngắn không đủ gram.
3. Báo coverage/membership provenance per cell, histogram hoặc quantiles, tóm tắt cổ chai và tất cả vi phạm theo family. P02c cần đúng pilot split. Không đổi tiêu chí sau thấy hướng AUC. Nếu sửa split phải lưu version, rerun kế hoạch tương ứng và ghi rõ so sánh nào còn hợp lệ.
