def sum_of_inputs (inputs) :
    sum = 0
    for i in inputs : 
        sum += i
    return sum


def activation_AND (s) :
    if s == 2 :
        return True
    return False


def activation_OR (s) :
    if s >= 1 :
        return True
    return False


def activation_NO (s) :
    if s == 0 :
        return True
    return False


def activation_XOR (s) :
    if s == 1 :
        return True
    return False


arrays = [[0,0],[1,0],[0,1],[1,1]]

for input in arrays :
    s = sum_of_inputs(input)
    
    print(f"For inputs {input} results : ", end=" ")
    
    print(f" And = {activation_AND(s)}", end="\t")
    print(f" OR = {activation_OR(s)}", end="\t")
    print(f" NO = {activation_NO(s)}", end="\t")
    print(f" XOR = {activation_XOR(s)}")