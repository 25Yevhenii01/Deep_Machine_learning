import numpy as np
#perceptron realization
def sigmoid(x): #function for activation
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([#input data
    [0,0,1],
    [1,1,1],
    [1,0,1],
    [0,1,1]
])

training_outputs = np.array([[0,1,1,0]]).T#transpose array - ouput data

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1

print("Random initialization weights:")
print(synaptic_weights)

#backpropagation
for i in range(20000):
    input_layer = training_inputs
    outputs = sigmoid( np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
    adjustments = np.dot( input_layer.T, err * (outputs * (1 - outputs)) )

    synaptic_weights += adjustments

print("Weights after trainings: ")
print(synaptic_weights)

print("Result: ")
print(outputs)

#test
new_inputs = np.array([0,0,1])
outputs = sigmoid( np.dot(new_inputs, synaptic_weights))

print("New: ")
print(outputs)
