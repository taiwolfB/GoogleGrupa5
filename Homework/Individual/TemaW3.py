def sum_params(*args, **kwargs):
    sum = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            sum += arg
    return sum


# print(sum_params(2, 4, 'abc', param_1=2))


# sum of all, sum of all even, sum of all odd
def recursive_sums(number,returnVals):
    if number != 0:
        if number % 2 == 0:
             return recursive_sums(number-1,[returnVals[0] + number, returnVals[1] + number, returnVals[2]])
        else:
             return recursive_sums(number-1,[returnVals[0] + number, returnVals[1], returnVals[2] + number])
    else:
        return returnVals

# print(recursive_sums(5,[0,0,0]))

def check_input_int():
    value = input()
    try:
        return int(value)
    except ValueError:
        return 0

print(check_input_int())
