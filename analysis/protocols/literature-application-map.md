# Phụ lục A · Bài báo dùng ở đâu trong fertility-mia

Bản tra cứu v2.14 · 18/11/2026. Bấm mã R để đi đến tên bài, vị trí và cách áp dụng. Đọc [sổ tay khái niệm](paper-concepts.md) và [hướng dẫn thực hành](implementation-guide.md) để hiểu cơ chế và ví dụ. Trong bản thảo dùng tác giả–năm. Mã R giữ tương thích với ghi chú cũ. Mỗi claim định lượng cần chốt version, bảng/cột, đơn vị và người đối chiếu trước khi đưa vào manuscript. Vai trò “tùy chọn” chỉ đi vào Method khi thực sự dùng.

| Đang làm phần nào | Trích nguồn | Đưa vào phần nào của bản thảo |
|---|---|---|
| P02b · Đếm token trên câu song song, phân biệt tax và PFR | [R5](#r5), [R21](#r21), [R17](#r17), [R20](#r20) | Introduction, Method dữ liệu/measurement, Appendix tokenizer manifest |
| P01/P02c/P03 · Split, control mù, overlap và 0× | [R3](#r3), [R4](#r4), [R23](#r23), [R13](#r13), [R14](#r14) | Method, split diagnostics, Limitations |
| Exposure, sham và bản dịch | [R12](#r12), [R9](#r9), [R19](#r19) | Related Work và Method, mô tả khác biệt giữa tác vụ và exposure thực tế |
| RQ1 · AUC, adjustment, low-FPR transfer | [R5](#r5), [R21](#r21), [R15](#r15), [R24](#r24), [R16](#r16), [R11](#r11) | Method thống kê. R15 cho xấp xỉ minh hoạ, R11 cho nhánh conformal nếu nhóm chọn |
| RQ2 · Hai detector native và chọn comparator | [R1](#r1), [R2](#r2), [R3](#r3), [R10](#r10), [R18](#r18) | Method/Related Work. R10 tùy chọn likelihood, R18 liên quan tác vụ điền slot |
| RQ3 · Rank, scoring variant và segmentation | [R5](#r5), [R7](#r7), [R6](#r6), [R8](#r8) | Method nêu công thức nhóm chọn. Ba tiêu chí RQ3 và AUC invariance dẫn về protocol của nhóm |
| Định vị novelty và scope | [R22](#r22), [R9](#r9), [R19](#r19), [R4](#r4), [R20](#r20), [R21](#r21) | Introduction và Related Work. So thước đo, đối tượng, nhãn và can thiệp |
| Bổ sung control thực nghiệm và nhật ký exposure | [R25](#r25), [R26](#r26), [R30](#r30), [R31](#r31) | Method P01/P03, độ khó trước LoRA, label theo view, support trước/sau matching |
| Dự toán threshold thấp | [R28](#r28) | Method bounds và Appendix, tách cỡ mẫu cal/test |
| Phạm vi novelty, stage và membership | [R27](#r27), [R29](#r29), [R32](#r32) | Related Work/Limitations. Ba đối tượng riêng là task accuracy, dataset order, tokenizer training |

## A. Detector, integrity và contamination

<a id="r1"></a>
**R1 · Shi et al. (2024), _Detecting Pretraining Data from Large Language Models_, ICLR.** Mở §2, §3, §4.3–4.4. Min-K% lấy log-prob token quan sát, chọn đuôi thấp theo phần trăm vị trí rồi lấy trung bình. Dùng k20 để tái tạo baseline, khóa cách chọn/rounding, so fixed-count trên dev và báo câu quá ngắn. Dẫn bài cho định nghĩa và sensitivity theo lượng văn bản ở WikiMIA. Nhãn WikiMIA dựa vào thời điểm, kiểm chéo với R3. Kết quả khi cắt ngắn văn bản không ước lượng hiệu ứng phân đoạn giữa ngôn ngữ. [Bản v3](https://arxiv.org/html/2310.16789v3)

<a id="r2"></a>
**R2 · Jingyang Zhang et al. (2025), _Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models_, ICLR.** Mở §4.2, Eq. 3–4, Appendix A và MIMIR ở §5. Với mỗi prefix, lấy μ và σ của log-prob theo phân phối toàn vocab. Z-score token thật rồi lấy trung bình đuôi thấp. Cache P01 phải lưu target log-prob và hai moment đủ tái tạo. Đối chiếu numerical stability, mask/prefix và lựa chọn k trước RQ2. Đây là chuẩn hoá theo ngữ cảnh token. Khoảng cách performance trên benchmark không suy ra bền với tokenizer hoặc bảo đảm chạy nhanh với cache thiếu. [Bản v4](https://arxiv.org/html/2404.02936v4)

<a id="r3"></a>
**R3 · Das, Jie Zhang & Tramèr (2025), _Blind Baselines Beat Membership Inference Attacks for Foundation Models_, IEEE Security and Privacy Workshops (DLSP).** Mở §§3–4 và Table 2 của arXiv v2. Classifier mù chỉ dùng text/metadata có thể phân biệt nhãn benchmark từ date, túi từ hoặc n-gram. Thiết lập B0 kiểm split của nhóm bằng family-disjoint training/eval với surface features và count. Cùng test cohort với detector, báo CI và tiến hành đối chiếu nhãn/nguồn nếu B0 có tín hiệu. Kết quả B0 tốt phản ánh nhãn có thông tin phía text trong thiết lập đó. [IEEE proceedings](https://doi.org/10.1109/SPW67851.2025.00016) · [Bản v2](https://arxiv.org/html/2406.16201v2)

<a id="r4"></a>
**R4 · Duan et al. (2024), _Do Membership Inference Attacks Work on Large Language Models?_, COLM.** Mở §3.2 về data ambiguity, §4 về temporal shift. MIMIR so member và held-out trong cùng nguồn và phân tích n-gram overlap/độ lặp. P02c ghi distribution overlap theo language/family trên exact split, dùng đơn vị ký tự nhất quán và sensitivity theo byte hoặc token khi cần. Báo coverage cho câu ngắn, không nhập ngưỡng overlap của tiếng Anh làm cutoff loại mẫu. Dẫn kết quả trong phạm vi Pythia/datasets của bài, và dùng như động cơ kiểm exposure dose. [COLM](https://openreview.net/pdf?id=av0D19pSkU) · [Bản v2](https://arxiv.org/abs/2402.07841v2)

<a id="r9"></a>
**R9 · Yao et al. (2024), _Data Contamination Can Cross Language Barriers_, EMNLP, 17864–17875.** Mở §3 và Tables 1–3. Tiếp xúc bản dịch benchmark có thể đi cùng tăng accuracy khi chấm tiếng Anh. So shared likelihood, prompting, n-gram và probe thay distractor. Dẫn cho rủi ro translation-family spillover và motivation lưu exposure theo language/view. RQ1 của nhóm cần outcome MIA theo nhãn và PFR đã đo; các bảng ở đây đánh giá cấu hình contamination khác và không phải Min-K AUC theo language. [ACL Anthology](https://aclanthology.org/2024.emnlp-main.990/)

<a id="r10"></a>
**R10 · Weichao Zhang et al. (2024), _Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method_, EMNLP, 5263–5274.** Mở Method và PatentMIA. DC-PDD phối xác suất token của model với độ hiếm token từ reference corpus, dùng smoothing, clipping và quy tắc token lặp. Có thể dùng làm comparator likelihood đã hiệu chỉnh theo corpus nếu có reference theo language và budget. Lock corpus/tokenizer and cap. PatentMIA dùng proxy thời gian, phạm vi benchmark khác nhau theo ngôn ngữ. [ACL Anthology](https://aclanthology.org/2024.emnlp-main.300/) · [arXiv v6](https://arxiv.org/abs/2409.14781v6)

<a id="r18"></a>
**R18 · Deng et al. (2024), _Investigating Data Contamination in Modern Benchmarks for Large Language Models_, NAACL, 8706–8719.** Mở phần Testset Slot Guessing. Mask trường trong benchmark và thử đoán lại giá trị thiếu. Dùng cho Related Work hoặc làm comparator hành vi khi nghiên cứu có item/slot rõ. OPUS sentence membership cần đặc tả khác và kết quả đoán slot không tự sinh nhãn exposure. [ACL Anthology](https://aclanthology.org/2024.naacl-long.482/)

<a id="r19"></a>
**R19 · Abbas, Shammaa & Awad (2026), _Obscuring Data Contamination Through Translation: Evidence from Arabic Corpora_, arXiv v2.** Mở §§3–4, Table 6 và Limitations. LoRA tiếp xúc bản dịch Ả Rập ở nhiều mức, đánh giá tiếng Anh và chẩn đoán consistency đa ngôn ngữ. Mốc 0% có ở một số so sánh, Min-K%++ v2 thiếu clean-reference evaluation. Dùng để thiết kế baseline 0× riêng cho mỗi scorer và ledger actual training volume, vì exposure proportion có thể đi cùng lượng dữ liệu khác nhau. Chốt v2 khi trích số, tránh ghép diễn giải v1. [Bản v2](https://arxiv.org/html/2601.14994v2)

<a id="r22"></a>
**R22 · Mishra, Boutet & Magnana (2026), _The Model’s Language Matters: A Comparative Privacy Analysis of LLMs_, Findings of EACL, 1038–1048.** Mở bản xuất bản §§3–4 và Figure 5. EN/ES/FR/IT với encoder/checkpoint theo ngôn ngữ, bộ phân loại shadow/XGBoost cho membership và các thước đo thuộc tính ngôn ngữ. Có ROC/AUC trong bản hội nghị. Bản preprint mô tả accuracy khác version. Đặt ở đầu Related Work để ghi nhận tiền lệ, sau đó nêu nghiên cứu của nhóm đo subword PFR trên câu song song, scoring autoregressive native và exposure theo target version. Việc lấy mẫu corpus có aligned theo item hay không cần căn cứ trên chính nghiên cứu. [Bản xuất bản](https://aclanthology.org/2026.findings-eacl.54/) · [Preprint 2025 để đối chiếu](https://arxiv.org/abs/2510.08813v1)

<a id="r23"></a>
**R23 · Arman Nik Khah (2026), _Detectable Only Where It Is Confounded: What Verified Duplication Counts Say About Membership Evidence in Language Models_, arXiv v2.** Mở §§2–7 và limitations. Tra exact-match counts trong nguồn training, phân tích loss và độ nhạy khi đổi tập đối chứng. Chọn non-member cùng nguồn/register và so overlap có kiểm soát. Kiểm loại hiệu ứng text-edit hay synthetic controls nếu dùng chúng. Dẫn để giải thích vì sao chỉ nhìn AUROC chưa đủ. Counts của pretraining và lượt thấy khi chạy LoRA là hai đại lượng, dùng riêng. [Bản v2](https://arxiv.org/html/2609.10830v2)

## B. Tokenization và bối cảnh đánh giá

<a id="r5"></a>
**R5 · Petrov, La Malfa, Torr & Bibi (2023), _Language Model Tokenizers Introduce Unfairness Between Languages_, NeurIPS.** Mở §§3–4 và Appendix C. Premium trên bản dịch đo chênh chi phí token với cùng ý nghĩa. P02b tái lập một vài dòng cl100k nếu khớp revision, corpus và aggregation. Đối chiếu với code gốc nối dev/devtest và tokenize chuỗi nối. Duy trì sentence-wise PFR của nhóm ở bảng riêng. Bảng cũ chỉ dùng chọn ứng viên, tự tính lại mọi tokenizer của panel. [Code tác giả](https://github.com/AleksandarPetrov/tokenization-fairness/tree/main/compute). PFR là thước đo của nghiên cứu trước, còn quan hệ với AUC và ngưỡng là câu hỏi cần dữ liệu của nhóm. [Bản v2](https://arxiv.org/pdf/2305.15425v2)

<a id="r6"></a>
**R6 · Provilkov, Emelianenko & Voita (2020), _BPE-Dropout: Simple and Effective Subword Regularization_, ACL, 1882–1892.** Mở phần phương pháp và thí nghiệm MT. Bỏ ngẫu nhiên một phần merge tạo phân đoạn khác trong huấn luyện. Related Work/Future Work cho E0. Nếu thử stress test, khóa phân phối sampling và checkpoint, lưu token IDs và forward khác nhau. Giới hạn là hành vi trên các phân đoạn được lấy mẫu; bài không cho upper bound về MIA. [ACL Anthology](https://aclanthology.org/2020.acl-main.170/)

<a id="r7"></a>
**R7 · Cao & Rimell (2021), _You should evaluate your language model on marginal likelihood over tokenisations_, EMNLP, 2104–2114.** Mở §§3–4 và Table 1. Đề xuất estimator cho xác suất chuỗi bề mặt bằng tổng qua các đường phân đoạn khác nhau, khảo sát entropy tokenizer và miền dữ liệu. Giải thích trong Method rằng cộng token log-prob của một encoding chính là điểm canonical của path đã chọn. Chỉ dùng làm tiền lệ khi nghiên cứu marginalization thật sự. Các con số perplexity ở đây không đo membership effect. [ACL Anthology](https://aclanthology.org/2021.emnlp-main.161/)

<a id="r8"></a>
**R8 · Kudo (2018), _Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates_, ACL, 66–75.** Mở phần unigram model và sampling. Lấy mẫu từ nhiều phân đoạn nhằm cải thiện huấn luyện MT. Dẫn cho prior art phân đoạn ngẫu nhiên theo thuật toán. Khác BPE-Dropout ở phân phối phân đoạn, nên E0 tùy tokenizer và không nằm trong lưới chính hiện tại. [ACL Anthology](https://aclanthology.org/P18-1007/)

<a id="r20"></a>
**R20 · Altıntaş et al. (2026), ICML, 2134–2179, _TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior_.** Mở §§3–5, Appendices B/C/G. Các cấu hình chia sẻ nhiều yếu tố huấn luyện và khác tokenizer. Phụ lục C.3 ghi fixed token budget dẫn tới lượng raw bytes khác nhau dù loader cùng thứ tự, và có ablation theo text budget. Dùng để thiết kế ledger bytes/tokens và nhận diện giới hạn khi so các backbone thông thường. Nếu dùng artifact về sau, xác nhận exposure theo stream/checkpoint, license, duplicate và coverage. Kết quả robustness không là kiểm định fertility–AUC. Công thức BPB của nhóm được tự định nghĩa bằng NLL base-2 chia byte bề mặt, nên đối chiếu implementation trước khi gán công thức cho TokSuite. [ICML/PMLR](https://proceedings.mlr.press/v306/altintas26a.html) · [Bản v2](https://arxiv.org/html/2512.20757v2)

<a id="r21"></a>
**R21 · Srivastava (2026), _The Tokenizer Tax: Quantifying and Explaining the Cross-Lingual Cost of Subword Tokenization for Indian Languages_, arXiv v1.** Mở §3, Table 2, §§7–9. Tax của word fertility chuẩn theo EN. Nếu cùng ratio-of-totals và dữ liệu thì `tax=PFR/(W_L/W_EN)`; khi khác tập hoặc aggregation, đo trực tiếp cả hai. Unmerged-byte-rate có thể là diagnostic CPU theo tokenizer phù hợp. Thảo luận Belebele cho lý do kiểm resource confounding, dùng một tokenizer cho fertility và model khác cho accuracy. Partial correlation và kết quả TokSuite không xác lập equivalence hay dự báo dấu của RQ1. [Bản v1](https://arxiv.org/html/2607.24276v1)

## C. Dữ liệu, huấn luyện và thống kê

<a id="r11"></a>
**R11 · Angelopoulos & Bates (2023), _Conformal Prediction: A Gentle Introduction_, Foundations and Trends in Machine Learning.** Đọc phần split conformal và exchangeability. Dùng khi triển khai reference-tail theo một guarantee đã chứng minh. Báo FPR/TPR thực nghiệm theo language từ nhãn và test. Empirical ranks hoặc pooled thresholds có mục tiêu tham chiếu riêng. [Tạp chí](https://doi.org/10.1561/2200000101) · [Preprint tên khác](https://arxiv.org/abs/2107.07511)

<a id="r12"></a>
**R12 · Hu et al. (2022), _LoRA: Low-Rank Adaptation of Large Language Models_, ICLR.** Mở phần phương pháp parameterization. Base weights cố định, dò cập nhật hạng thấp. Dẫn cho adapter setup, ghi rank/scale/target modules/base revision/seed trong manifest. Mức exposure và bằng chứng LoRA ghi nhớ đến đâu lấy từ run của nhóm. [OpenReview](https://openreview.net/forum?id=nZeVKeeFYf9)

<a id="r13"></a>
**R13 · Biao Zhang, Williams, Titov & Sennrich (2020), _Improving Massively Multilingual Neural Machine Translation and Zero-Shot Translation_, ACL, 1628–1639.** Mở phần OPUS-100 dataset. Đặc tả dữ liệu song ngữ ghép với EN. Nêu split/license/language pair đã dùng và đo intersection EN giữa pairs ở P02b. Chiều dài và tỷ lệ short texts lấy từ selected pilot records. [ACL Anthology](https://aclanthology.org/2020.acl-main.148/)

<a id="r14"></a>
**R14 · Yang et al. (2024), _Qwen2.5 Technical Report_, arXiv:2412.15115.** Mở phần architecture/pretraining. Dẫn nguồn cho họ model, kèm model card của exact checkpoint từ manifest. 0× là base trước LoRA của nhóm. Quy mô/dữ liệu nêu trong technical report không xác minh sự xuất hiện của từng câu OPUS. [Báo cáo](https://arxiv.org/abs/2412.15115) · [Model card 1.5B](https://huggingface.co/Qwen/Qwen2.5-1.5B)

<a id="r15"></a>
**R15 · Hanley & McNeil (1982), _The Meaning and Use of the Area Under a Receiver Operating Characteristic (ROC) Curve_, Radiology 143(1), 29–36.** AUC là xác suất xếp đúng một cặp positive–negative với quy ước ties. Bài cung cấp xấp xỉ SE trong thiết lập riêng. Dùng trong Appendix để giải thích sketches cỡ mẫu. Chọn joint resampling theo family của dữ liệu thực cho protocol chính. [PubMed](https://pubmed.ncbi.nlm.nih.gov/7063747/)

<a id="r16"></a>
**R16 · Holm (1979), _A Simple Sequentially Rejective Multiple Test Procedure_, Scandinavian Journal of Statistics 6(2), 65–70.** Điều chỉnh step-down kiểm family-wise error khi p-values đầu vào hợp lệ. Khóa family nào là confirmatory trong C-final, p-values phát sinh theo design. Sensitivity và exploratory gắn nhãn riêng. [JSTOR](https://www.jstor.org/stable/4615733)

<a id="r17"></a>
**R17 · NLLB Team et al. (2022), _No Language Left Behind: Scaling Human-Centered Machine Translation_, arXiv:2207.04672.** Mở phần FLORES-200 evaluation. Dùng aligned IDs và split đã chọn cho PFR reference. Ghi translationese, context và nguồn trong Limitations. Vai trò FLORES trong plan này là corpus đối chiếu token counts. [Bài báo](https://arxiv.org/abs/2207.04672) · [Dataset card](https://huggingface.co/datasets/facebook/flores)

<a id="r24"></a>
**R24 · DeLong, DeLong & Clarke-Pearson (1988), _Comparing the Areas under Two or More Correlated Receiver Operating Characteristic Curves: A Nonparametric Approach_, Biometrics 44(3), 837–845.** Dùng U-statistics để đánh giá covariance AUC khi hai scanner chấm cùng cases. Là tiền lệ cho so sánh ghép cặp before/after hoặc giữa detector. Với translations/cluster và training seeds, resample family chung và báo phạm vi conditional theo design. [PubMed](https://pubmed.ncbi.nlm.nih.gov/3203132/)

## D. Cách viết Introduction và kiểm trích dẫn

1. R5/R21 xác lập thước đo tokenization và động cơ so đa ngôn ngữ. R20 bổ sung bài học kiểm budget, bytes và tokenizers.
2. R9/R19 cho tình huống phơi nhiễm qua bản dịch. R22 là tiền lệ về separability khác nhau giữa các ngôn ngữ.
3. R1/R2 xác định scoring đang khảo sát. R3/R4/R23 giải thích vì sao cần family assignment, text-only diagnostics và verified exposure.
4. Trình bày đóng góp ở mức kết quả thực chứng có thể thu được. Câu mở bài đề xuất: “Chúng tôi kiểm tra mối liên hệ giữa parallel tokenization premium và độ nhạy của detector likelihood trong một thiết kế phơi nhiễm bổ sung có kiểm soát, cùng các kiểm tra độ nhạy theo support và quy tắc chấm điểm.” Từ “gây” đòi hỏi thiết kế bổ sung. Novelty cần kiểm thêm theo chủ đề trước nộp.
5. Với mỗi câu cần dẫn, ghi `claim_id | manuscript section | R-ID | bản/section/table | ngữ cảnh/mẫu | người kiểm | trạng thái`. Với kết luận nhóm, thay R-ID bằng `REPORT path/hash`. Gắn nhãn hypothesis, planned hoặc observed. Các bài trong danh sách ứng viên nội bộ ngoài R1–R24 được thêm khi có vai trò và nguồn cụ thể.

## E. Tài liệu bổ sung và phần đưa vào kế hoạch

<a id="r25"></a>
**R25 · Banaei, Shahzad, Maguire Jr., Chiesa & Kostić (2026), _From Training Exposure to Membership Evidence: A Controlled Study of OLMo 2_, arXiv v1.** Dùng §§III-C–E để mô tả chọn cặp theo difficulty/length và đặt exposure bằng coin flip. §IV Eqs. 1–2 đo score gain trên target/control rồi contrast trong cặp. §V-A–C và §V-F/Fig. 10 phân biệt rank, operating point và việc held-out score cũng dịch. Trích ngắn theo Abstract, “One exposure raises a previously unseen document’s likelihood on average but rarely identifies it.” Trong fertility-mia, dùng idea cho label ledger, một `background-only` control nếu đủ ngân sách và báo từ cùng cohort khi làm ΔAUC. Bài có exact twin mid-training, còn LoRA 0× khác stage và không là twin. Dữ liệu là document-length, kiểm exact có thể bỏ sót paraphrase. Chuyển **quy trình**, không dùng số lượng cặp hay AUROC của họ làm định mức. [Toàn văn v1](https://arxiv.org/html/2610.41732v1)

<a id="r26"></a>
**R26 · Kocyigit, Briakou, Deutsch, Luo, Cherry & Freitag (2025), _Overestimation in LLM Evaluation: A Controlled Large-Scale Study on Data Contamination’s Impact on Machine Translation_, ICML, 31105–31132.** Đọc Abstract và setup source-only/target-only/source+target. Phân biệt exposure một phía với toàn cặp dịch, theo schedule và tần suất. Trích ý: dạng phơi nhiễm ảnh hưởng mức thay đổi BLEU trong thí nghiệm MT. Dùng ngay để mở rộng manifest thành `family × view × run`, thêm đối chứng translation-only riêng. BLEU đo chất lượng dịch, nên không dự báo AUC/FPR. Lưới pretraining 1B/8B là thiết kế riêng. [PMLR](https://proceedings.mlr.press/v267/kocyigit25a.html)

<a id="r27"></a>
**R27 · Kocyigit & Yildirim (2026), _The Impact of Post-training on Data Contamination_, arXiv v1.** §§3–5 phân biệt extended pretraining với SFT/GRPO trên benchmark math/code và các phiên bản đối chiếu. Dùng §5 và §5.1 để buộc Results ghi stage, recipe và endpoint. Trích ý: apparent score inflation thay đổi theo checkpoint/recipe; tác giả giới hạn ở late injection với dose cụ thể. Xếp Related Work/Limitations. Hoãn việc thêm SFT/GRPO vì câu hỏi chính đo likelihood-MIA dưới LoRA. [Toàn văn v1](https://arxiv.org/html/2601.06103v1)

<a id="r28"></a>
**R28 · Xin Tong, Feng & Li (2018), _Neyman-Pearson Classification Algorithms and NP Receiver Operating Characteristics_, Science Advances 4(2), eaao1659.** Mở phần NP umbrella algorithm, Proposition 1–2 và ROC bands. Dùng score order statistics trên null holdout để khống chế xác suất FPR vượt α dưới giả định. Trích ý: phải định cỡ mẫu calibration riêng với test và cân đối violation tolerance. Minh hoạ dùng ở [guide mục 5](implementation-guide.md) cho iid, continuous và ngưỡng max. Weighted pooled/clusters/ties của nghiên cứu cần phân tích riêng. Giữ main là empirical thresholds và achieved rates, chỉ dùng guarantee khi chứng minh đúng trường hợp. [Bản tác giả](https://statistics.arizona.edu/sites/default/files/2023-09/Journal%20Paper%20091823.pdf) · [DOI](https://doi.org/10.1126/sciadv.aao1659)

<a id="r29"></a>
**R29 · Ahuja, Gumma & Sitaram (2024), _Contamination Report for Multilingual Benchmarks_, arXiv v1, EvalEval workshop.** Mở §3, Table 1 và §5. Probe so likelihood của canonical order với permutations, trong giả định exchangeability. Trích ý: audit dataset-level đa ngôn ngữ có thể cho cờ rủi ro ở reference dataset. Dùng để ghi vai trò FLORES chỉ làm PFR reference và phân biệt với ground truth. Model bị flag ở cấp bộ không cho biết sentence nào xuất hiện hay tỷ lệ theo language. Ordering test cũng yêu cầu log-prob, nên không lấp nhánh phi-likelihood của RQ2. [Toàn văn v1](https://arxiv.org/html/2410.16186v1)

<a id="r30"></a>
**R30 · Wang et al. (2026), _Are Fine-Tuned LLM Membership Signals Real? Separating Memorization from Likelihood Shortcuts_, Findings of EMNLP, 32850–32869.** Mở §§4.1, 4.3–4.4 và Appendix C.2–C.4 để xem cách match bằng pre-target features và kiểm độ cân bằng. Trích ngắn theo Abstract: “high attack AUC alone is not reliable evidence of data use”. Nhập hai diagnostics: base-only score control, và matched sensitivity theo độ dài/độ khó trước LoRA. Báo retained PFR variation vì matching có thể làm mất support; sample nhỏ thì coi descriptive. Comparator học DeMIA cần nhãn và likelihood base/target, hoãn tới khi đủ calibration budget. Kết quả English tasks của bài không chuyển thành bảo đảm threshold đa ngôn ngữ. [ACL Anthology](https://aclanthology.org/2026.findings-emnlp.1544/) · [Toàn văn](https://aclanthology.org/2026.findings-emnlp.1544.pdf)

<a id="r31"></a>
**R31 · Meeus, Shilov, Faysse & De Montjoye (2024), _Copyright Traps for Large Language Models_, ICML, 35296–35309.** Mở §§4.3–4.5, §5.2 và Table 2. Thí nghiệm từ scratch với traps, ngẫu nhiên phân bổ treatment và thay length/repetition. Trích ý: số lần xuất hiện chỉ có nghĩa cùng độ dài, representation và regime. Nhập ledger planned/realized exposure và cùng sampling cho treated/heldout. Hoãn tạo synthetic trap cho lưới chính. Độ lặp tính trong một pretraining run cụ thể không suy ra LoRA dose của câu OPUS. [PMLR](https://proceedings.mlr.press/v235/meeus24a.html)

<a id="r32"></a>
**R32 · Meng Tong, Du, Chen, Zhang & Li (2026), _Membership Inference Attacks on Tokenizers of Large Language Models_, arXiv v4.** Mở §§3, 5.1–5.2 và §7. Suy dấu vết dataset đã góp vào huấn luyện BPE tokenizer qua vocabulary/merges với quyền truy cập và reference assumptions. Trích ý: phải nêu đích của membership. Dùng để định vị Introduction. Nhóm giữ tokenizer revision cố định trong từng run và kiểm exposure của model/adapter, endpoint khác tokenizer training. Hoãn đưa các phương pháp đó vào RQ2 vì thay target của nhãn. [Toàn văn v4](https://arxiv.org/html/2510.05699v4)

## F. Cách rà nguồn mới và thứ tự ưu tiên

- Lượt tra ngày 18/11/2026 dùng các truy vấn quanh multilingual contamination, controlled training exposure, fine-tuned likelihood shortcuts, tokenizer-training membership và low-FPR order statistics. Ưu tiên ACL Anthology, PMLR, bài tác giả và arXiv có version. Đọc đúng phần dùng, đối chiếu metadata và giới hạn design trước khi nhập.
- **Đọc trước buổi họp:** R25 §§III-C/IV/V-F, R30 §§4.3–4.4, R5 §§3–4, R1/R2 phần công thức. **Khi chốt threshold:** R28 Proposition 1–2 và rà cohort. **Khi viết Related Work:** R22, R26/R27/R29/R32.
- Lượt tra có phạm vi theo các cụm trên. Ghi novelty dưới dạng câu hỏi về parallel PFR và độ nhạy của likelihood scoring trong added exposure, đối chiếu lại trước nộp nếu có nghiên cứu gần hơn. Không dùng kết quả tìm kiếm để tuyên bố ưu tiên tuyệt đối.

## G. Mở đúng đoạn để rà claim trước khi viết

| Chỗ gốc cần đọc | Ý trích và dùng ngay | Câu phải tự kiểm trước khi viết |
|---|---|---|
| [R1 §3, Eq. 1](#r1) và [R2 §4.2, Eq. 3–4](#r2) | R1 chọn đuôi theo log-prob gốc. R2 chuẩn hoá theo distribution tại prefix rồi mới chọn đuôi. Đưa cả hai vào Method và tài liệu cache | Cùng prefix/retained text chưa, code đã giữ thứ tự normalize → select chưa, có báo actual k không |
| [R3 v2 Table 2](#r3) và [R4 §§3–4](#r4) | Một số benchmark có baseline mù vượt scorer. Khác biệt nguồn và độ chồng lấp có thể ảnh hưởng separation. Dẫn khi giải thích B0 và P02c | Kết quả nói về benchmark nào, text features nào, metric/operating point nào |
| [R5 §§3–4 và code](#r5), [R21 §3/Table 2](#r21) | Ratio token trên nội dung dịch và tax trên tokens/word là hai phép đo. Dùng để ghi rõ tên cột, denom, corpus và aggregation | Paper count nối văn bản hay tách mỗi câu, có lấy EN làm reference đúng version chưa |
| [R7 §§3–4](#r7) | Mỗi đường phân đoạn có xác suất riêng, marginal tổng qua các đường. Dẫn đúng đoạn khi mô tả canonical path và giới hạn span score | Có dùng lại token sequence và cache hay forward lại theo segmentation khác |
| [R19 v2 Table 6 và Limitations](#r19) và [R26 setup](#r26) | Điểm English probe, view được train và lượng text thực tế là ba cột riêng. Dùng để giải thích label dictionary ở Method | Có nêu target view hay đã gộp nhãn family làm exact membership |
| [R20 Appendix C.3, Table 5](#r20) | Cùng thứ tự dữ liệu và token budget có thể khác consumed bytes. Dẫn làm lý do ghi cả tokens/bytes/steps | Kiểm stream theo exact checkpoint trước khi gọi một item là member |
| [R22 Findings Fig. 5](#r22) | Bản xuất bản dùng ROC/AUC cho membership; preprint ghi accuracy. Nêu prior art và tách design trong Related Work | Đã đối chiếu đúng phiên bản, classifier, model và thước đo chưa |
| [R25 §IV Eqs. 1–2 và §V-F](#r25), [R30 Appendix C.2–C.4](#r30) | Trích quy tắc giữ cặp, score gain so control và đo độ khó trước target. Dùng để kiểm P03 và chuẩn bị C-prep | Cổng support đã tính số family đúng chưa, 0× có thật sự tương đương twin hay chỉ là mốc trước LoRA |
| [R28 Proposition 1–2](#r28) | Cỡ mẫu cal cho violation probability là bài toán riêng với test CI. Dùng Appendix để giải thích con số minh hoạ | IID/continuous có đúng hay thiết kế có ties và nhiều view trong family |
