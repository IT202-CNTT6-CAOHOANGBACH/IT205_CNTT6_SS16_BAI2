'''
    - Dòng new_prescription = old_prescription không tạo ra một bản sao mới, mà chỉ tạo thêm một “nhãn” trỏ đến cùng vùng nhớ. Do đó, bất kỳ thay đổi nào trên new_prescription 
    cũng đồng thời tác động lên old_prescription
    - Để thực sự tạo ra một "bản sao" (copy) độc lập của List mà không ảnh hưởng đến List gốc, ta có thể dùng những cách:
        + Dùng copy() → new_prescription = old_prescription.copy()
        + Dùng slicing → new_prescription = old_prescription[:]

    - Lệnh new_prescription[0].replace("Panadol", "Paracetamol") không có tác dụng vì
    replace() trả về một chuỗi mới, nhưng lập trình viên không gán lại kết quả đó vào 
    phần tử list. Chuỗi trong list vẫn giữ nguyên.
    - Cú pháp đúng để cập nhật phần tử: 
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
'''

# sửa lỗi
# Danh sách thuốc ngày hôm qua (Lịch sử bệnh án cần giữ nguyên)
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

# Hàm tạo và cập nhật đơn thuốc cho ngày mới
def update_prescription(old_prescription):
    # Tạo bản sao độc lập của đơn thuốc hôm qua
    new_prescription = old_prescription[:]
    
    # Đổi tên thuốc ở vị trí đầu tiên từ Panadol thành Paracetamol
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    
    # Thêm thuốc mới cho ngày hôm nay
    new_prescription.append("Oresol")
    
    return new_prescription

# Hệ thống chạy cấp thuốc cho ngày hôm nay
today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)