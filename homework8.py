import vat



def get_summ(one, two, delimeter='&'):
    return str(one.upper()) + str(delimeter) + str(two.upper())

sum_string = get_summ("learn","python")
print(sum_string)
