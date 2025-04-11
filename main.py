import math

class Neuron_network :
    def __init__(self, input_array) :
        self.network = {"input" : input_array}
        self.layer_count = 0
    
    def add_layer(self, neuron_count) :
        self.layer_count += 1
        self.add_to_network_dict("layer",self.layer_count,[None]*neuron_count)
        if self.layer_count == 1 :
            neuron_count_of_previus_layer = len(self.network["input"])
        else :
            neuron_count_of_previus_layer = len(self.get_from_network_dict("layer",1)) 
        self.add_to_network_dict("connection",self.layer_count,[[1]*neuron_count_of_previus_layer]*neuron_count)
    
    def add_to_network_dict(self,type_of_input, number_of_input, input) :
        self.network[type_of_input+"-"+str(number_of_input)] = input

    def get_from_network_dict(self,type_of_output,number_of_output) :
        return self.network[type_of_output+"-"+str(number_of_output)]
    
    def calculate_neuron_output(inputs, coefficients) :
        sum = 0
        for i in range(len(input)) :
            sum += inputs[i]*coefficients[i]
        return sum

    def activasion_function(x) :
        return 1/(1+math.exp(-x))
    
    

time_array = [2.57, 4.35, 1.27, 5.46, 1.30, 4.92, 1.31, 4.14, 1.97, 5.67, 0.92, 4.76, 1.72, 4.44, 1.49] 
net = Neuron_network(time_array[:3])
net.add_layer(2)
print(net.network)