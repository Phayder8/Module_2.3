my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
while x < len(my_list):
    n = my_list[x]
    x = x + 1
    if n == 0:
        continue
    elif n < 0:
        break
    else:
        print(n)