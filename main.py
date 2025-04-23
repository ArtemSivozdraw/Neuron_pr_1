import math
import matplotlib.pyplot as plt

def activasion_function(x):
    return 6 / (1 + math.exp(-x))

def diff_activasion_function(x):
    s = activasion_function(x) / 6
    return 6 * s * (1 - s)

def sum_of_scales(weights, inputs, bias):
    return sum(w * x for w, x in zip(weights, inputs)) + bias

time_array = [2.57, 4.35, 1.27, 5.46, 1.30, 4.92, 1.31, 4.14, 1.97, 5.67, 0.92, 4.76, 1.72, 4.44, 1.49]

propagation_speed = 0.001
connections = [-0.48243474657619106, -0.5610720245678693, -0.8792767556275607]
bias = 6.328349459611023

cost_history = []
bias_history = []
weight_history = [[] for _ in range(3)]

epoch = 10000
for current in range(epoch):
    avarage_cost = 0
    avarage_connection_update = [0.0] * 3
    avarage_bias_update = 0.0
    cycle_counter = 0

    for i in range(len(time_array) - 5):
        inputs = time_array[i:i+3]
        s = sum_of_scales(connections, inputs, bias)
        a = activasion_function(s)
        expected_value = time_array[i + 3]

        cost = (expected_value - a) ** 2
        cost_delta = 2 * (expected_value - a)
        output_delta = diff_activasion_function(s)
        bias_delta = cost_delta * output_delta

        for k in range(3):
            avarage_connection_update[k] += bias_delta * inputs[k]
        avarage_bias_update += bias_delta
        avarage_cost += cost
        cycle_counter += 1

    bias += propagation_speed * (avarage_bias_update / cycle_counter)
    for i in range(3):
        connections[i] += propagation_speed * (avarage_connection_update[i] / cycle_counter)

    cost_history.append(avarage_cost / cycle_counter)
    bias_history.append(bias)
    for i in range(3):
        weight_history[i].append(connections[i])
    
    progres_bar = round(current / epoch * 100,2)
    print("\r",progres_bar, round(avarage_cost / cycle_counter, 2), end=" ")

print()

for i in range(len(time_array)-3) :
    s = sum_of_scales(connections,time_array[i: i+3],bias)
    a = activasion_function(s)
    expected_value = time_array[i+3]

    print(a , expected_value)

print()

print(avarage_cost / cycle_counter)
print(bias,connections)


# --- Побудова графіків ---
fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# Графік помилки
axs[0].plot(cost_history, label="Середня помилка (Cost)", color='blue')
axs[0].set_title("Зміна помилки під час навчання")
axs[0].set_xlabel("Епоха")
axs[0].set_ylabel("Cost")
axs[0].legend()
axs[0].grid(True)

# Графік ваг і bias
axs[1].plot(bias_history, label="Зсув (Bias)", linestyle='--', color='black')
colors = ['red', 'green', 'orange']
for i in range(3):
    axs[1].plot(weight_history[i], label=f"Вага {i}", color=colors[i])
axs[1].set_title("Зміна ваг і зсуву під час навчання")
axs[1].set_xlabel("Епоха")
axs[1].set_ylabel("Значення параметрів")
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()


