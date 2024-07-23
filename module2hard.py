def password (number):
    code = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                code += str(i) + str(j)
    return code

print('введите число от 3 до 20:')
print(password(int(input())))
















