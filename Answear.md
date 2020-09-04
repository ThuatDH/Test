## Q1. What is the difference between list and tuples in Python?
1. List : là một collection có thứ tự, có thể thay đổi. Cho phép chứa dữ liệu trùng lặp.
2. Tuple : là một collection có thứ tự, không thể thay đổi. Cho phép chứa dữ liệu trùng lặp.
## Q2. What are the key features of Python?
* Easy to learn.
* Supports quick development.
* Cross-platform.
* Open Source.
* Extensible.
* Embeddable.
* Large standard library and active community.
* Useful for a wide variety of applications.  
## Q3. What type of language is python?
* Python là ngôn ngữ lập trình với đối tượng, mô-đun, luồng, ngoại lệ và quản lý bộ nhớ tự động
## Q4. How is Python an interpreted language?
* Ngôn ngữ Python là một ngôn ngữ thông dịch. 
* Chương trình Python chạy trực tiếp từ mã nguồn. 
* Nó chuyển đổi mã nguồn được lập trình viên viết thành ngôn ngữ trung gian, sau đó một lần nữa được dịch sang ngôn ngữ máy để thực thi.
## What is pep 8?
* PEP 8 là một quy ước cách viết mã nguồn, một bộ khuyến nghị về cách viết mã Python để chúng dễ đọc hơn.
* Được viết năm 2001 bởi Guido van Rossum, Barry Warsaw, và Nick  Coghlan
## Q6. How is memory managed in Python?
* Bộ nhớ Python được quản lý bởi không gian heap riêng của Python. Tất cả các đối tượng Python và cấu trúc dữ liệu được đặt trong một heap riêng. Lập trình viên không có quyền truy cập vào heap riêng này và trình thông dịch của Python sẽ quản lý heap riêng này.
* Việc phân bổ không gian heap của Python cho các đối tượng được thực hiện bởi trình quản lý bộ nhớ Python. API lõi cung cấp quyền truy cập vào một số công cụ để lập trình viên viết mã.
* Python cũng có một trình thu gom rác sẵn có, giải phóng tất cả bộ nhớ không sử dụng và giúp không gian heap có thể sử dụng bộ nhớ này.
## Q7. What is name space in Python?
* Trong Python, mỗi tên được khai báo đều có một ví trí để lưu trữ và tìm kiếm. Nó được gọi là không gian tên (namespace). 
* Nó giống như một chiếc hộp nơi tên biến được ánh xạ tới vị trí lưu đối tượng. 
* Bất cứ khi nào biến được tìm kiếm, chiếc hộp này cũng sẽ được tìm để trả lại đối tượng tương ứng.
## Q8. What is PYTHON PATH?
* PYTHON_PATH là một danh sách các thư mục nơi mà Python sẽ tìm kiếm các modules khi bạn sử dụng lệnh import (VD: import os, import sys, …)
## Q9. What are python modules?
* Trong Python, mô-đun là cách để tổ chức chương trình. Mỗi tệp chương trình Python là một mô-đun, một mô-đun có thể nạp các mô-đun khác giống như một đối tượng hoặc thuộc tính.
* Thư mục của chương trình Python là một gói các mô-đun. Một gói có thể có các mô-đun hoặc thư mục con.
## Q10. What are local variables and global variables in Python? Please give an exam
* Global variable là variable mà bạn có thể access ở mọi lúc, mọi nơi
* Local variable là variable mà chỉ accessible trong phạm vi function của nó
* Ví dụ: 
""" python
my_var = 'global'
def call_me_1():
    print(f'call_me_1: {my_var}')
def call_me_2():
    my_var = 'local'
    print(f'call_me_2: {my_var}')
if __name__ == '__main__':
    call_me_1()
    call_me_2()
    print(f'__main__: {my_var}')
"""
## Q11. What is __init__?
* __init__ là hàm dựng hay constructor của một class. Khi một thực thể (instance) của một class được tạo ra thì hàm này sẽ được thực thi đầu tiên và một cách tự động
## Q12. What is self in Python?
* Các tham số self là tham chiếu đến lớp chính nó, và được sử dụng để truy cập các biến đó thuộc về lớp.