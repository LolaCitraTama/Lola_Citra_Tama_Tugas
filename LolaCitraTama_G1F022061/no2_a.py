def contoh(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} adalah angka genap.")
        else:
            print(f"{num} adalah angka ganjil.")


list_angka = [1, 2, 3, 4, 5]

contoh(list_angka)
