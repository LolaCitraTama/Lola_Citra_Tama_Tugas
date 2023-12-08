def contoh_while(numbers):
    index = 0
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            print(f"{numbers[index]} adalah angka genap.")
        else:
            print(f"{numbers[index]} adalah angka ganjil.")
        index += 1


list_angka = [1, 2, 3, 4, 5]

contoh_while(list_angka)
