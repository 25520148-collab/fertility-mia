# Hướng dẫn làm nghiên cứu từ dữ liệu đến bài báo · v2.15

Đọc cùng [plan](../../plan.md), [phiếu họp](../../group-meeting.md), [phụ lục nguồn](literature-application-map.md) và [sổ tay khái niệm](paper-concepts.md). Các tên tệp đầu ra bên dưới là đề xuất để mọi người tìm cùng một chỗ. Ví dụ số là dữ liệu giả dùng để hiểu phép đo.

## 1. Chốt tên của thứ mình đang đo

| Câu hỏi | Đơn vị | Quan sát cần có | Kết luận có thể viết |
|---|---|---|---|
| Văn bản bị chia nhỏ đến đâu? | Cặp EN–L, một tokenizer revision | Số token của hai bản trên cùng policy | Bản L dùng bao nhiêu token so với bản EN trong corpus này |
| Detector xếp mẫu exposed cao hơn bao nhiêu? | Một cặp positive–negative trong cùng eval cell | Score và nhãn exposure xác thực cho target | AUC của cách chấm trong chế độ phơi nhiễm đã chạy |
| Exposure đi cùng thay đổi gì so với mốc gốc? | Cùng evidence cohort, score ở hai checkpoint | AUC ở cả hai checkpoint, hoặc score per item để tính thay đổi | Chênh separation hoặc chênh score theo estimand đã chọn |
| Một ngưỡng chuyển giữa ngôn ngữ được không? | Ngưỡng fit trên cal, áp vào test | Score, FP/N₀ và TP/N₁ ở mỗi ngôn ngữ | Tỷ lệ gắn cờ sai/đúng tại ngưỡng đó cùng độ bất định |
| Cách chấm mới có tốt hơn cho nhóm ngôn ngữ thấp? | Cùng samples và hai scoring rules | Rank, AUC từng ngôn ngữ, coverage, CI ghép cặp | Các tiêu chí RQ3 đã qua hoặc còn bất định |

**Eval cell** là một bộ `backbone × run/seed × language × exposure setting × detector`. Một family nội dung có thể xuất hiện ở nhiều cell. Khi tính CI, giữ cấu trúc đó. Với checkpoint trước LoRA, nhãn dùng cho AUC là *assignment dự kiến* sẽ áp ở run sau. Scope nhãn là dữ liệu nhóm thêm vào run, còn pretraining gốc ngoài tầm quan sát nếu thiếu stream. [R3, R4, R25](literature-application-map.md)

## 2. P01 · Thu hồi tài sản và tái dựng nhãn

**Người làm:** người giữ notebook cùng một người kiểm chéo. **Đầu vào:** exact texts và split gốc, tokenizer/model revision, adapter IDs, run/seed, config, optimizer-visible stream, score cache. **Đầu ra:** `asset-inventory.md`, manifest theo [schema](pfr-and-splits.md), bảng `eligible → scored` có counts theo nhãn/ngôn ngữ.

1. Tạo một dòng mỗi `target_run × family × view`. Family gồm một nội dung và các bản dịch/near-dup liên quan. View là một bản ngôn ngữ hoặc biểu diễn cụ thể của family. Lưu cân bằng labels đã định và nhãn thực tế ở hai cột riêng.
2. Kiểm exact match và lượng text thực sự đến optimizer sau cắt đoạn. Ví dụ family F được chọn, train thấy F-VI nhưng chấm F-JA. Nhãn F-VI là direct nếu span khớp. F-JA là **translation-only**. F-JA không dùng làm negative chưa exposed family. Nếu chỉ nửa đầu F-VI thấy khi train và score cả câu, cờ là partial, cần policy riêng. File config muốn thấy F mà log thiếu bằng chứng thì eligible = unknown. Xem R9, R19, R26.
3. Định nghĩa hai câu hỏi riêng nếu nhóm cần: detect **direct exposure** trên direct so với verified control, và transfer sang cùng family trên translation-only so với verified control. Báo translation-only/partial/unknown riêng và counts bị loại. Nếu pilot chỉ có assignment, báo phân tích theo assignment như một kết quả khác và ghi tỷ lệ sai lệch có thể kiểm được.
4. Detector dev, calibration và final test giữ family disjoint. Positives của detector test vẫn đến từ target training. Không nhập chung “train của model” và “train của detector” thành một cột. Đối chiếu overlap cả exposure stream **và** background.
5. Chốt mẫu trước khi nhìn score. Khi tình trạng exposure/score bị thiếu khác nhau giữa nhóm, ghi count theo từng lý do và nhãn/cell. Phân tích complete-case áp dụng cho phần đủ dữ liệu. Nếu vi phạm gán nhãn trong prospective test, ghi deviation và nhóm chốt lại phạm vi trước khi diễn giải.

