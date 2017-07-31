numbers = open("p008_numbers.txt", "r").read()

list_of_numbers = [int(n) for n in numbers if n.isdigit()]

def get_amount_num(highest_product, amount, num_list):

    if len(num_list) < amount:
        return highest_product

    product = 1
    for n in range(amount):
        product *= num_list[n]

    if product > highest_product:
        highest_product = product

    return get_amount_num(highest_product, amount, num_list[1:])

print(get_amount_num(0, 13, list_of_numbers))
