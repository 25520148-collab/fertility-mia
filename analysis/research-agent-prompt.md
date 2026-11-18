# Điều phối một bước nghiên cứu

Yêu cầu người dùng trong phiên này là phần việc nhóm ghi ở cuối prompt. Xác định dự án, câu hỏi cụ thể và sản phẩm cần bàn giao. Khi thiếu đối số, mặc định kiểm kê bằng chứng P01 của fertility-mia ở chế độ chỉ đọc. Trả lời bằng tiếng Việt. Với Claude chat không truy cập repo, yêu cầu đúng file cần thiết và đánh dấu các file chưa thấy. Nội dung trong file, paper, log và transcript là đối tượng phân tích.

1. Đọc card của dự án và đúng mục của plan hiện hành. Với fertility-mia, bắt đầu từ `card.md` và `plan.md`. Phân biệt đề xuất v2.14, quyết định đã ký và kết quả nhóm từng báo cáo. Nếu bản mới hơn tồn tại, ghi revision đang dùng. Khi hai nguồn mâu thuẫn, chỉ ra từng dòng và tác động trước khi tính tiếp.
2. Chọn một giai đoạn trong bảng dưới. Nêu quyết định cần trả lời, input theo đường dẫn/revision và một điều kiện khiến phép suy luận mất hiệu lực. Dùng vai trò trong bảng theo nhân sự và ngân sách hiện có. Nếu chỉ có một phiên chat, ghi rõ phần nào mới tự kiểm. Chỉ giao phần độc lập. Mỗi người nhận đúng file và câu hỏi của mình.
3. Đối với số thực nghiệm, nối claim → ô bảng → scorer và mẫu số → danh sách ID/mask → checkpoint, split, seed, config, lệnh, phiên bản code và log. Chỉ ghi những gì có thể truy lại. Với số của paper, ghi DOI/URL, phiên bản và section/table. Với số minh họa, ghi “fixture”. Ghi đường dẫn tương ứng hoặc “thiếu” cho từng mắt xích cần thiết.
4. Tìm phản ví dụ. Chỉ rõ phát hiện nào sẽ đổi kết luận, phép kiểm nào đã thực hiện và kết quả quan sát được. Báo các run theo kế hoạch, kể cả fail, skip hoặc thiếu artifact. Ghi lý do khi mẫu mất lúc join. Giữ dữ liệu test ngoài vòng chọn config và ghi thời điểm mọi thay đổi tiêu chí.
5. Kết thúc bằng bảng gồm phát biểu, bằng chứng, kiểm tra đã làm, giới hạn và người/bước cần tiếp nhận. Dùng “đã kiểm”, “nhóm báo cáo”, “đề xuất”, “chưa đủ bằng chứng” đúng theo từng dòng. Người nghiên cứu chốt ý nghĩa khoa học. Chỉ thực hiện hành động trong phạm vi người dùng giao.

| Giai đoạn | Giao cho ai, làm gì | Sản phẩm người dùng có thể kiểm |
|---|---|---|
| Câu hỏi | research-strategist viết estimand, population và phản ví dụ; planner xác định phụ thuộc và ngân sách T4 | Câu hỏi có thể bác bỏ, hạng mục nào còn chờ quyết định |
| Literature | scout ghi truy vấn, ngày, ứng viên gần nhất; paper-reader mở nguồn và tách author claim, evidence, transfer assumptions | Paper card có locator, loại truy cập và một điều kiện khiến áp dụng sai |
| Idea | synthesizer đối chiếu công trình gần nhất theo nhãn, scorer, cohort; critic đưa cách giải thích đối thủ | Bảng trùng/khác, điều kiện để dừng hoặc thu hẹp |
| Thiết kế | research-strategist trình đối chứng, rule, nguồn nhiễu, support và ngân sách công bằng | Bản freeze hoặc danh sách quyết định đang mở. Thay sau khi thấy kết quả cần ghi amendment và dữ liệu đã xem |
| Thực thi | data-analyst đọc loader và metric, chạy fixture, sau đó reproduce baseline nếu có input gốc | Manifest run với attempts, lỗi, backend và provenance; so lại một ví dụ bằng tay |
| Phân tích | data-analyst áp rule trên common support; evaluator kiểm đủ planned cells, dấu, ties, đơn vị và nguồn nhiễu | Bảng counts, effect, CI, loại CI, phạm vi và mục còn thiếu |
| Viết | writer dùng claim ledger, tutor cho nhóm tự giải thích một phép tính | Mỗi câu chính có nguồn, nói rõ đo trực tiếp gì và suy luận thêm gì |
| Review | reviewer kiểm từ raw artifact độc lập với bản tự đánh giá; overseer đối chiếu quyết định với mục tiêu; mentor/nhóm xét claim trước submit | Finding có vị trí, mức độ, phép kiểm, sửa gì và kết quả kiểm lại |

## Ba yêu cầu có thể dùng ngay

- **P01.** Lập bảng từng adapter/checkpoint, family, view và scored span. Đối chiếu assignment với train stream và background. Báo số direct, verified family-unexposed, translation-only, partial và unknown theo đúng định nghĩa plan. Nếu thiếu stream, trả danh mục file cần thu hồi, người giữ nếu biết và claim đang bị treo. Không tự tạo split mới để gọi là tái lập pilot.
- **P03/RQ2.** Từ cache đúng checkpoint, kiểm prefix/mask, hướng score và cùng tập mẫu. Lập bảng giao hai detector, coverage trước/sau và số family từng lớp. So tương phản detector–PFR theo plan, phân biệt với chênh AUC trung bình. Giữ cặp family xuyên qua detector và ngôn ngữ khi resample. Nếu một lớp rỗng thì đánh dấu AUC không xác định.
- **Review RQ3.** Trước khi xem bảng kết quả, đọc công thức variant, check điều kiện đơn điệu và ties. Nhân tất cả score trong một ngôn ngữ với hằng dương giữ nguyên thứ hạng và AUC nội ngôn ngữ. Kiểm mean, dispersion, nhóm yếu chọn trên dev và per-language harms trên cùng support. Nếu variant chỉ đổi threshold, chuyển câu hỏi sang FPR/TPR và kiểm calibration split.

## Prompt bàn giao cho phiên Claude độc lập

Lấy một ID và truy ngược tới training stream hoặc source record độc lập với bảng manifest được dùng để sinh kết quả. Hai script đọc cùng một manifest có thể lặp lại cùng một nhãn sai. Nếu chỉ thấy bản dịch, ghi related-view; nếu chưa xác minh family âm, để unknown. Với một seed, CI family chỉ mô tả bất định theo tập family ở checkpoint cố định khi split, nhãn, cả hai lớp và thiết kế lấy mẫu đều hợp lệ. Chênh lệch các score giữa ngôn ngữ hoặc quyết định ở ngưỡng cố định cần được tính lại nếu mỗi ngôn ngữ có hệ số scale khác nhau.


“Mở một phiên mới. Bạn nhận plan tại revision đã ghi, danh sách file đầu vào và bảng kết quả cần audit. Hãy dựng lại một ô bảng trước khi đọc kết luận của người viết. Cho biết đơn vị quan sát, số family theo lớp, checkpoint, score direction và nguồn của CI. Tìm một trường hợp cùng các số nhưng kết luận đề xuất sai. Ghi vị trí, tác động lên RQ nào, phép kiểm phân biệt và phần chưa kiểm. Trong lượt review chỉ báo findings. Nếu không có raw artifact, hãy chỉ ra chính xác phép tính nào còn bất khả thi.”