**Vì sao:** nếu coi F-JA là control, detector có thể phát hiện dấu vết của nội dung đã thấy, rồi mình tính nó là false positive của tập supposedly unexposed. Để đánh giá transfer, chính ví dụ đó là một treatment khác. R25 cho tiền lệ randomize trong cặp có difficulty gần nhau và ghi nhận score của controls cũng dịch sau training. Vì vậy bảng label đúng vẫn cần đối chứng training và đo trên control chung. Mốc 0× giúp đo baseline difficulty. Sham cùng ngân sách trên text đối chứng disjoint là nhánh mạnh hơn khi câu hỏi đòi phân biệt adaptation chung.

**Nếu thiếu:** ghi rõ inventory nào chưa thể tìm, người giữ và ngày. Notebook mới từ OPUS được phép làm rerun nếu nhóm duyệt với version riêng, không gắn lại cho pilot gốc. Không tái tạo số từ ảnh/chỉ số tổng hợp.

## 3. P02b/P02c · Đếm tokenizer và kiểm tính so được

1. Dùng corpus reference FLORES để kiểm tokenizer trên cùng IDs. Với Petrov, tái tạo cách đếm của tác giả khi đối chiếu số in bảng. Dùng protocol riêng, đếm từng câu để tính PFR của nhóm. Cặp có EN 10 token, VI 15 token có PFR 1,5. Nếu cặp khác EN 100/VI 120 thì median hai ratios là 1,35 và ratio-of-totals là 135/110 ≈ 1,23. Phép sau cho câu dài sức nặng lớn hơn. R5/R17 hỗ trợ measurement. R21 cho tax theo whitespace words, do đó không nhập làm cùng cột.
2. In bảng từ 3 đến 5 checkpoint ứng viên ở mức **CPU tokenizer only** nếu có revision/licence. Khoá chính sách BOS/EOS, Unicode, normalization, padding/truncation. Lưu `tokenizer_matrix` theo corpus/version. PFR trên reference và PFR theo cohort OPUS có thể khác nhau vì corpus và độ dài.
3. Lấy giao EN pivot có nguồn và ID, từ đó lập bảng `cell × bin × class`. Nếu target nói 20 token và EN 10, PFR 2. Nếu câu khác EN 5, cùng target 20 thì PFR 4 vì đổi nội dung. Phân tích cùng nội dung giữ estimand primary. Lọc hoặc cân bằng số token là sensitivity trên tập có common support. Ghi coverage và sự thay đổi composition. Không extrapolate ra bin có thiếu một lớp.
4. Lập audit exact, near duplicate và character n-gram. Giữ một unit, n và preprocessing đã khóa. Báo nhóm câu ngắn thiếu gram và source clusters. R4 đề xuất nhìn độ chồng lấp như rủi ro đo lường. Không mượn trực tiếp cutoff 20% từ thí nghiệm khác để loại mẫu. Chạy P02c trên exact split sau P01.
5. Chốt cách gộp **bằng đơn vị đích**. Ví dụ AUC_1=.70, AUC_2=.50 và weights dev theo token bins là .6/.4 thì within-bin AUC chuẩn hoá là .62. Tính AUC trên union có thể cho số khác vì nó đếm thêm các so sánh khác bin. Nếu tính theo family, nêu quy tắc một view/family/language hoặc trọng số để family có nhiều biến thể không chi phối tự động.

**Nghiệm thu:** cả hai bảng token counts full-content và scored, source/pivot coverage, support trước–sau, PFR variation và split check. Mỗi số có script/commit, tokenizer revision và IDs. Đi tiếp với cohort mô tả nếu common support thiếu.

## 4. P03 · Chấm điểm từ cùng cache và hiểu kết quả

Ví dụ 5 token có log-prob theo thứ tự `[-.2,-2.0,-.6,-1.0,-.5]`. Min-K20 chọn vùng xác suất thấp nhất. Với đúng 1 token được chọn, điểm là −2.0. Mean log-prob dùng cả 5, bằng −.86. Min-K%++ cần cùng vị trí nhưng chuẩn hoá từng log-prob bằng moment của **phân phối toàn vocab tại vị trí đó** rồi mới chọn đuôi, nên top-k token IDs có thể đổi. Native scorer nên có exact version và fallback cho fewer-than-k/masked tokens. R1/R2 hỗ trợ công thức. R6–R8 cho bối cảnh phân đoạn thay thế, chỉ dùng để giải thích vì sao đó là can thiệp khác.

