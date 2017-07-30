numbers = open("p008_numbers.txt", "r").read()

def get_numbers(numbers, amount):
    # list_numbers = [int(n) for n in numbers if n.isdigit()]
    list_numbers = [1, 2, 3]

    highest_total = 0
    current_product = 0
    for n in list_numbers:
        current_product = n
        for m in range(1, amount + 1):
            # print("n = ", n)
            # print("list_numbers.index(n) = ", list_numbers.index(n))
            # print("amount = ", amount)
            print("n = ", n)
            print("m = ", m)
            print(list_numbers[list_numbers.index(n) + m])
            # print("list_numbers.index(n) + amount = ", list_numbers.index(n) + amount)
            if 
                test_var = list_numbers[list_numbers(list_numbers.index(n) + amount)]

        # print(current_product)
        if current_product > highest_total:
            highest_total = current_product

    return highest_total

print(get_numbers(numbers, 2))
