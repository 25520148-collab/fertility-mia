# Phụ lục A · Mỗi bài báo làm gì trong fertility-mia · v2.15

Bản tra cứu v2.15 · 18/11/2026. Phụ lục đọc được theo hai chiều:

- **Đang làm một phần việc** và cần biết dựa vào bài nào → đọc [Mục 1](#1-mỗi-phần-việc-dùng-bài-nào-và-dùng-thế-nào).
- **Đang đọc một bài** và cần biết nó đóng vai gì trong nghiên cứu của nhóm → đọc [Mục 2](#2-từng-bài-làm-gì-trong-hướng-nghiên-cứu-của-nhóm).

Khái niệm của từng bài giải thích ở [sổ tay khái niệm](paper-concepts.md). Ví dụ số ở [hướng dẫn từng bước](implementation-guide.md). Thiết kế hiện hành ở [kế hoạch](../../plan.md). Trong bản thảo dùng tác giả–năm. Mã R giữ nguyên để tương thích với ghi chú cũ.

## 0. Mức đọc và quy tắc trích

Mỗi bài có một nhãn mức đọc. Nhãn nói **ai đã đọc đến đâu**, và từ đó **được trích gì**.

| Nhãn | Nghĩa | Được dùng để | Không được dùng để |
|---|---|---|---|
| `TV` | Đã đọc toàn văn trong dự án | Mô tả phương pháp và kết quả. Trích **con số** sau khi mở lại đúng bảng | Trích số mà không mở lại bảng |
| `PL` | Đã đọc một phần (ghi rõ phần nào) | Như `TV`, nhưng chỉ trong phần đã đọc | Nói về phần chưa đọc |
| `AB` | Đã đối chiếu tiêu đề, tác giả, venue, version và **abstract** | Ý chính và con số **có trong abstract** | Chi tiết trong thân bài, kể cả vị trí section ghi trong phụ lục cũ |
| `CM` | Chưa mở trong dự án; tài liệu chuẩn hoặc phương pháp phổ biến | Định nghĩa và mô tả phương pháp ở mức tổng quát | Bất kỳ con số nào |

**Quy tắc chung.** Một claim định lượng trong bản thảo phải ghi version, bảng hoặc cột, đơn vị và người đối chiếu, theo sổ đối chiếu kết luận (`paper/claim-ledger.md` ở repo public của nhóm). Bài ở mức `AB` hoặc `CM` muốn dùng chi tiết thì phải đọc lên mức `TV`/`PL` trước.

**Nhật ký đối chiếu ngày 18/11/2026.** Claude mở trang arXiv, ACL Anthology hoặc PMLR của **R10, R19, R20, R21, R23, R25, R26, R27, R29, R30, R32** và đối chiếu tiêu đề, tác giả, venue, trang và version. Tất cả khớp, trừ một chỗ:

- **R29** — phụ lục v2.14 ghi venue là *EvalEval workshop*. Trang arXiv **không ghi venue nào** (comments chỉ có "11 pages, 2 tables"). Đã bỏ venue cho tới khi tìm được nguồn.
- **R19** — xác nhận thêm phương pháp: *"The exposure is implemented through LoRA fine-tuning"*, mức phơi nhiễm 0/10/50/100%, bốn model instruct.
- **Hai câu trích nguyên văn** trong phụ lục cũ (R25 và R30) **khớp đúng** abstract.

Các vị trí section của R25–R32 (ví dụ "§IV Eqs. 1–2") do Codex ghi ở v2.14. Claude **chưa** mở thân bài để đối chiếu, nên các vị trí đó giữ ở dạng *"vị trí cần mở"*, chưa phải *"đã kiểm"*.

---

## 1. Mỗi phần việc dùng bài nào, và dùng thế nào

Mỗi mục dưới đây là một phần việc trong [kế hoạch](../../plan.md). Bảng ghi bài dùng, dùng cụ thể vào đâu, và giới hạn khi chuyển kết quả của bài sang đề tài của nhóm. Dòng **"Phần nội bộ"** ghi những gì **không** có bài nào chống đỡ: đó là thiết kế hoặc phép tính của nhóm, và trong bản thảo phải trình bày như vậy.

<a id="t1"></a>
### T1 · P01 · Thu hồi pilot và dựng ledger nhãn phơi nhiễm

Việc: với mỗi lần chạy LoRA, xác định chính xác đoạn nào đã thực sự vào huấn luyện, đoạn nào chỉ có bản dịch đã vào, và đoạn nào là đối chứng sạch.

| Bài | Dùng cụ thể | Giới hạn khi chuyển sang đề tài |
|---|---|---|
| [R25](#r25) | Thiết kế gán phơi nhiễm theo **cặp tài liệu ghép** (có trong abstract): mỗi member có một đối chứng tương đương. Ghi chú v2.14 nói cặp ghép theo độ khó và độ dài và gán bằng tung đồng xu — **chưa mở §III để xác nhận** | Họ chạy lại mid-training của OLMo 2 với một run chính thức làm đối chứng. LoRA của nhóm là giai đoạn khác, và mốc 0× **không** phải một run sinh đôi |
| [R26](#r26) | Lý do ledger phải ghi **view nào** đã vào huấn luyện: chỉ bản EN, chỉ bản L, hay cả hai. Trong thí nghiệm MT của họ, dạng phơi nhiễm đổi mức phồng điểm | Họ đo BLEU, không đo AUROC |
| [R31](#r31) | Tách phơi nhiễm **dự kiến** (planned) với phơi nhiễm **thực tế** (realized). Số lần lặp chỉ có nghĩa khi đi cùng độ dài và chế độ huấn luyện | Họ cài chuỗi bẫy vào pretraining từ đầu; nhóm không tạo bẫy |
| [R19](#r19) | Tiền lệ gần nhất: **LoRA trên bản dịch** ở nhiều mức phơi nhiễm. Ghi lượng dữ liệu thực vào ledger, vì cùng một tỷ lệ phơi nhiễm có thể ứng với lượng văn bản khác nhau | Họ chấm bằng probe tiếng Anh trên benchmark |
| [R9](#r9) | Lý do có nhãn **translation-only** riêng: phơi nhiễm bản dịch có thể làm tăng điểm trên bản gốc | Họ đo accuracy benchmark |
| [R12](#r12) | Định nghĩa LoRA. Manifest ghi rank, scale, target modules, base revision, seed | Mức ghi nhớ thực tế phải đo từ run của nhóm |
| [R14](#r14) | Ghi đúng checkpoint của model pilot | Technical report không cho biết câu OPUS nào đã có trong pretraining |

**Phần nội bộ:** năm nhãn `direct` / `translation-only` / `partial` / `unknown` / `verified family-unexposed` và quy tắc chiều thận trọng (bản ghi chưa xác minh **không bao giờ** thành đối chứng) là thiết kế của nhóm, ghi ở [protocol PFR và split](pfr-and-splits.md).

<a id="t2"></a>
### T2 · P02b · Đo PFR

Việc: với mỗi cặp câu song song, đếm số token của bản L chia cho bản EN bằng cùng tokenizer.

| Bài | Dùng cụ thể | Giới hạn |
|---|---|---|
| [R5](#r5) | **Định nghĩa PFR** — chính là *premium* của bài này. Tái lập vài dòng của họ để kiểm pipeline đếm, so với [code tác giả](https://github.com/AleksandarPetrov/tokenization-fairness/tree/main/compute) | Code của họ nối dev+devtest rồi tokenize cả chuỗi; nhóm đếm **theo từng cặp**. Hai cách phải ở hai bảng riêng |
| [R17](#r17) | FLORES-200 làm **corpus tham chiếu**: cùng ID câu ở mọi ngôn ngữ | Văn bản dịch (translationese) có thể khác văn bản tự nhiên |
| [R13](#r13) | OPUS-100 là corpus của pilot. Các cặp EN–L **có thể** không cùng tập câu EN, nên phải đo phần giao | Độ dài và tỷ lệ câu ngắn lấy từ dữ liệu pilot, không từ bài |
| [R21](#r21) | Phân biệt **tax** (token/từ khoảng trắng, chuẩn theo EN) với **PFR**. Chỉ đo tax ở chữ viết có khoảng trắng | Khác tập câu hoặc khác cách gộp thì không đổi được tax sang PFR |
| [R20](#r20) | Lý do ghi **cả tokens lẫn bytes**: hai tokenizer khác nhau cắt cùng một văn bản thành số token khác nhau, nên cùng ngân sách token ứng với lượng byte khác nhau. Lý do này là số học; theo ghi chú v2.14, R20 Appendix C.3 ghi nhận đúng hiện tượng đó — **chưa mở** | Kết quả robustness của họ không phải kiểm định PFR–AUROC |

<a id="t3"></a>
### T3 · P02c · Split, chồng lấp, baseline mù và mốc 0×

Việc: trước khi tin bất kỳ AUROC nào, kiểm rằng member và non-member không khác nhau vì lý do khác ngoài phơi nhiễm.

| Bài | Dùng cụ thể | Giới hạn |
|---|---|---|
| [R3](#r3) | **B0**: một classifier chỉ nhìn văn bản, không nhìn model. Nếu B0 đoán được nhãn thì split có vấn đề | B0 là phép kiểm split, **không** phải detector phơi nhiễm |
| [R4](#r4) | Đo chồng lấp n-gram giữa member và non-member theo từng ngôn ngữ và family. Động cơ dùng phơi nhiễm có kiểm soát thay vì nhãn tự nhiên | **Không** nhập ngưỡng overlap của họ làm luật loại mẫu |
| [R23](#r23) | Lý do đối chứng phải **cùng nguồn** và **đã xác minh**: đổi tập đối chứng có thể đổi AUROC | Đếm bản sao trong pretraining khác số lượt thấy khi chạy LoRA |
| [R30](#r30) | **Base-only control**: chấm cùng mẫu bằng model gốc trước LoRA. Nếu model gốc đã tách được hai lớp thì AUROC sau LoRA chưa chứng minh ghi nhớ | Họ làm trên tác vụ tiếng Anh |
| [R25](#r25) | Abstract nói cần một **đối chứng tương đương** để MIA hoạt động tốt. Ghi chú v2.14 (§V-F, Fig. 10) thêm rằng điểm của đối chứng cũng dịch sau huấn luyện — **chưa mở để xác nhận** | Xem giới hạn ở T1 |

**Phần nội bộ:** dải split-integrity cho AUROC ở 0× (độ lệch khỏi 0,5 quá `z·SE(n)` thì gắn cờ) là phép tính của nhóm.

<a id="t4"></a>
### T4 · P03 · Chấm điểm native

Việc: tái tạo đúng hai detector theo định nghĩa gốc, từ cùng một cache log-prob.

| Bài | Dùng cụ thể | Giới hạn |
|---|---|---|
| [R1](#r1) | **Min-K%**: trung bình log-prob của k% token xác suất thấp nhất, `k = 20%`. Khóa cách làm tròn k và cách xử lý câu ngắn | Kết quả cắt ngắn văn bản trong bài đo **lượng nội dung**, không đo **cách phân đoạn** |
| [R2](#r2) | **Min-K%++**: chuẩn hoá log-prob từng token bằng μ, σ của phân phối toàn vocab **tại đúng prefix**, rồi mới chọn đuôi thấp. Cache phải lưu μ và σ | Thắng trên benchmark không chứng minh bền với tokenizer |
| [R7](#r7) | Gọi đúng tên thứ đang chấm: điểm của **một đường phân đoạn** (canonical), không phải likelihood của chuỗi bề mặt | Các con số perplexity trong bài không đo membership |
| [R14](#r14) | Ghi đúng revision của model và tokenizer | — |

<a id="t5"></a>
### T5 · RQ1 · Kết quả chính: AUROC sau LoRA

Việc: đo khả năng detector xếp **đoạn thực sự được huấn luyện** cao hơn **đoạn đối chứng đã xác minh**, rồi xem nó liên hệ thế nào với PFR trên các ngôn ngữ đã khảo sát.

| Bài | Dùng cụ thể | Giới hạn |
|---|---|---|
| [R15](#r15) | **Định nghĩa AUROC**: xác suất một positive có điểm cao hơn một negative, cộng nửa xác suất hoà | Công thức SE của bài dựa trên giả định riêng; CI chính dùng bootstrap theo family |
| [R1](#r1) | **Detector primary** đề xuất: Min-K% native `k = 20%`, chốt trước khi xem kết quả | — |
| [R5](#r5) | PFR là trục x | Quan hệ PFR–AUROC là câu hỏi của nhóm, bài không trả lời |

**Phần nội bộ:** nhánh **Anh–Trung** (hai điểm cấp ngôn ngữ chỉ cho phép mô tả, không có độ dốc kiểm định được) là quyết định thiết kế của nhóm.

<a id="t6"></a>
### T6 · RQ1 · ΔAUROC và mốc 0× (bổ trợ)

| Bài | Dùng cụ thể | Giới hạn |
|---|---|---|
| [R24](#r24) | Hai AUROC tính trên **cùng các case** thì tương quan với nhau, nên hiệu của chúng phải tính phương sai có ghép cặp | Công thức của bài giả định case độc lập; family lồng nhau thì dùng bootstrap theo family |
| [R25](#r25) | Lý do so với **đối chứng tương đương** trên cùng mẫu và cùng nhãn (abstract). Chi tiết điểm đối chứng dịch sau huấn luyện ở §V-F **chưa mở** | 0× không phải run sinh đôi |
| [R19](#r19) | Tiền lệ đặt **mốc 0% riêng cho mỗi scorer** | — |

<a id="t7"></a>
### T7 · RQ1 và RQ2 · Phân tích trong ngôn ngữ theo bin `pfr_i`

**Không có bài nào chống đỡ trực tiếp — đây là phân tích của nhóm.** Nó dựa trên một tính chất của định nghĩa: `pfr_i` được đo **theo từng cặp câu**, nên trong cùng một ngôn ngữ PFR vẫn khác nhau giữa các câu. Nếu membership được gán ngẫu nhiên theo family thì member và non-member trong cùng một bin so được với nhau. **Điều kiện:** phép so chỉ hợp lệ khi membership **được gán ngẫu nhiên theo family**. Điều này đúng với pilot thiết kế mới từ đầu; với pilot cũ, cách gán chưa biết, nên phải kiểm trong P01 trước khi dùng phân tích này.

| Bài | Dùng làm gì |
|---|---|
| [R5](#r5) | Khái niệm tỷ số token trên bản dịch song song. Lưu ý R5 gộp cả corpus, còn nhóm đo **theo từng cặp** |
| [R1](#r1), [R4](#r4) | Lý do phải báo phân phối độ dài trong mỗi bin: điểm của detector nhạy với lượng văn bản được chấm |

<a id="t8"></a>
### T8 · RQ1 · Điều chỉnh theo độ khó trước LoRA

| Bài | Dùng cụ thể | Giới hạn |
|---|---|---|
| [R30](#r30) | **Matched sensitivity**: ghép member và non-member theo đặc trưng đo **trước** LoRA (độ dài, NLL của model gốc), báo độ cân bằng trước và sau ghép | Ghép cặp có thể làm mất support và thu hẹp dải PFR, nên báo cùng cohort đầy đủ |
| [R21](#r21) | Lý do phải nghĩ tới nhiễu do **lượng tài nguyên** của ngôn ngữ | Hồi quy riêng phần của họ không dự báo dấu của RQ1 |
| [R20](#r20) | Một biến đo bằng byte thay vì token tránh đưa số token vào mẫu số | Công thức bits/byte của nhóm phải tự định nghĩa và đối chiếu implementation |

<a id="t9"></a>
### T9 · RQ1 · Chuyển ngưỡng giữa ngôn ngữ (đánh giá riêng)

| Bài | Dùng cụ thể | Giới hạn |
|---|---|---|
| [R28](#r28) | Chọn ngưỡng từ order statistic của điểm đối chứng để giới hạn xác suất FPR vượt α. Giải thích vì sao **cỡ mẫu calibration** là bài toán riêng với CI của test | Bảo đảm cần iid và điểm liên tục; thiết kế có ties, trọng số và family thì phải phân tích riêng |
| [R11](#r11) | Chỉ dùng nếu nhóm muốn một **bảo đảm có chứng minh** cho FPR | Ngưỡng thực nghiệm và tỷ lệ đạt được là phần chính |

<a id="t10"></a>
### T10 · RQ2 · Độ dốc theo PFR của chênh AUROC giữa hai detector

| Bài | Dùng cụ thể | Giới hạn |
|---|---|---|
| [R1](#r1), [R2](#r2) | Hai detector được so. Câu hỏi: Min-K%++ chuẩn hoá theo ngữ cảnh, vậy nó có **ít nhạy theo PFR** hơn Min-K% không | Bài gốc Min-K%++ không thử theo PFR |
| [R24](#r24) | Hai detector chấm **cùng các case**, nên chênh của chúng dùng phương sai ghép cặp | Xem T6 |
| [R16](#r16) | Nếu nhóm có nhiều phép kiểm confirmatory, khóa họ phép kiểm và dùng Holm | p-value đầu vào phải hợp lệ |

**Phần nội bộ:** ca kiểm *A hơn B đúng 0,05 ở mọi PFR thì độ dốc phải bằng 0* là phép kiểm pipeline của nhóm.

<a id="t11"></a>
### T11 · RQ2 · Vì sao comparator phi-likelihood là phần mở rộng

Mỗi bài dưới đây là một ứng viên đã xét, kèm lý do **chưa** dùng được làm detector phơi nhiễm không dựa likelihood cho đề tài này.

| Bài | Ứng viên | Lý do chưa dùng |
|---|---|---|
| [R3](#r3) | Baseline mù B0 | Không nhìn model nên không đo phơi nhiễm; giữ vai trò kiểm split |
| [R10](#r10) | DC-PDD | Vẫn dùng xác suất token của model, nên vẫn là likelihood |
| [R18](#r18) | TS-Guessing | Cần item có trường bị che; câu OPUS không có |
| [R29](#r29) | Probe hộp đen ở cấp bộ dữ liệu | Kết luận ở cấp **bộ dữ liệu**, không ở cấp câu (có trong abstract). Ghi chú v2.14 nói probe so thứ tự gốc với thứ tự xáo trộn bằng log-prob, nên vẫn dựa likelihood — **chưa mở §3 để xác nhận** |
| [R32](#r32) | MIA trên tokenizer | Đích membership khác: dữ liệu huấn luyện tokenizer, không phải adapter |

<a id="t12"></a>
### T12 · RQ3 · Phép chấm đổi được thứ hạng

| Bài | Dùng cụ thể | Giới hạn |
|---|---|---|
| [R7](#r7) | Đổi quy tắc chấm là **một can thiệp khác** với đổi cách phân đoạn: cùng một cache, cùng một đường phân đoạn | Chỉ dẫn R7 như tiền lệ marginal likelihood nếu nhóm thực sự marginalize |
| [R5](#r5) | PFR là đầu vào của công thức. Nếu dùng PFR cặp thì cần bản EN lúc chấm, nên claim giới hạn ở **paired audit** | — |
| [R6](#r6), [R8](#r8) | Future Work: cho model thấy nhiều cách phân đoạn khác nhau | Đổi token IDs nghĩa là phải chạy lại model, ngoài lưới chính |

**Phần nội bộ:** ví dụ tính tay `s = (10, 8)`, `T = (20, 10)` → `(0,50 ; 0,80)`; [fixture F3](fixtures.py) (nhân hằng giữ nguyên AUROC, 0,6667 → 0,6667); và ba tiêu chí `ΔD`, `Δmean`, `Δlow`.

<a id="t13"></a>
### T13 · Độ chính xác và đa phép thử

| Bài | Dùng cụ thể |
|---|---|
| [R15](#r15) | Định nghĩa AUROC và xấp xỉ SE cho phép tính cỡ mẫu minh hoạ |
| [R24](#r24) | Logic covariance khi so hai AUROC trên cùng case |
| [R16](#r16) | Kiểm soát sai số theo họ phép thử |
| [R28](#r28) | Cỡ mẫu calibration cho ngưỡng FPR thấp |

<a id="t14"></a>
### T14 · Viết Introduction và Related Work

Xem [Mục 3](#3-viết-introduction-và-related-work) cho thứ tự và câu delta.

| Dòng Related Work | Bài |
|---|---|
| Ngôn ngữ và rò rỉ thông tin — **tiền lệ gần nhất** | [R22](#r22) |
| Tokenizer và chi phí giữa ngôn ngữ | [R5](#r5), [R21](#r21), [R20](#r20) |
| Contamination qua bản dịch và theo giai đoạn huấn luyện | [R9](#r9), [R19](#r19), [R26](#r26), [R27](#r27), [R29](#r29) |
| Phê phán đánh giá MIA | [R3](#r3), [R4](#r4), [R23](#r23), [R30](#r30), [R25](#r25) |
| Detector likelihood | [R1](#r1), [R2](#r2), [R10](#r10) |
| Đích của membership | [R32](#r32) |

<a id="t15"></a>
### T15 · Limitations và Future Work

| Bài | Giới hạn hoặc hướng tiếp |
|---|---|
| [R27](#r27) | Kết luận phụ thuộc **giai đoạn huấn luyện**; nhóm chỉ đo LoRA |
| [R25](#r25) | Mốc 0× là trước LoRA, không phải run sinh đôi |
| [R23](#r23) | Phơi nhiễm trong pretraining không quan sát được |
| [R20](#r20) | **Future Work:** TokSuite có 14 model **chỉ khác tokenizer**. Đây là loại can thiệp mà [kế hoạch](../../plan.md) nói là cần để có claim riêng về tokenizer. Muốn dùng phải kiểm license, kích thước model so với T4, và xác minh phơi nhiễm |
| [R6](#r6), [R8](#r8) | Future Work: stress test với nhiều cách phân đoạn |

---

## 2. Từng bài làm gì trong hướng nghiên cứu của nhóm

Mỗi thẻ có bốn dòng: **bài làm gì** · **nhóm dùng vào việc nào** · **không dùng để nói gì** · **mở ở đâu**. Mã `T` dẫn về [Mục 1](#1-mỗi-phần-việc-dùng-bài-nào-và-dùng-thế-nào).

### A. Detector, kiểm tập đánh giá và contamination

<a id="r1"></a>
#### R1 · Shi et al. (2024) · Min-K% · `TV`

_Detecting Pretraining Data from Large Language Models_, ICLR 2024 · [arXiv v3](https://arxiv.org/html/2310.16789v3)

- **Bài làm gì.** Đề xuất Min-K%: chấm một đoạn bằng trung bình log-prob của k% token có xác suất thấp nhất. Giới thiệu benchmark WikiMIA, nhãn dựa trên thời điểm văn bản xuất hiện.
- **Nhóm dùng vào.** Detector primary của RQ1 và một trong hai detector của RQ2 ([T4](#t4), [T5](#t5), [T10](#t10)). Khóa `k = 20%`, cách làm tròn và câu ngắn. Lý do báo phân phối độ dài trong mỗi bin `pfr_i` ([T7](#t7)); Related Work ([T14](#t14)).
- **Không dùng để nói.** Thí nghiệm cắt ngắn văn bản đổi **lượng nội dung**, không đổi **cách phân đoạn**, nên không ước lượng được hiệu ứng PFR. Nhãn WikiMIA theo thời gian có thể kéo theo lệch phân phối (xem R3).
- **Mở ở đâu.** §3 Eq. 1; §4.3–4.4.

<a id="r2"></a>
#### R2 · Jingyang Zhang et al. (2025) · Min-K%++ · `TV`

_Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models_, ICLR 2025 · [arXiv v4](https://arxiv.org/html/2404.02936v4)

- **Bài làm gì.** Chuẩn hoá log-prob từng token bằng trung bình μ và độ lệch σ của phân phối toàn vocab tại prefix đó, rồi mới lấy đuôi thấp.
- **Nhóm dùng vào.** Detector thứ hai của RQ2 ([T4](#t4), [T10](#t10)). Vì nó chuẩn hoá theo ngữ cảnh, câu hỏi của RQ2 là nó có ít nhạy theo PFR hơn Min-K% không. Cache phải lưu μ và σ. Related Work ([T14](#t14)).
- **Không dùng để nói.** Thắng trên benchmark không chứng minh bền với tokenizer, cũng không chứng minh chạy nhanh khi cache thiếu moment.
- **Mở ở đâu.** §4.2 Eq. 3–4; Appendix A; MIMIR ở §5.

<a id="r3"></a>
#### R3 · Das, Jie Zhang & Tramèr (2025) · Blind Baselines · `TV`

_Blind Baselines Beat Membership Inference Attacks for Foundation Models_, IEEE Security and Privacy Workshops (DLSP) 2025 · [IEEE](https://doi.org/10.1109/SPW67851.2025.00016) · [arXiv v2](https://arxiv.org/html/2406.16201v2)

- **Bài làm gì.** Cho thấy một classifier **không nhìn model**, chỉ dùng văn bản hoặc metadata, vẫn đoán đúng nhãn member/non-member trên nhiều benchmark MIA, vì hai lớp lệch phân phối.
- **Nhóm dùng vào.** Phép kiểm B0 trong P02c, và vai trò kiểm lệch dữ liệu trong RQ2 ([T3](#t3), [T11](#t11)); phê phán MIA trong Related Work ([T14](#t14)).
- **Không dùng để nói.** B0 không đo phơi nhiễm; B0 tốt chỉ nói nhãn có thông tin phía văn bản trong thiết lập đó. Venue là **workshop**.
- **Mở ở đâu.** §§3–4; Table 2 của arXiv v2.

<a id="r4"></a>
#### R4 · Duan et al. (2024) · MIMIR · `TV`

_Do Membership Inference Attacks Work on Large Language Models?_, COLM 2024 · [OpenReview](https://openreview.net/pdf?id=av0D19pSkU) · [arXiv v2](https://arxiv.org/abs/2402.07841v2)

- **Bài làm gì.** Cho thấy MIA trên dữ liệu pretraining gần như ngẫu nhiên khi member và non-member cùng phân phối. Chồng lấp n-gram và lệch thời gian làm phồng kết quả.
- **Nhóm dùng vào.** Đo chồng lấp theo ngôn ngữ và family ([T3](#t3)); lý do dùng phơi nhiễm có kiểm soát thay vì nhãn tự nhiên; lý do báo độ dài trong mỗi bin ([T7](#t7)); phê phán MIA trong Related Work ([T14](#t14)).
- **Không dùng để nói.** Không nhập ngưỡng overlap của họ làm luật loại mẫu. Kết quả giới hạn ở Pythia và các bộ dữ liệu của bài.
- **Mở ở đâu.** §3.2 data ambiguity; §4 temporal shift.

<a id="r9"></a>
#### R9 · Yao et al. (2024) · Contamination vượt rào ngôn ngữ · `TV`

_Data Contamination Can Cross Language Barriers_, EMNLP 2024, 17864–17875 · [ACL Anthology](https://aclanthology.org/2024.emnlp-main.990/)

- **Bài làm gì.** Cho thấy cố ý đưa **bản dịch** của benchmark vào huấn luyện làm tăng điểm khi chấm bản tiếng Anh, trong khi các phép dò contamination thông thường khó phát hiện.
- **Nhóm dùng vào.** Lý do có nhãn translation-only riêng và chia theo family ([T1](#t1)); Related Work ([T14](#t14)).
- **Không dùng để nói.** Họ đo accuracy benchmark, không đo AUROC của Min-K% theo ngôn ngữ.
- **Mở ở đâu.** §3; Tables 1–3.

<a id="r10"></a>
#### R10 · Weichao Zhang et al. (2024) · DC-PDD · `TV`

_Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method_, EMNLP 2024, 5263–5274 · [ACL Anthology](https://aclanthology.org/2024.emnlp-main.300/) · [arXiv v6](https://arxiv.org/abs/2409.14781v6)

- **Bài làm gì.** Hiệu chỉnh xác suất token của model bằng tần suất token trong một corpus tham chiếu, dùng cross-entropy giữa hai phân phối làm điểm.
- **Nhóm dùng vào.** Ứng viên comparator **likelihood đã hiệu chỉnh** cho phần mở rộng; và lý do nó **không** thoả điều kiện "không dựa likelihood" ([T11](#t11), [T14](#t14)).
- **Không dùng để nói.** Benchmark PatentMIA dùng proxy thời gian; cần corpus tham chiếu riêng cho từng ngôn ngữ.
- **Mở ở đâu.** Phần Method; PatentMIA.

<a id="r18"></a>
#### R18 · Deng et al. (2024) · TS-Guessing · `CM`

_Investigating Data Contamination in Modern Benchmarks for Large Language Models_, NAACL 2024, 8706–8719 · [ACL Anthology](https://aclanthology.org/2024.naacl-long.482/)

- **Bài làm gì.** Che một trường trong item benchmark (ví dụ một đáp án sai) và xem model có đoán lại đúng giá trị không.
- **Nhóm dùng vào.** Related Work; và lý do không dùng làm comparator ([T11](#t11)).
- **Không dùng để nói.** Câu OPUS không có trường để che; đoán đúng một trường không tự tạo ra nhãn phơi nhiễm.
- **Mở ở đâu.** Phần Testset Slot Guessing.

<a id="r19"></a>
#### R19 · Abbas, Shammaa & Awad (2026) · Contamination qua tiếng Ả Rập · `TV`

_Obscuring Data Contamination Through Translation: Evidence from Arabic Corpora_, arXiv v2 (8/10/2026) · [arXiv v2](https://arxiv.org/html/2601.14994v2)

- **Bài làm gì.** Fine-tune bằng **LoRA** bốn model instruct (Llama-3.2-1B, Mistral-7B, Gemma-3-1B, Qwen3-1.7B) trên bản dịch tiếng Ả Rập của MMLU và XQuAD ở mức 0/10/50/100%, rồi kiểm bằng probe tiếng Anh (TS-Guessing, Min-K%++), accuracy tiếng Anh và một chẩn đoán nhất quán giữa ngôn ngữ.
- **Nhóm dùng vào.** **Tiền lệ gần nhất** cho phơi nhiễm LoRA có kiểm soát qua bản dịch ([T1](#t1)); mốc 0% cho mỗi scorer ([T6](#t6)); Related Work ([T14](#t14)).
- **Không dùng để nói.** Họ đo trên benchmark bằng probe tiếng Anh, không đo AUROC theo PFR. Trích số thì dùng v2, không ghép với diễn giải của v1.
- **Mở ở đâu.** §§3–4; Table 6; Limitations.

<a id="r22"></a>
#### R22 · Mishra, Boutet & Magnana (2026) · Ngôn ngữ và privacy · `TV`

_The Model's Language Matters: A Comparative Privacy Analysis of LLMs_, Findings of EACL 2026, 1038–1048 · [ACL Anthology](https://aclanthology.org/2026.findings-eacl.54/) · [preprint 2025](https://arxiv.org/abs/2510.08813v1)

- **Bài làm gì.** So mức rò rỉ privacy giữa EN, ES, FR, IT bằng shadow model và classifier XGBoost, gắn với các thuộc tính ngôn ngữ cấp ký tự và cú pháp.
- **Nhóm dùng vào.** **Tiền lệ gần nhất** cho câu hỏi "ngôn ngữ có ảnh hưởng rò rỉ không". Đặt **sớm** trong Related Work ([T14](#t14)).
- **Không dùng để nói.** Họ không đo PFR subword trên câu song song, không dùng detector likelihood autoregressive, không có nhãn phơi nhiễm theo lần chạy. Bản hội nghị dùng ROC/AUC, bản preprint ghi accuracy — trích đúng bản.
- **Mở ở đâu.** §§3–4; Figure 5 của bản Findings.

<a id="r23"></a>
#### R23 · Arman Nik Khah (2026) · Số bản trùng đã xác minh · `TV`

_Detectable Only Where It Is Confounded: What Verified Duplication Counts Say About Membership Evidence in Language Models_, arXiv v2 (29/9/2026) · [arXiv v2](https://arxiv.org/html/2609.10830v2)

- **Bài làm gì.** Dùng số lần lặp đã xác minh trong corpus của OLMo-2 và Pythia. Ở mức lặp thông thường tín hiệu membership rất yếu; tín hiệu mạnh trên khoảng một nghìn bản trùng lại trùng với các câu nổi tiếng. Tín hiệu biểu kiến có thể đến từ cách chọn tập đối chứng.
- **Nhóm dùng vào.** Lý do đối chứng phải cùng nguồn và đã xác minh ([T3](#t3)); phê phán MIA ([T14](#t14)); Limitations ([T15](#t15)).
- **Không dùng để nói.** Đếm bản sao trong pretraining và số lượt thấy khi chạy LoRA là **hai đại lượng khác nhau**.
- **Mở ở đâu.** §§2–7; Limitations.

### B. Tokenization và phân đoạn

<a id="r5"></a>
#### R5 · Petrov, La Malfa, Torr & Bibi (2023) · Tokenizer và bất công giữa ngôn ngữ · `TV`

_Language Model Tokenizers Introduce Unfairness Between Languages_, NeurIPS 2023 · [arXiv v2](https://arxiv.org/pdf/2305.15425v2) · [code tác giả](https://github.com/AleksandarPetrov/tokenization-fairness/tree/main/compute)

- **Bài làm gì.** Định nghĩa **premium**: số token để biểu diễn cùng một nội dung đã dịch, chia cho số token của bản tham chiếu. Đo premium cho nhiều tokenizer và ngôn ngữ trên FLORES.
- **Nhóm dùng vào.** **Định nghĩa PFR** ([T2](#t2)); trục x của RQ1 ([T5](#t5)); khái niệm cho phân tích trong ngôn ngữ, với lưu ý R5 gộp cả corpus còn nhóm đo theo cặp ([T7](#t7)); đầu vào công thức RQ3 ([T12](#t12)); Related Work ([T14](#t14)).
- **Không dùng để nói.** Quan hệ giữa PFR và AUROC là câu hỏi của nhóm. Bảng của bài chỉ dùng để chọn ứng viên panel; mọi tokenizer của panel phải tự đo lại.
- **Mở ở đâu.** §§3–4; Appendix C; code gốc.

<a id="r6"></a>
#### R6 · Provilkov, Emelianenko & Voita (2020) · BPE-Dropout · `CM`

_BPE-Dropout: Simple and Effective Subword Regularization_, ACL 2020, 1882–1892 · [ACL Anthology](https://aclanthology.org/2020.acl-main.170/)

- **Bài làm gì.** Bỏ ngẫu nhiên một phần phép merge của BPE trong huấn luyện để model thấy nhiều cách phân đoạn của cùng một văn bản.
- **Nhóm dùng vào.** Future Work: stress test với nhiều cách phân đoạn ([T12](#t12), [T15](#t15)).
- **Không dùng để nói.** Bài không cho giới hạn nào về MIA.
- **Mở ở đâu.** Phần phương pháp; thí nghiệm MT.

<a id="r7"></a>
#### R7 · Cao & Rimell (2021) · Marginal likelihood qua các cách phân đoạn · `TV`

_You should evaluate your language model on marginal likelihood over tokenisations_, EMNLP 2021, 2104–2114 · [ACL Anthology](https://aclanthology.org/2021.emnlp-main.161/)

- **Bài làm gì.** Chỉ ra xác suất của một chuỗi bề mặt là **tổng qua mọi cách phân đoạn**; LM thường chỉ chấm một đường (canonical). Đề xuất estimator cho tổng đó.
- **Nhóm dùng vào.** Gọi đúng tên thứ đang chấm ([T4](#t4)); lý do RQ3 là **đổi quy tắc chấm** chứ không phải marginal likelihood ([T12](#t12)).
- **Không dùng để nói.** Các con số perplexity của bài không đo hiệu ứng membership.
- **Mở ở đâu.** §§3–4; Table 1.

<a id="r8"></a>
#### R8 · Kudo (2018) · Subword regularization · `CM`

_Subword Regularization: Improving Neural Network Translation Models with Multiple Subword Candidates_, ACL 2018, 66–75 · [ACL Anthology](https://aclanthology.org/P18-1007/)

- **Bài làm gì.** Lấy mẫu nhiều cách phân đoạn từ một mô hình unigram để cải thiện huấn luyện MT.
- **Nhóm dùng vào.** Future Work, cạnh R6 ([T12](#t12), [T15](#t15)).
- **Không dùng để nói.** Phân phối phân đoạn khác BPE-Dropout, nên kết quả phụ thuộc tokenizer.
- **Mở ở đâu.** Phần unigram model và sampling.

<a id="r20"></a>
#### R20 · Altıntaş et al. (2026) · TokSuite · `PL`

_TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior_, ICML 2026, PMLR 306: 2134–2179 · [PMLR](https://proceedings.mlr.press/v306/altintas26a.html) · [arXiv v2](https://arxiv.org/html/2512.20757v2)

- **Bài làm gì.** Phát hành **14 model chỉ khác nhau ở tokenizer**, cùng một benchmark robustness đa ngôn ngữ gồm tiếng Anh, **tiếng Trung**, Farsi, Ý và Thổ Nhĩ Kỳ (cả hai ý có trong abstract). Theo ghi chú v2.14, Appendix C.3 ghi rằng cùng ngân sách token có thể tiêu thụ lượng byte khác nhau — phần này **chưa mở**.
- **Nhóm dùng vào.** Lý do ledger ghi cả tokens lẫn bytes ([T2](#t2)); biến đo bằng byte cho điều chỉnh ([T8](#t8)); Related Work ([T14](#t14)); **Future Work**: bộ model chỉ khác tokenizer là loại can thiệp cần cho một claim riêng về tokenizer ([T15](#t15)).
- **Không dùng để nói.** Kết quả robustness của họ không phải kiểm định PFR–AUROC. Muốn dùng model của họ phải kiểm license, kích thước so với T4 và xác minh phơi nhiễm.
- **Mở ở đâu.** Đã đọc phần đầu, Table 4 và Limitations; venue và abstract đối chiếu 18/11. Chưa đọc §§3–5 đầy đủ và Appendices B/C/G.

<a id="r21"></a>
#### R21 · Srivastava (2026) · Tokenizer Tax · `TV`

_The Tokenizer Tax: Quantifying and Explaining the Cross-Lingual Cost of Subword Tokenization for Indian Languages_, arXiv v1 (27/7/2026) · [arXiv v1](https://arxiv.org/html/2607.24276v1)

- **Bài làm gì.** Đo trên FLORES-200 với sáu tokenizer xem ngôn ngữ Ấn Độ cần nhiều token hơn tiếng Anh bao nhiêu; phần lớn chênh lệch đến từ các phép merge byte thất bại.
- **Nhóm dùng vào.** Phân biệt **tax** với **PFR** ([T2](#t2)); lý do nghĩ tới nhiễu do tài nguyên ([T8](#t8)); Related Work ([T14](#t14)).
- **Không dùng để nói.** Tax là token/từ khoảng trắng chuẩn theo EN, khác PFR. Hồi quy riêng phần của bài không dự báo dấu của RQ1.
- **Mở ở đâu.** §3; Table 2; §§7–9.

### C. Dữ liệu, huấn luyện và model

<a id="r12"></a>
#### R12 · Hu et al. (2022) · LoRA · `CM`

_LoRA: Low-Rank Adaptation of Large Language Models_, ICLR 2022 · [OpenReview](https://openreview.net/forum?id=nZeVKeeFYf9)

- **Bài làm gì.** Giữ nguyên trọng số gốc, chỉ học một cập nhật hạng thấp.
- **Nhóm dùng vào.** Phương pháp đưa phơi nhiễm vào model ([T1](#t1)).
- **Không dùng để nói.** Mức ghi nhớ của LoRA trong đề tài phải đo từ run của nhóm.
- **Mở ở đâu.** Phần phương pháp.

<a id="r13"></a>
#### R13 · Biao Zhang, Williams, Titov & Sennrich (2020) · OPUS-100 · `CM`

_Improving Massively Multilingual Neural Machine Translation and Zero-Shot Translation_, ACL 2020, 1628–1639 · [ACL Anthology](https://aclanthology.org/2020.acl-main.148/)

- **Bài làm gì.** Giới thiệu OPUS-100: các cặp song ngữ đều ghép với tiếng Anh.
- **Nhóm dùng vào.** Corpus của pilot; lý do phải đo phần giao câu EN giữa các cặp ([T2](#t2)).
- **Không dùng để nói.** Độ dài và tỷ lệ câu ngắn phải lấy từ dữ liệu pilot.
- **Mở ở đâu.** Phần dataset.

<a id="r14"></a>
#### R14 · Yang et al. (2024) · Qwen2.5 · `CM`

_Qwen2.5 Technical Report_, arXiv:2412.15115 · [báo cáo](https://arxiv.org/abs/2412.15115) · [model card 1.5B](https://huggingface.co/Qwen/Qwen2.5-1.5B)

- **Bài làm gì.** Mô tả họ model Qwen2.5.
- **Nhóm dùng vào.** Ghi đúng checkpoint của model pilot ([T1](#t1), [T4](#t4)).
- **Không dùng để nói.** Báo cáo không cho biết câu OPUS nào đã có trong pretraining.
- **Mở ở đâu.** Phần architecture và pretraining; model card của đúng checkpoint.

<a id="r17"></a>
#### R17 · NLLB Team et al. (2022) · FLORES-200 · `CM`

_No Language Left Behind: Scaling Human-Centered Machine Translation_, arXiv:2207.04672 · [bài](https://arxiv.org/abs/2207.04672) · [dataset card](https://huggingface.co/datasets/facebook/flores)

- **Bài làm gì.** Giới thiệu FLORES-200: cùng một tập câu đã dịch sang hơn 200 ngôn ngữ.
- **Nhóm dùng vào.** Corpus tham chiếu để đếm PFR ([T2](#t2)).
- **Không dùng để nói.** Văn bản dịch có thể khác văn bản tự nhiên; FLORES không phải nhãn membership.
- **Mở ở đâu.** Phần FLORES-200.

### D. Thống kê

<a id="r11"></a>
#### R11 · Angelopoulos & Bates (2023) · Conformal prediction · `CM`

_Conformal Prediction: A Gentle Introduction_, Foundations and Trends in Machine Learning · [tạp chí](https://doi.org/10.1561/2200000101) · [preprint](https://arxiv.org/abs/2107.07511)

- **Bài làm gì.** Giới thiệu split conformal: bảo đảm phủ dưới giả định hoán đổi được.
- **Nhóm dùng vào.** Chỉ khi nhóm muốn một bảo đảm FPR có chứng minh ([T9](#t9)).
- **Không dùng để nói.** Bảo đảm là phủ biên trung bình, không chuyển nguyên sang từng nhóm ngôn ngữ.
- **Mở ở đâu.** Phần split conformal và exchangeability.

<a id="r15"></a>
#### R15 · Hanley & McNeil (1982) · Ý nghĩa của AUROC · `CM`

_The Meaning and Use of the Area Under a Receiver Operating Characteristic (ROC) Curve_, Radiology 143(1), 29–36 · [PubMed](https://pubmed.ncbi.nlm.nih.gov/7063747/)

- **Bài làm gì.** AUROC là xác suất xếp đúng một cặp positive–negative; cho công thức xấp xỉ SE.
- **Nhóm dùng vào.** Định nghĩa outcome chính ([T5](#t5)); phép tính cỡ mẫu minh hoạ ([T13](#t13)).
- **Không dùng để nói.** CI chính của nhóm dùng bootstrap theo family, không dùng công thức này.
- **Mở ở đâu.** Toàn bài.

<a id="r16"></a>
#### R16 · Holm (1979) · Holm step-down · `CM`

_A Simple Sequentially Rejective Multiple Test Procedure_, Scandinavian Journal of Statistics 6(2), 65–70 · [JSTOR](https://www.jstor.org/stable/4615733)

- **Bài làm gì.** Thủ tục kiểm soát sai số theo họ khi có nhiều phép kiểm.
- **Nhóm dùng vào.** Họ phép kiểm confirmatory khóa ở C-final ([T10](#t10), [T13](#t13)).
- **Không dùng để nói.** Phân tích sensitivity và exploratory gắn nhãn riêng, không gộp vào họ này.
- **Mở ở đâu.** Toàn bài.

<a id="r24"></a>
#### R24 · DeLong, DeLong & Clarke-Pearson (1988) · So hai AUROC tương quan · `CM`

_Comparing the Areas under Two or More Correlated Receiver Operating Characteristic Curves: A Nonparametric Approach_, Biometrics 44(3), 837–845 · [PubMed](https://pubmed.ncbi.nlm.nih.gov/3203132/)

- **Bài làm gì.** Dùng U-statistic để tính covariance khi hai phép chấm dùng chung các case.
- **Nhóm dùng vào.** Logic so ghép cặp cho ΔAUROC và cho chênh giữa hai detector ([T6](#t6), [T10](#t10), [T13](#t13)).
- **Không dùng để nói.** Công thức giả định case độc lập; với bản dịch lồng trong family thì dùng bootstrap theo family.
- **Mở ở đâu.** Chỉ đã xem abstract và metadata.

<a id="r28"></a>
#### R28 · Xin Tong, Feng & Li (2018) · Neyman–Pearson classification · `CM`

_Neyman-Pearson Classification Algorithms and NP Receiver Operating Characteristics_, Science Advances 4(2), eaao1659 · [DOI](https://doi.org/10.1126/sciadv.aao1659) · [bản tác giả](https://statistics.arizona.edu/sites/default/files/2023-09/Journal%20Paper%20091823.pdf)

- **Bài làm gì.** Thuật toán NP umbrella: chọn ngưỡng từ order statistic của điểm lớp null để giới hạn xác suất FPR vượt α.
- **Nhóm dùng vào.** Giải thích cỡ mẫu calibration cho ngưỡng FPR thấp ([T9](#t9), [T13](#t13)); ví dụ `n ≥ 299` ở α = 0,01 trong [hướng dẫn](implementation-guide.md).
- **Không dùng để nói.** Bảo đảm cần iid và điểm liên tục; thiết kế có ties, trọng số và family phải phân tích riêng.
- **Mở ở đâu.** Phần NP umbrella; Proposition 1–2.

### E. Nghiên cứu phơi nhiễm có kiểm soát và định vị đóng góp

Các bài ở mục này được thêm ở v2.13–v2.14. Claude đã đối chiếu metadata và abstract ngày 18/11; vị trí section là do Codex ghi, **cần mở trước khi trích chi tiết**.

<a id="r25"></a>
#### R25 · Banaei, Shahzad, Maguire Jr., Chiesa & Kostić (2026) · Phơi nhiễm có kiểm soát trên OLMo 2 · `AB`

_From Training Exposure to Membership Evidence: A Controlled Study of OLMo 2_, arXiv v1 (30/10/2026) · [arXiv v1](https://arxiv.org/html/2610.41732v1)

- **Bài làm gì.** Chạy lại giai đoạn mid-training của OLMo 2 1B với các **cặp tài liệu ghép**, và dùng run chính thức của AI2 làm đối chứng phản thực tế. Abstract kết luận cần một đối chứng tương đương để MIA hoạt động tốt. *Ghép theo biến nào và gán bằng cách nào (ghi chú v2.14 nói: độ khó, độ dài, tung đồng xu) chưa được mở để xác nhận.* Kết luận trong abstract: *"One exposure raises a previously unseen document's likelihood on average but rarely identifies it."*
- **Nhóm dùng vào.** Thiết kế gán phơi nhiễm theo cặp ghép ([T1](#t1)); lý do so với đối chứng tương đương trên cùng cohort ([T3](#t3), [T6](#t6)); kỳ vọng thực tế: một lần phơi nhiễm thường không đủ để nhận diện; phê phán MIA ([T14](#t14)); Limitations ([T15](#t15)).
- **Không dùng để nói.** Họ có run đối chứng gần như sinh đôi; mốc 0× của nhóm thì không. Không dùng số cặp hay AUROC của họ làm định mức.
- **Vị trí cần mở.** §§III-C–E (chọn cặp); §IV Eqs. 1–2; §V-A–C; §V-F, Fig. 10.

<a id="r26"></a>
#### R26 · Kocyigit, Briakou, Deutsch, Luo, Cherry & Freitag (2025) · Contamination trong MT · `AB`

_Overestimation in LLM Evaluation: A Controlled Large-Scale Study on Data Contamination's Impact on Machine Translation_, ICML 2025, PMLR 267: 31105–31132 · [PMLR](https://proceedings.mlr.press/v267/kocyigit25a.html)

- **Bài làm gì.** Đưa contamination có kiểm soát vào pretraining của model 1B và 8B cho dịch máy. Theo abstract, contamination **cả nguồn lẫn đích** làm phồng BLEU nhiều nhất; chỉ nguồn hoặc chỉ đích phồng ít hơn và kém nhất quán. Họ cũng xét thời điểm và tần suất.
- **Nhóm dùng vào.** Lý do ledger ghi **view nào** đã vào huấn luyện: EN, L hay cả hai ([T1](#t1)); Related Work ([T14](#t14)).
- **Không dùng để nói.** BLEU đo chất lượng dịch, không dự báo AUROC hay FPR.
- **Vị trí cần mở.** Phần setup source-only / target-only / source+target.

<a id="r27"></a>
#### R27 · Kocyigit & Yildirim (2026) · Contamination qua giai đoạn hậu huấn luyện · `AB`

_The Impact of Post-training on Data Contamination_, arXiv v1 (3/1/2026) · [arXiv v1](https://arxiv.org/html/2601.06103v1)

- **Bài làm gì.** Đưa item GSM8K và MBPP vào pretraining của Qwen2.5 và Gemma3, rồi so sau SFT và GRPO. Theo abstract, hiệu ứng mờ dần khi pretraining thêm, còn SFT và GRPO làm thông tin lộ lại theo cách khác nhau.
- **Nhóm dùng vào.** Limitations: kết luận phụ thuộc giai đoạn huấn luyện; nhóm chỉ đo LoRA ([T14](#t14), [T15](#t15)).
- **Không dùng để nói.** Không thêm SFT/GRPO vào thiết kế chính.
- **Vị trí cần mở.** §§3–5; §5.1.

<a id="r29"></a>
#### R29 · Ahuja, Gumma & Sitaram (2024) · Báo cáo contamination đa ngôn ngữ · `AB`

_Contamination Report for Multilingual Benchmarks_, arXiv v1 (21/10/2024) · [arXiv v1](https://arxiv.org/html/2410.16186v1). **arXiv không ghi venue** — phụ lục cũ ghi "EvalEval workshop" không có nguồn, đã bỏ.

- **Bài làm gì.** Dùng probe hộp đen kiểm xem bảy benchmark đa ngôn ngữ có lọt vào dữ liệu huấn luyện của bảy model không. *Ghi chú v2.14 nói probe so thứ tự gốc của bộ dữ liệu với các thứ tự xáo trộn — chưa mở §3 để xác nhận.*
- **Nhóm dùng vào.** Related Work; lý do FLORES chỉ là corpus tham chiếu PFR chứ không phải ground truth; và lý do probe này không phải comparator phi-likelihood ([T11](#t11), [T14](#t14)).
- **Không dùng để nói.** Kết luận ở cấp bộ dữ liệu, không cho biết câu nào đã có trong huấn luyện.
- **Vị trí cần mở.** §3; Table 1; §5.

<a id="r30"></a>
#### R30 · Wang et al. (2026) · DeMIA · `AB`

_Are Fine-Tuned LLM Membership Signals Real? Separating Memorization from Likelihood Shortcuts_, Findings of EMNLP 2026, 32850–32869 · [ACL Anthology](https://aclanthology.org/2026.findings-emnlp.1544/) · [PDF](https://aclanthology.org/2026.findings-emnlp.1544.pdf)

- **Bài làm gì.** Với LLM đã fine-tune, abstract nêu rằng *"high attack AUC alone is not reliable evidence of data use"*, vì điểm có thể phản ánh độ dài, độ khó hoặc domain. Đề xuất DeMIA, tách phần chấm membership khỏi mô hình độ khó.
- **Nhóm dùng vào.** Base-only control ([T3](#t3)); matched sensitivity theo đặc trưng trước LoRA ([T8](#t8)); phê phán MIA ([T14](#t14)).
- **Không dùng để nói.** Kết quả trên tác vụ tiếng Anh không chuyển thành bảo đảm cho ngưỡng đa ngôn ngữ. DeMIA cần nhãn và likelihood của cả model gốc và model đích, nên để phần mở rộng.
- **Vị trí cần mở.** §§4.1, 4.3–4.4; Appendix C.2–C.4.

<a id="r31"></a>
#### R31 · Meeus, Shilov, Faysse & de Montjoye (2024) · Copyright traps · `CM`

_Copyright Traps for Large Language Models_, ICML 2024, PMLR 235: 35296–35309 · [PMLR](https://proceedings.mlr.press/v235/meeus24a.html)

- **Bài làm gì.** Cài các chuỗi bẫy vào dữ liệu huấn luyện một model từ đầu, phân bổ ngẫu nhiên, thay độ dài và số lần lặp, rồi đo khả năng phát hiện.
- **Nhóm dùng vào.** Tách phơi nhiễm dự kiến và thực tế trong ledger ([T1](#t1)).
- **Không dùng để nói.** Số lần lặp trong một run pretraining cụ thể không suy ra liều LoRA của câu OPUS. Nhóm không tạo bẫy.
- **Vị trí cần mở.** §§4.3–4.5; §5.2; Table 2.

<a id="r32"></a>
#### R32 · Meng Tong, Du, Chen, Zhang & Li (2026) · MIA trên tokenizer · `AB`

_Membership Inference Attacks on Tokenizers of Large Language Models_, arXiv v4 (25/5/2026) · [arXiv v4](https://arxiv.org/html/2510.05699v4)

- **Bài làm gì.** Coi tokenizer là đích tấn công: suy ra một tập dữ liệu có góp vào huấn luyện tokenizer hay không; đề xuất năm phương pháp và một cách phòng thủ thích ứng (có trong abstract). *Ghi chú v2.14 nói các phương pháp dựa vào vocabulary và merge rules — chưa mở để xác nhận.*
- **Nhóm dùng vào.** Introduction: nói rõ **đích membership** của nhóm là dữ liệu huấn luyện adapter, không phải dữ liệu huấn luyện tokenizer ([T11](#t11), [T14](#t14)).
- **Không dùng để nói.** Không đưa các phương pháp của bài vào RQ2, vì chúng đổi đích của nhãn.
- **Vị trí cần mở.** §3; §§5.1–5.2; §7.

---

## 3. Viết Introduction và Related Work

**Thứ tự đề xuất cho Introduction:**

1. Đo contamination đa ngôn ngữ đang dựa vào detector likelihood ([R1](#r1), [R2](#r2)).
2. Cùng một nội dung tốn số token rất khác nhau giữa các ngôn ngữ ([R5](#r5), [R21](#r21)).
3. Đánh giá MIA dễ sai vì lệch phân phối và đối chứng không tương đương ([R3](#r3), [R4](#r4), [R23](#r23), [R30](#r30)).
4. Phơi nhiễm qua bản dịch có thật và khó phát hiện ([R9](#r9), [R19](#r19)).
5. Câu hỏi của nhóm và đóng góp, ở mức kết quả có thể thu được.

**Câu mở đề xuất:** *"Chúng tôi kiểm tra mối liên hệ giữa PFR trên câu song song và AUROC của detector likelihood, trong một thiết kế phơi nhiễm bổ sung có kiểm soát bằng LoRA với nhãn đã xác minh theo từng lần chạy."* Không dùng từ "gây ra": claim nhân quả về tokenizer cần thiết kế can thiệp bổ sung ([T15](#t15)).

**Các câu delta** — mỗi dòng Related Work kết thúc bằng một câu nói rõ nhóm khác ở đâu:

| Dòng | Bài | Câu delta |
|---|---|---|
| Ngôn ngữ và rò rỉ | [R22](#r22) | R22 cho thấy mức rò rỉ khác nhau giữa các ngôn ngữ với shadow model và thuộc tính ký tự/cú pháp. Nhóm đo **PFR cấp subword trên câu song song**, dùng **detector likelihood native** và **nhãn phơi nhiễm theo lần chạy** |
| Tokenizer giữa ngôn ngữ | [R5](#r5), [R21](#r21), [R20](#r20) | Dòng này đo **chi phí** và **bất công với người dùng**. Nhóm hỏi hệ quả lên **tính hợp lệ của một phép đo** |
| Contamination qua bản dịch | [R9](#r9), [R19](#r19), [R26](#r26) | Các bài này đo điểm benchmark hoặc probe tiếng Anh. Nhóm đo **AUROC theo PFR** trên nhãn đã xác minh |
| Phê phán MIA | [R3](#r3), [R4](#r4), [R23](#r23), [R30](#r30), [R25](#r25) | Dòng này chỉ ra điều kiện đánh giá làm sai kết luận. Nhóm áp các phép kiểm đó vào **bối cảnh đa ngôn ngữ**, nơi độ dài token đi cùng chính biến giải thích |
| Đích của membership | [R32](#r32) | Nhóm đo membership của dữ liệu huấn luyện **adapter**, không phải tokenizer |

**Novelty.** Lượt tra ngày 18/11/2026 có phạm vi giới hạn (xem [Mục 5](#5-rà-nguồn-mới)). Không viết "đầu tiên" hay "chưa ai làm" ở cấp "ngôn ngữ ảnh hưởng MIA" — [R22](#r22) đã làm phần đó.

## 4. Mở đúng đoạn trước khi viết

| Chỗ gốc cần đọc | Ý trích và dùng ngay | Câu phải tự kiểm trước khi viết |
|---|---|---|
| [R1 §3, Eq. 1](#r1) và [R2 §4.2, Eq. 3–4](#r2) | R1 chọn đuôi theo log-prob gốc. R2 chuẩn hoá theo phân phối tại prefix rồi mới chọn đuôi | Cùng prefix và văn bản giữ lại chưa? Code đã giữ đúng thứ tự chuẩn hoá → chọn chưa? Có báo k thực tế không? |
| [R3 v2 Table 2](#r3) và [R4 §§3–4](#r4) | Một số benchmark có baseline mù vượt detector; chênh nguồn và chồng lấp ảnh hưởng separation | Kết quả nói về benchmark nào, đặc trưng văn bản nào, metric nào? |
| [R5 §§3–4 và code](#r5), [R21 §3, Table 2](#r21) | Tỷ số token trên nội dung dịch và tax trên token/từ là hai phép đo khác nhau | Bài đếm văn bản nối hay từng câu? Có lấy EN làm tham chiếu đúng version không? |
| [R7 §§3–4](#r7) | Mỗi đường phân đoạn có xác suất riêng; marginal là tổng qua các đường | Có dùng lại token sequence và cache, hay forward lại với phân đoạn khác? |
| [R19 v2 Table 6 và Limitations](#r19), [R26 setup](#r26) | Điểm probe tiếng Anh, view được huấn luyện và lượng văn bản thực tế là ba cột riêng | Có nêu view đích, hay đã gộp nhãn family thành membership chính xác? |
| [R20 Appendix C.3, Table 5](#r20) | Cùng thứ tự dữ liệu và ngân sách token có thể khác lượng byte đã tiêu thụ | **Chưa đọc** Appendix C.3 — mở trước khi trích |
| [R22 Findings Fig. 5](#r22) | Bản hội nghị dùng ROC/AUC; bản preprint ghi accuracy | Đã đối chiếu đúng phiên bản, classifier, model và thước đo chưa? |
| [R25 §IV Eqs. 1–2, §V-F](#r25) và [R30 Appendix C.2–C.4](#r30) | Quy tắc giữ cặp, gain so với đối chứng, đo độ khó trước khi phơi nhiễm | **Chưa đọc thân bài** — mở trước khi trích. 0× có thật sự tương đương run sinh đôi không, hay chỉ là mốc trước LoRA? |
| [R28 Proposition 1–2](#r28) | Cỡ mẫu calibration cho xác suất vi phạm là bài toán riêng với CI của test | Giả định iid và liên tục có đúng không, hay thiết kế có ties và nhiều view trong family? |

## 5. Rà nguồn mới

- **Phạm vi lượt tra 18/11/2026:** các cụm multilingual contamination, controlled training exposure, fine-tuned likelihood shortcuts, tokenizer-training membership và low-FPR order statistics. Ưu tiên ACL Anthology, PMLR, trang tác giả và arXiv có version.
- **Trước buổi họp nhóm:** đọc [R25](#r25), [R30](#r30) lên mức `PL` (hai bài này đang chống đỡ thiết kế nhãn và control mà mới ở mức `AB`), cộng [R5](#r5) §§3–4 và phần công thức của [R1](#r1)/[R2](#r2).
- **Khi chốt ngưỡng:** [R28](#r28) Proposition 1–2.
- **Khi viết Related Work:** [R22](#r22), [R26](#r26), [R27](#r27), [R29](#r29), [R32](#r32).
- Bài mới chỉ được thêm khi có **vai trò cụ thể** trong một mục T ở trên và **nguồn có version**.

## 6. Kiểm phủ: mỗi bài phục vụ phần việc nào

Bảng này để kiểm rằng không bài nào nằm trong phụ lục mà không có việc, và không việc nào thiếu nguồn mà không ghi "phần nội bộ".

| Bài | Mức | Phần việc |
|---|---|---|
| [R1](#r1) | `TV` | T4, T5, T7, T10, T14 |
| [R2](#r2) | `TV` | T4, T10, T14 |
| [R3](#r3) | `TV` | T3, T11, T14 |
| [R4](#r4) | `TV` | T3, T7, T14 |
| [R5](#r5) | `TV` | T2, T5, T7, T12, T14 |
| [R6](#r6) | `CM` | T12, T15 |
| [R7](#r7) | `TV` | T4, T12 |
| [R8](#r8) | `CM` | T12, T15 |
| [R9](#r9) | `TV` | T1, T14 |
| [R10](#r10) | `TV` | T11, T14 |
| [R11](#r11) | `CM` | T9 |
| [R12](#r12) | `CM` | T1 |
| [R13](#r13) | `CM` | T2 |
| [R14](#r14) | `CM` | T1, T4 |
| [R15](#r15) | `CM` | T5, T13 |
| [R16](#r16) | `CM` | T10, T13 |
| [R17](#r17) | `CM` | T2 |
| [R18](#r18) | `CM` | T11 |
| [R19](#r19) | `TV` | T1, T6, T14 |
| [R20](#r20) | `PL` | T2, T8, T14, T15 |
| [R21](#r21) | `TV` | T2, T8, T14 |
| [R22](#r22) | `TV` | T14 |
| [R23](#r23) | `TV` | T3, T14, T15 |
| [R24](#r24) | `CM` | T6, T10, T13 |
| [R25](#r25) | `AB` | T1, T3, T6, T14, T15 |
| [R26](#r26) | `AB` | T1, T14 |
| [R27](#r27) | `AB` | T14, T15 |
| [R28](#r28) | `CM` | T9, T13 |
| [R29](#r29) | `AB` | T11, T14 |
| [R30](#r30) | `AB` | T3, T8, T14 |
| [R31](#r31) | `CM` | T1 |
| [R32](#r32) | `AB` | T11, T14 |

**Tổng:** 12 bài `TV`, 1 bài `PL`, 6 bài `AB`, 13 bài `CM`. Hai bài chống đỡ trực tiếp thiết kế nhãn và control — [R25](#r25) và [R30](#r30) — đang ở mức `AB`; đọc chúng lên `PL` là việc nên làm trước C-final.
