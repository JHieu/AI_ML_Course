from ultralytics import YOLO
import cv2

# Tải mô hình YOLOv8 đã được huấn luyện
model = YOLO(r'D:\THUC TAP NGOAI TRUONG\YOLO Bicycle Detection\train\weights\best.pt')

# Đường dẫn đến hình ảnh trên máy tính
image_path = r'D:\THUC TAP NGOAI TRUONG\YOLO Bicycle Detection\train\images\bicycle5.jpg'  # Thay đổi đường dẫn này tới hình ảnh của bạn

# Đọc hình ảnh
image = cv2.imread(image_path)

# Kiểm tra xem hình ảnh có được đọc thành công không
if image is None:
    print(f"Không thể đọc hình ảnh từ {image_path}")
    exit()

# Danh sách các nhãn lớp (có thể cần thay đổi theo nhãn lớp của bạn)
class_names = ["Bicycle", "Other"]  # Thay thế bằng các nhãn lớp của bạn

# Phát hiện đối tượng trong hình ảnh
results = model(image)

# Vẽ bounding box và nhãn lên hình ảnh
for result in results:
    for box in result.boxes:
        # Chuyển đổi tensor thành các giá trị int
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        confidence = float(box.conf[0])  # Sử dụng thuộc tính `conf` để lấy điểm tin cậy
        label_idx = int(box.cls[0])  # Sử dụng thuộc tính `cls` để lấy nhãn lớp
        label = class_names[label_idx]  # Lấy tên nhãn từ danh sách nhãn lớp
        
        # Vẽ bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Ghi tên nhãn và điểm tin cậy lên hình ảnh
        text = f'{label} {confidence:.2f}'
        cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Hiển thị hình ảnh với các bounding box và nhãn
cv2.imshow('YOLOv8 Detection', image)

# Nhấn bất kỳ phím nào để thoát
cv2.waitKey(0)
cv2.destroyAllWindows()
