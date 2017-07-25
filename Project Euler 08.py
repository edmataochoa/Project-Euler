numbers = open("p008_numbers.txt", "r").read()

def multiply_quantity(number):
    list_numbers = [int(n) for n in number if n.isdigit()]

    def get_numbers(num_of_digits):
        count = 0
        total = 0
        current_num = 0
        for n in list_numbers:
            while count < num_of_digits:
                total *= n
                count += 1
            if total > current_num:
                current_num = total
            count = 0
            total = 0
        return current_num

    return get_numbers


multilply_numbers = multiply_quantity(numbers)
print(multilply_numbers(4))
