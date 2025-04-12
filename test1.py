import math
def activasion_function(x) :
    return 1/(1+math.exp(-x))

def sum_of_scales(weights, inputs, bias) :
    sum = 0
    for i in range(len(inputs)) :
        sum+=weights[i]*inputs[i]
    return sum+bias

time_array = [2.57, 4.35, 1.27, 5.46, 1.30, 4.92, 1.31, 4.14, 1.97, 5.67, 0.92, 4.76, 1.72, 4.44, 1.49] 

connections = [1] * 3
bias = 0
neuron = 0

for i in range(len(time_array)-3) :
    a = activasion_function(sum_of_scales(connections,time_array[i: i+3],bias))
    expected_value = time_array[i+3]

    print(a,expected_value)

