def binary_search(arr, x):

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # jika elemen berasa ditengah
        if arr[mid] < x:
            low = mid + 1

        # jika elemen barada disebelah kiri tengah
        elif arr[mid] > x:
            high = mid - 1

        # elemen ditemukan
        else:
            return mid
        
    # elemen tidak ditemukan
    return -1

def main():
    # Menerima input daftar elemen yang sudah terurt dari pengguna
    arr = list(map(int, input("Masukkan daftar elemen yang sudah terurut (pisahkan dengan spasi): ").split()))

    #Menerima input elemen yang akan dicari
    x = int(input("Masukkan elemen yang akan dicari: "))

    result = binary_search(arr, x)

    if result != -1:
        print(f"Elemen ditemukan pada indeks {result}")
    else:
        print("Elemen tidak ditemukan dalam daftar")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()