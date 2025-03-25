number_sequence = [
    int(num)
    for num in input("Введите последовательность чисел через пробел:\n").strip().split()
]

odd_count = 0
div_3_not_5_count = 0
odd_value_count_even_index = 0

for i, num in enumerate(number_sequence):
    if num % 2 == 1:
        odd_count += 1
        if (i + 1) % 2 == 0:
            odd_value_count_even_index += 1
    if num % 3 == 0 and num % 5 != 0:
        div_3_not_5_count += 1

print(
    f"Количество нечетных чисел: {odd_count}\n"
    f"Количество чисел, кратных 3 и не кратных 5: {div_3_not_5_count}\n"
    f"Количество чисел нечетных значений на четных позициях: {odd_value_count_even_index}"
)
