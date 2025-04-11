import math

class Neuron_network :
    def __init__(self, input_array) :
        self.network = {"input" : input_array}
        self.layer_count = 0
    
    def add_layer(self, neuron_count) :
        self.layer_count += 1
        self.add_to_network_dict("layer",self.layer_count,[None]*neuron_count)
        self.add_to_network_dict("bias",self.layer_count,[0]*neuron_count)

        if self.layer_count == 1 :
            neuron_count_of_previus_layer = len(self.network["input"])
        else :
            neuron_count_of_previus_layer = len(self.get_from_network_dict("layer",1)) 
        self.add_to_network_dict("connection",self.layer_count,[[1]*neuron_count_of_previus_layer]*neuron_count)

    
    def add_to_network_dict(self,type_of_input, number_of_input, input) :
        self.network[type_of_input+"-"+str(number_of_input)] = input

    def get_from_network_dict(self,type_of_output,number_of_output) :
        try:
            return self.network[type_of_output+"-"+str(number_of_output)]
        except KeyError :
            return None
        
    def calculate_neuron_output(self,inputs, coefficients, bias) :
        sum = 0
        for i in range(len(inputs)) :
            sum += inputs[i]*coefficients[i]
        sum+=bias
        return sum

    def activasion_function(x) :
        return 1/(1+math.exp(-x))
    
    def calculate_network_output(self) :
        i = 1 
        if not self.get_from_network_dict("layer",i) :
            print("Пуста мережа, потрібно хоча б один шар нейронів.")
            exit(0)
        while self.get_from_network_dict("layer",i) :
            if i == 1 :
                previus_layer = self.network["input"]
            else :
                previus_layer = self.get_from_network_dict("layer",i-1)
            
            for j in range (len(self.get_from_network_dict("layer",i))) :
                connection = self.get_from_network_dict("connection",i)[j]
                bias = self.get_from_network_dict("bias",i)[j]
                self.network["layer-"+str(i)][j] = self.calculate_neuron_output(previus_layer, connection, bias)
            
            i+=1

time_array = [2.57, 4.35, 1.27, 5.46, 1.30, 4.92, 1.31, 4.14, 1.97, 5.67, 0.92, 4.76, 1.72, 4.44, 1.49] 
net = Neuron_network(time_array[:3])
net.add_layer(1)
net.calculate_network_output()
print(net.network)