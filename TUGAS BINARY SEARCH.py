def binary_search(motor_list, target_price):
    low = 0
    high = len(motor_list) - 1

    while low <= high:
        mid = (high + low) // 2

        # Jika harga motor di tengah lebih kecil dari target, abaikan bagian kiri
        if motor_list[mid]["price"] < target_price:
            low = mid + 1

        # Jika harga motor di tengah lebih besar dari target, abaikan bagian kanan
        elif motor_list[mid]["price"] > target_price:
            high = mid - 1

        else:
            return mid
        
    return -1

def main():
    # Daftar motor yang sudah diurutkan berdasarkan harga
    motor_list = [
        {"id": 1, "name": "Beat", "price": 16000000},
        {"id": 2, "name": "Mio", "price": 17000000},
        {"id": 3, "name": "Scoopy", "price": 18000000},
        {"id": 4, "name": "Vario", "price": 24000000},
        {"id": 5, "name": "NMAX", "price": 30000000},
    ]

    try:
        target_price = int(input("Masukkan harga motor yang akan dicari: "))
    except ValueError:
        print("Harap masukkan angka yang valid.")
        return

    result = binary_search(motor_list, target_price)

    if result != -1:
        motor = motor_list[result]
        print(f"Motor ditemukan: {motor['name']}, Harga: Rp {motor['price']:,}")
    else:
        print("Motor dengan harga tersebut tidak ditemukan.")

if __name__ == "__main__":
    main()
