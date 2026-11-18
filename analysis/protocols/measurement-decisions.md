# Phiếu đo lường · v2.14

Dùng cùng [plan](../../plan.md) và [phiếu họp](../../group-meeting.md). Các chính sách cần nhóm ký ở C-final. Đối chiếu source theo [Phụ lục A](literature-application-map.md).

| Mục | Quyết định cần khóa | Đầu ra kiểm được |
|---|---|---|
| PFR | Tokenizer revision, text view, gộp cặp, trọng số | Cặp IDs, missing/zero denominators, quantiles, cross-language intersection |
| RQ1 outcome | AUC(after) hoặc ΔAUC theo câu hỏi, một primary | Cùng eval labels/cases cho before/after, paired CI |
| RQ1 length | Tập comparable content và sensitivity theo token bins | Support chart, per-class counts, variance PFR còn lại, drop/retention |
| RQ1 adjustment | Proxy tiền LoRA, units, weighting, estimation population | Design matrix có rank/support và báo leverage/leave-one-language-out |
| RQ1 threshold | Score > τ, reference weights, α, minimum positive/negative families, absolute gap | Achieved calibration/test rates và ties, refit trong bootstrap. Bảng per-language có counts |
| RQ2 | Native baselines, predeclared signed contrast hoặc magnitude contrast có CI phù hợp | Common cases, sign, k, short-text utilization, phi-likelihood feasibility |
| RQ3 | Một formula khóa trên dev, inference input, minimum coverage, dispersion, q, δ, α | Native/variant scores merged on same IDs. Low-group khóa từ dev, báo CI ghép cặp |
| Precision | Conditional inference panel hay generalization, estimand, family of tests | Joint resampling và seed-level output, simulation assumptions, Monte Carlo error |
| Exposure | Dose unit, optimizer-visible text, background, sham và assignment | Manifest theo adapter/checkpoint với actual bytes, tokens, copies, steps |

## Chính sách triển khai

- Cột đối tượng ngưỡng ghi shared-adapter, cross-adapter hoặc within-adapter. Đề xuất rule empirical là chọn cutoff quan sát nhỏ nhất trong calibration negatives sao cho tỷ lệ trọng số có `score > τ` không vượt α. Chốt trọng số và tie rule trước. Ghi raw rates và gap để nhận ra pooled-rate che lệch theo language.
- RQ2 report detector-AUC table và contrast của PFR slope có bootstrap chung. RQ3 giữ cohort chung và eligibility theo language/class, công bố seed aggregation, lower-group từ dev và per-language harms. Các quyết định có ví dụ trong [hướng dẫn](implementation-guide.md).

- `score > τ` và chiều score cao hơn hướng member. Trên calibration chọn quantile empirical với policy được khóa. Khi trùng ties báo realized rate. Metadata ghi cutoffs, số token thực sự chấm, score orientation và null reason. Test chỉ áp dụng ngưỡng đã fit cho checkpoint/detector.
- Báo `FP/N_0` và `TP/N_1` từng ô. Với 150 negatives độc lập, mỗi event đổi FPR khoảng 0,67 điểm phần trăm. Nếu thấy 0/150, cận exact một phía 95% là khoảng 1,98%. Đây là phép tính minh họa cho test iid. Calibration và test cần dự toán riêng, điều chỉnh theo clusters/weights. Thiếu precision thì bỏ claim confirmatory tại FPR 1%.
- Native Min-K%++ từ full-vocab log-softmax. `μ=sum(p log p)`, `σ²=sum(p log² p)−μ²`. Ghi dtype của phép tính, baseline rounding, tolerance nhỏ do số học và flag σ gần 0. Lưu cache sufficient statistics cùng masks/prefix/revisions. So cache với direct scorer trên fixture. Báo native k và số trường hợp 1–2 selected tokens theo lớp/ngôn ngữ.
- AUC ties cho nửa điểm. Để tính ΔAUC, đồng thời lấy resample weights cho cả checkpoint và chạy lại AUC cho cùng labels. Trên cùng family giữa translations/cells giữ cùng trọng số resampling. Raw-score correlation chỉ mô tả.
- Scoring variant so cùng eligible support. Mỗi báo cáo có count của all eligible, NaN, short/truncated, usable paired. Nếu đổi eligibility, có bảng sensitivity trên shared cases và coverage riêng theo label/language.
- FPR và TPR dùng cohort có nhãn assignment/exposure được xác thực cho checkpoint. Cohort thiếu nhãn chỉ báo flag rates, disagreement, coverage và mô tả reference set. Bootstrap calibration và test tách theo vai trò.
