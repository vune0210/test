import json

# Đọc nội dung từ tập tin JSON
with open('readfile.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Hiển thị thông tin từ JSON
print("Họ và tên:", data["ho_ten"])
print("Tuổi:", data["tuoi"])
print("Giới tính:", data["gioi_tinh"])
print("Địa chỉ:")
print("  Xã:", data["dia_chi"]["xa"])
print("  Huyện:", data["dia_chi"]["huyen"])
print("  Tỉnh:", data["dia_chi"]["tinh"])
print("  Quốc gia:", data["dia_chi"]["quoc_gia"])
print("Email:", data["email"])
print("Số điện thoại:", data["so_dien_thoai"])
print("Sở thích:")
for so_thich in data["so_thich"]:
    print("  Tên:", so_thich["ten"])
    print("  Mức độ:", so_thich["muc_do"])
    print()



