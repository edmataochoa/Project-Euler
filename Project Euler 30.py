def list_to_num(num):
    return [n for n in str(num)]

def sum_powers(num, pow):
    total = 0
    for n in range(num + 1):
        total += (n ** pow)
    return total

def total_sum(num):
    lst = list_to_num(num)
    total = 0
    for n in lst:
        total += int(n)
    return total

def pow_plus_sum(num, pow):
    return total_sum



print(total_sum(234))
