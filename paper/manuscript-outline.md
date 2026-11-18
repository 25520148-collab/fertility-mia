# Khung bản thảo để nhóm cùng viết

Đây là outline làm việc. Dùng [kế hoạch v2.15](../plan.md) cho các lựa chọn thiết kế và [sổ đối chiếu kết luận](claim-ledger.md) để kiểm từng câu định lượng.

| Phần | Nội dung cần viết | Bằng chứng trước khi chốt |
|---|---|---|
| **Abstract** | Câu hỏi, thiết kế, kết quả chính, giới hạn khái quát | Kết quả đã xác thực và đúng phạm vi checkpoint/exposure |
| **Introduction** | Vì sao đo contamination đa ngôn ngữ cần quan tâm tokenizer, ba RQ và mục tiêu đóng góp | R5/R21 về fertility, R9/R19/R22 về prior art, R25/R30 về thiết kế đối chứng |
| **Related Work** | Likelihood detectors, blind shortcuts, tokenizer fairness, exposure qua dịch, nghiên cứu controlled exposure | [Phụ lục tra nguồn](../analysis/protocols/literature-application-map.md), đúng version và section |
| **Data and Exposure** | Corpus, tỷ lệ intersection, family split, baseline 0×, target run, nhãn direct/related/partial/unknown | [Protocol PFR và split](../analysis/protocols/pfr-and-splits.md), manifest, log optimizer-visible |
| **Measurement and Analysis** | PFR/tax, native Min-K và Min-K%++, **AUROC sau LoRA làm kết quả chính** và ΔAUROC bổ trợ, phân tích trong ngôn ngữ theo bin `pfr_i`, threshold transfer ở phần riêng, RQ3 và CI ghép cặp | [Quyết định đo lường](../analysis/protocols/measurement-decisions.md) và prereg đã duyệt |
| **Results** | Bảng coverage và integrity; RQ1 PFR–AUROC sau LoRA, rồi ΔAUROC và threshold transfer; RQ2 **độ dốc theo PFR của chênh AUROC**, kèm AUROC từng detector; RQ3 mean, dispersion, low-group và per-language | Artifact theo run, seed, cohort, comparator, counts và CI. Ghi riêng báo cáo mô tả nếu support thiếu |
| **Discussion, Limitations, Ethics** | Scope của LoRA, translation spillover, model/tokenizer, precision, quyền chia sẻ dữ liệu | Diễn giải đúng từng estimand, công bố việc nhóm đã duyệt |
| **Conclusion** | Trả lời từng RQ theo số liệu và mức độ bất định | Đối chiếu manuscript với claim ledger |
| **Reproducibility Appendix** | Revisions, preprocessing, hashes, scorer configuration, constraints và deviations | Chỉ dẫn tái lập và provenance đủ để reviewer kiểm |

Tên người viết và người rà cho từng mục được nhóm ghi trong Issue hoặc [phiếu họp](../group-meeting.md).
