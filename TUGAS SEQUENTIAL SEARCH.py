# Daftar barang elektronik
products = [
    {"id": 1, "name": "Laptop", "harga": 15000000},
    {"id": 2, "name": "Handphone", "harga": 8000000},
    {"id": 3, "name": "Tab", "harga": 5000000},
    {"id": 4, "name": "Camera", "harga": 6000000},
    {"id": 5, "name": "Smartwatch", "harga": 2500000},
]

def sequential_search(products, target_name):
    for product in products:
        if product["name"].lower() == target_name.lower():
            return product
    return None

target_name = input("Masukkan nama barang elektronik yang ingin dicari: ")

# Mencari barang
result = sequential_search(products, target_name)

if result:
    print(f"Barang ditemukan: {result['name']}, Harga: Rp {result['harga']:,}")
else:
    print("Barang tidak ditemukan.")
