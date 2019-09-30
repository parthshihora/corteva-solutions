final_product = 1
current_product = 1
current_count = 1
with open('number.txt') as number_file:
    number_to_divide = []
    i = 0
    for line in number_file:
        for c in line:
            if c != '\n' and current_count <= 8:
                if int(c) != 0:
                    current_product = current_product * int(c)
                    number_to_divide.append(int(c))
                    current_count += 1
                else:
                    current_product = 1
                    current_count = 1
                    number_to_divide = []
                    i = 0

            else:
                if c != '\n' and int(c) != 0:
                    if current_product >= final_product:
                        final_product = current_product
                    current_product = (current_product // number_to_divide[i]) * int(c)
                    number_to_divide.append(int(c))
                    i += 1
                elif c != '\n' and int(c) == 0:
                    number_to_divide = []
                    i = 0
                    current_count = 1
                    current_product = 1


if current_product > final_product:
    print('Answer:', current_product)
else:
    print('Answer', final_product)

