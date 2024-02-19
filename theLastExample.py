largest = None
smallest = None

while True:
    num_input = input("Введіть число: ")

    if num_input.lower() == "готово":
        break

    try:
        num = int(num_input)
    except ValueError:
        print("Некоректний ввід. Будь ласка, введіть ціле число або 'готово'.")
        continue

    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

if largest is not None:
    print("Найбільше число:", largest)
if smallest is not None:
    print("Найменше число:", smallest)
