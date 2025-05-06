import numpy as np
import matplotlib.pyplot as plt

# Função de ativação sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada da função sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Classe da Rede Neural Multicamadas
class NeuralNetwork:
    def __init__(self, input_size, hidden_sizes, output_size, learning_rate=0.1, epochs=10000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        layer_sizes = [input_size] + hidden_sizes + [output_size]
        self.weights = [np.random.uniform(-1, 1, (layer_sizes[i], layer_sizes[i+1])) for i in range(len(layer_sizes) - 1)]
        self.mse_por_epoca = []

    def feedforward(self, x):
        activations = [x]
        input = x
        for weight in self.weights:
            net_input = np.dot(input, weight)
            activation = sigmoid(net_input)
            activations.append(activation)
            input = activation
        return activations

    def backpropagation(self, activations, y_true):
        error = y_true - activations[-1]
        deltas = [error * sigmoid_derivative(activations[-1])]
        for i in reversed(range(len(self.weights) - 1)):
            delta = deltas[-1].dot(self.weights[i+1].T) * sigmoid_derivative(activations[i+1])
            deltas.append(delta)
        deltas.reverse()
        for i in range(len(self.weights)):
            layer_input = np.atleast_2d(activations[i])
            delta = np.atleast_2d(deltas[i])
            self.weights[i] += self.learning_rate * layer_input.T.dot(delta)

    def train(self, X, y):
        for epoch in range(self.epochs):
            for xi, yi in zip(X, y):
                activations = self.feedforward(xi)
                self.backpropagation(activations, yi)
            mse = np.mean(np.square(y - self.predict(X)))
            self.mse_por_epoca.append(mse)
            if epoch % 1000 == 0:
                print(f"Época {epoch}, Erro (MSE): {mse:.6f}")

    def predict(self, X):
        return np.array([self.feedforward(xi)[-1] for xi in X])

# Programa principal
if __name__ == "__main__":
    # Dados de entrada (paridade de 3 bits)
    X = np.array([
        [0, 0, 0], [0, 0, 1],
        [0, 1, 0], [0, 1, 1],
        [1, 0, 0], [1, 0, 1],
        [1, 1, 0], [1, 1, 1]
    ])
    
    # Saída desejada: 1 se número ímpar de 1s, 0 se par
    y = np.array([
        [0], [1], [1], [0],
        [1], [0], [0], [1]
    ])
    
    # Testes com diferentes números de neurônios e taxas de aprendizagem
    nn = NeuralNetwork(input_size=3, hidden_sizes=[3], output_size=1, learning_rate=0.2, epochs=3000)
    nn.train(X, y)

    # Resultados
    outputs = nn.predict(X)
    print("\nResultados:")
    for xi, yi_pred in zip(X, outputs):
        print(f"Entrada: {xi}, Saída prevista: {yi_pred.round()}")

    # Plot do erro MSE
    plt.plot(nn.mse_por_epoca)
    plt.title("Erro quadrático médio (MSE) por época")
    plt.xlabel("Época")
    plt.ylabel("MSE")
    plt.grid(True)
    plt.show()

