
expenseReport = []
with open("./input1.txt", "r") as f:
    for line in f: 
        expenseReport.append(int(line))


def find_terms(the_list, the_value):
    for first_term in the_list:
        second_term = the_value - first_term
        if second_term in the_list:
            return first_term, second_term

def find_terms_recursive(the_list, the_value):
    if len(the_list) < 2:
        return None
    if len(the_list) == 2:
        return the_list[0], the_list[1]
   


(first, second) = find_terms(expenseReport, 2020)
print(f'The first answer is: {first} * {second} = {first * second}')



small_list = list(filter(lambda x: x < 1200, expenseReport))
print(small_list)
for i, s in enumerate(small_list):
    print(f'{s} {find_terms(small_list, 2020 - small_list[i])}')
