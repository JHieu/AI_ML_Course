from PIL import Image
import os

source_folder = 'D:\THUC TAP NGOAI TRUONG\YOLO Bicycle Detection\train\images'
destination_folder = 'S:/BKU/Thuctap/yolov8/coco128/images/train2017/'      # Source muon luu vao

directory = os.listdir(source_folder)
print(directory)

for item in directory:
    img = Image.open(source_folder + item)
    width, height = img.size
    if width >= height:
        ratio = width/height
        new_width = 640
        new_height = int(new_width/ratio)
    elif width < height:
        ratio = height/width
        new_height = 640
        new_width = int(new_height/ratio)
    imgResize = img.resize((new_width, new_height), Image.LANCZOS)
    imgResize.save(destination_folder + item[:-4] + '.jpg', quality = 100)
    