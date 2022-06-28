# Code đồ án môn học Trí tuệ nhân tạo

## Các thư viện được sử dụng

- keras
- numpy
- matplotlib
- tkinter
- pillow
- win32gui

## File train_digit_recognizer
- Dữ liệu được load sử dụng hàm load_data(): mnist.load_data()
- Hàm preprocess_data:
    - Chức năng: xử lý dữ liệu trước khi sử dụng.
    - Input: tập dữ liệu test và train.
    - Output: dữ liệu đã được đưa về dạng chuẩn có thể sử dụng bởi thư viện Keras.
- Hàm LeNet:
    - Chức năng: tạo ra model
    - Input: void
    - Output: model có đầy đủ các lớp yêu cầu
- Hàm train_model:
    - Chức năng: huẩn luyện mô hình, vẽ biểu đồ
    -  Input: model; tập dữ liệu huẩn luyện, kiểm tra; số lần huấn luyện - epoch; batch-size
    - Output: void
- Hàm summary_history:
    - Chức năng: Vẽ biểu đồ thể hiện Accuracy của mô hình sau khi huẩn luyện.
- Mô hình sau khi được huấn luyện sẽ được lưu vào file **handwriting.h5**

## File gui_digit_recognizer
- Chức năng: 
    - tạo 1 ứng dụng nhỏ để ứng dụng model này trong thực tế.
- Class App:
    - Chức năng: xây dựng 1 giao diện cho ứng dụng.
    - GUI bao gồm: 
        - 1 vùng canvas để viết chữ số.
        - Nút Clear.
        - Nút Recognize.
- Hàm predict_digit:
    - Chức năng: dự đoán số được vẽ trên giao diện là số nào.
    - Input: ảnh chụp số được vẽ trên giao diện
    - Output: số được dự đoán và độ chính xác.