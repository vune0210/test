import json
# Tạo đối tượng dữ liệu
profile_data = {
    "ho_ten": "Lê Tiến Vũ",
    "tuoi": 21,
    "gioi_tinh": "Nam",
    "dia_chi": {
        "so_nha": "111 Cầu giấy",
        "xa": "Thị trấn HƯng Hóa",
        "huyen": "Quận MNO",
        "tinh": "Thành phố XYZ",
        "quoc_gia": "Việt Nam"
    },
    "email": "nguyenvana@example.com",
    "so_dien_thoai": "0123456789",
    "so_thich": [
        {"ten": "Du lịch", "muc_do": "Cao"},
        {"ten": "Đọc sách", "muc_do": "Trung bình"},
        {"ten": "Chơi thể thao", "muc_do": "Cao"},
        {"ten": "Nghe nhạc", "muc_do": "Cao"}
    ]
}

# Ghi đối tượng JSON vào file
with open('test.json', 'w', encoding='utf-8') as json_file:
    json.dump(profile_data, json_file, ensure_ascii=False, indent=4)

print('File JSON đã được tạo thành công.')
