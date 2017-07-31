from operator import mul

def collatz(x, n_list):
  n_list.append(int(x))
  if x == 1:
    return n_list
  elif x % 2 == 0:
    return collatz(x / 2, n_list)
  else:
    return collatz(mul(3, x) + 1, n_list)

def col_chain(x):
  col_numbers = []
  return len(collatz(x, col_numbers))

def count_chain(x):
  current_max_len = 0
  highest_len = 0
  for n in range(1, x + 1):
    if col_chain(n) > current_max_len:
      current_max_len = col_chain(n)
      highest_len = n
  return highest_len

print(count_chain(1000000))
