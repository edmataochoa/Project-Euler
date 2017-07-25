large_num = open("p013_large_num.txt", "r").read()

def first_digits_sum(num):
    total = 0
    current_num = ""
    for digit in str(num):
        current_num += digit
        if digit == "\n":
            total += int(current_num)
            current_num = ""

    def how_many_digits(quantity):
        return str(total)[0:quantity]

    return how_many_digits

one_hundred_fifty_num = first_digits_sum(large_num)
print(one_hundred_fifty_num(10))
