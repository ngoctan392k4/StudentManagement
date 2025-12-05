1. MỤC ĐÍCH PHẦN MỀM
- Phần mềm minh họa cách thiết kế hệ thống cacs module và chuyển đổi sang mã nguồn 
- Trong project này, các modules được thiết lập bao gồm: ClassModule, CourseModule, GradeModule, StudentModule
- Demo sẽ thực hiện thêm học sinh mới, gán sinh viên vào một lớp, thêm điểm một môn học cho sinh viên, xuất điểm GPA ra màn hình 

2. DANH SÁCH MODULE ĐÃ CÀI ĐẶT
- ClassModule: quản lý tên lớp và giảng viên của lớp
- CourseModule: quản lý các khóa học với tên khóa học, tín chỉ và loại khóa học
- GradeModule: quản lý điểm số với chức năng chấm điểm, tính GPA) và hiển thị
- StudentModule: quản lý sinh viên với mã sinh viên, tên, khoa, chuyên ngành

3. CHỨC NĂNG CHÍNH (đã implement)
- Tạo 2 lớp học với tên lớp và giảng viên
- Tạo 2 khóa học với tên khóa học, tín chỉ và loại khóa học
- Tạo 1 sinh viên với mã sinh viên, tên, khoa, chuyên ngành
- Cho sinh viên tham gia 2 lớp vừa tạo 
- Gán điểm của sinh viên cho 2 môn học 
- Tính điểm trung bình cho sinh viên 
- Hiển thị thông tin điểm các môn và điểm GPA của sinh viên 

4. THÀNH VIÊN THỰC HIỆN
- Huỳnh Nguyễn Ngọc Tân

5. HƯỚNG DẪN CHẠY THỬ
Folder project tên: StudentManagement 
Trong folder có chứa folder src chứa tất cả module và hàm main 
1. Mở project bằng Visual Studio 
2. Mở terminal và đứng ở thư mục StudentManagement 
3. Nhập câu lệnh ( python -m src ) để chạy
4. Màn hình sẽ hiển thị thông tin điểm và GPA của sinh viên