**Chấm đúng:** cache giữ checkpoint/revision, text hash, mask, BOS hoặc prefix, dtype, target logp, μ, σ và reason cho NaN. Loại token padding/special theo scoring specification. Check hướng score, rounding, ties, shift index ở causal LM và replay trực tiếp trên fixture. Báo ngắn/NaN riêng từng lớp. So hai rule trên cùng IDs và bytes. Native Min-K so với span variant có thể đổi selection lẫn aggregation. Muốn quy thay đổi cho aggregation, cố định các phần khác và kiểm fixture.

**Đọc AUC:** hai positives có score .8/.4, hai negatives .6/.4. Có 2 thắng, 1 thua, 1 tie, AUC=.625. Ví dụ trên cùng cohort, checkpoint base AUC .55 và after .65 thì ΔAUC=.10. Tính AUC trên từng hiệu score after−base là một phép khác và cần toàn bộ score từng item. CI của chênh dùng ghép cặp family bởi cả hai checkpoint chấm lại các case giống nhau. R15/R24 hỗ trợ định nghĩa và logic covariance. R25 minh hoạ AUC cao hơn vẫn có thể đi cùng TPR rất thấp ở ngưỡng chặt.

**Chẩn đoán B0 và 0×:** fit B0 trên dev, chọn cùng feature protocol trước test và báo per cell. Tín hiệu text-only thúc đẩy kiểm label/source/mã hóa, đồng thời xem CI và degree of matching. Nếu hoán vị nhãn để kiểm assignment, làm tại **checkpoint mốc** với rule ngẫu nhiên thật, giữ family/pair/strata và fit lại bước học của B0 nếu có. Score sau train phụ thuộc assignment qua model, nên không dùng phép đổi nhãn giản đơn để suy ra causal exposure. R3/R4/R23/R25 là lý do kiểm trước khi gửi bảng kết quả.

## 5. RQ1–RQ3 · Từ bảng số sang kết luận

### RQ1 · Association và chuyển ngưỡng

- Đề xuất một backbone, một dose chính và native Min-K20 làm primary measurement, sau C-final. Lập mỗi dòng model–language có gộp seeds theo trọng số đã khóa và lưu từng seed. Đề xuất PFR median trên cohort aligned đánh giá, NLL base lấy từ calibration/dev với comparable source/length và đúng checkpoint. Chọn một proxy và một thang (ví dụ log₂ PFR), lưu ma trận thật và kiểm residual variation/leverage. Báo adjusted và raw kèm estimate/CI theo finite panel. RQ1 cũ có cụm "kiểm soát perplexity"; câu RQ1 hiện hành thay bằng "điều chỉnh theo độ khó trước LoRA, chỉ khi biến đo đã chốt". Nếu nhóm vẫn báo logPPL thì đó là sensitivity, và phải nêu logPPL chia cho số token nên chứa chính `T_L` ở mẫu số. Slope dương chỉ nghĩa là association trên panel nếu support đủ, vì pretrained model, nguồn và dài/ngắn có thể đồng thay đổi. Theo R30, có thể làm matched sensitivity từ pre-target features (ví dụ log độ dài ký tự + base NLL) với policy khóa trên dev, báo balance trước/sau, retained families và dải PFR. Matching thay estimand và có thể mất support, nên báo cùng full cohort.
- Chuyển ngưỡng dùng weights khóa trước. Ví dụ EN và VI mỗi ô đạt 8/100 false positives khi α mục tiêu .05, và gap giữa hai ô là 0. Ngưỡng vẫn lệch 3 điểm phần trăm từ mục tiêu ở cả hai. Báo **gap lẫn absolute rates**, đồng thời TPR và coverage. Quantile fit trên cal rồi áp test, báo ties với `score > τ`. Khi bootstrap giữ family shared cross-language, giữ riêng vai trò cal/test và fit lại ngưỡng. Báo uncertainty conditional trên fixed panel/checkpoints. R11/R28 dùng để giải thích giả định khi đòi guarantee, empirical quantile và test counts là phần main. Nếu chấm nhiều ngưỡng sau khi xem data, gọi sensitivity. Chưa có nhãn thì chỉ báo flag-rate/disagreement.
- Precision demo: 150 negatives độc lập mà 0 false positive cho 95% upper bound ≈ 1,98%, đủ giải thích vì sao FPR 1% rất khó xác nhận. Với cal iid/continuous và threshold bằng max, xác suất true tail FPR > α là `(1−α)^n`. Ở α=.01, conf .95, công thức cho n≥299. Đây là minh hoạ của một policy và một null distribution, không là gate cỡ mẫu chung cho pooled/clustered design. R28.

### RQ2 · Độ dốc theo PFR của chênh AUROC

