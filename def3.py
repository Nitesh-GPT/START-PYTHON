def sum_digits(s):
    total = 0
    for char in s:
      if char in "0123456789":
        val = int(char)
        total += val
    return total
print(sum_digits("1234abc"))