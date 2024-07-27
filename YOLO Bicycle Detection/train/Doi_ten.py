import os

# Đường dẫn tới thư mục chứa các tệp ảnh
folder_path = r"D:\THUC TAP NGOAI TRUONG\YOLO Bicycle Detection\train\images"

# Khởi tạo biến đếm
count = 1

# Duyệt qua tất cả các tệp trong thư mục
for filename in os.listdir(folder_path):
    
    # Tạo tên tệp mới
    new_filename = f"{count}.jpg"
    
    # Tạo đường dẫn đầy đủ tới tệp cũ và tệp mới
    old_file_path = os.path.join(folder_path, filename)
    new_file_path = os.path.join(folder_path, new_filename)
    
    # Đổi tên tệp
    os.rename(old_file_path, new_file_path)
    
    # Tăng biến đếm
    count += 1

print("Đổi tên hàng loạt hoàn tất.")