So AUC từng detector là bảng mô tả. Câu RQ2 hỏi **mối liên hệ với PFR có khác giữa hai detector không**, nên kiểm trực tiếp contrast `β_MinK++−β_MinK` trên cùng test cases và same covariate policy. **Ca kiểm trước khi mở test:** cho AUC của A luôn hơn B đúng 0,05 ở mọi PFR, ví dụ A = (.70, .65, .60) và B = (.65, .60, .55) tại PFR = (1, 2, 3). Chênh là (.05, .05, .05), nên chênh trung bình phải ra .05 và độ dốc của chênh phải ra 0. Pipeline trả độ dốc khác 0 là pipeline sai. Báo dấu/trị tuyệt đối của từng slope. Nếu claim “++ ít nhạy hơn” dựa trên magnitude, khóa `|β_++|−|β_MinK|` riêng và kiểm CI gần zero; so dấu đơn thuần không trả lời magnitude. Nếu chỉ dư ngân sách cho hai native methods, ghi phần phi-likelihood chưa trả lời. B0 là chẩn đoán split, DC-PDD dùng model token probabilities còn TS-Guessing cần benchmark slots. Lý do từng ứng viên ở [phụ lục T11](literature-application-map.md#t11).

### RQ3 · Cách normalization có thể đổi AUC

Một ứng viên để mô phỏng dev: lấy native score q, fit trend `q≈a_l+b·log₂(PFR_i)` trên control dev, rồi score `q'=q−b·log₂(PFR_i)`. Đây là **ứng viên nội bộ**, cần EN view hợp lệ lúc chấm, một slope chung làm lựa chọn tối giản, language intercept trong fit, robust support và đủ family. Đầu vào missing thì báo unscorable. Không fit lại từ test. Ví dụ positive .70, negative .60 với PFR lần lượt 4 và 1, b=.10 thì score mới .50/.60, thứ hạng đảo. Khi dùng một hằng cho cả ngôn ngữ, thứ hạng giữ nguyên. Dấu của đổi rank và tác động AUC phải đo, ví dụ này có thể làm xấu đi. So trên common cases, in AUC native all-eligible riêng để nhận ra selection.

Tại C-final, khóa dispersion, biên δ, low-group q chọn từ dev và khoảng tin cậy. Ví dụ AUC baseline hai ngôn ngữ .60/.80, variant .60/.65, gap thu hẹp nhưng AUC trung bình giảm và nhóm yếu giữ nguyên. Kế hoạch yêu cầu giảm dispersion, non-inferior mean và cải thiện nhóm low đã khóa. Ngược lại, native [.60,.70,.90] sang [.64,.86,.76] có thể qua ba tiêu chí nhưng ngôn ngữ thứ ba giảm .14. Vì vậy báo mọi ngôn ngữ và đăng ký biên harm riêng khi claim bảo vệ từng ngôn ngữ. Nếu CI chưa đạt một tiêu chí, ghi mức bất định. Biến thể dùng bản EN có phạm vi paired audit.

## 6. Từ kết quả sang bản thảo

| Đầu ra nhóm tạo | Câu có thể đưa vào bài | Kiểm trước khi dẫn |
|---|---|---|
| Matrix PFR + IDs | Trên corpus/tokenizer cụ thể, median PFR và spread quan sát là … | R5 về khái niệm, R21 về tax, số của nhóm từ artifact |
| AUC, ΔAUC, CI theo cell | Native detector xếp hạng exposed/control với AUC … dưới regime LoRA này | Exposure join, split, scores, output cả seeds |
| Threshold/holdout counts | Ở ngưỡng fit trên cal, ngôn ngữ … có FPR … và TPR … | Tie/threshold policy, sample counts, uncertainty và scale |
| Scoring variant giữ support | Khi đổi scoring rule trong cùng checkpoint/cache, … | Range và coverage, lựa chọn trên dev, matched CI |
| Result null với CI rộng | Dữ liệu hiện có chưa phân biệt được giữa các cỡ hiệu ứng này | Sufficient precision/equivalence margin nếu nhóm muốn claim nhỏ |
| Trích bài công bố trước | Bài A báo … trên bộ dữ liệu/model …, nhóm chuyển phần thiết kế … | Mở đúng phiên bản và section, ghi vai trò và điểm khác trước khi trích |

Mỗi claim nối với source section hoặc artifact path/hash. C-prep kết thúc khi có budget đo, sample support, label policy, quyết định RQ1–RQ3 và feasibility cho phần tính toán. W1 viết Method/Related Work từ kế hoạch đã duyệt. W2 viết Results sau freeze và cập nhật claim ledger. W3 có người kiểm số, người kiểm nguồn và người đọc dễ hiểu.
