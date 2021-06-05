
from typing import List, Tuple

import numpy as np

# input_size = 2 # wejscie
# hidden_size = 10 # wielkosc ukrytej warstwy
# output_size = 1

iterations = 50 # iteracje

alpha = 0.0001

data = np.array([ # dane wejsciowe
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

labels = np.array([0, 1, 1, 0]) # zalozone wyjscie


class NeuralNetwork:
    def __init__(self, hidden_sizes: List[int], output_size: int, input_size: int) -> None:


        self.weights = []  # inicjujemy wagi sieci dla warstw ukrytych
        self.layers = []  # umieszczamy wartosci znajdujace sie w poszczegolnych ukrytych warstwach sieci
        self.weights.append(np.random.random_sample((input_size, hidden_sizes[0]))) # wagi miedzy wejsciem a 1. warstwa ukryta

        for i in range(len(hidden_sizes) - 1):
            self.weights.append(np.random.random_sample((hidden_sizes[i], hidden_sizes[i+1]))) # wagi miedzy warstwami ukrytymi
        self.weights.append(np.random.random_sample((hidden_sizes[-1], output_size))) # wagi miedzy ostatnia warstwa ukryta a wyjsciem

    def predict(self, input_: np.ndarray) -> np.ndarray:
        # zwracamy wartosci znajdujace sie w ostatniej warstwie sieci
        return self.layers[-1]

    def fit(self, data: np.ndarray, labels: np.ndarray, iterations: int, alpha: float) -> float:
        # zwracamy wartosc bledu treningu
        for _ in range(iterations):
            error = 0.0
            correct_count = 0

            for i in range (len(data)): # petla dzialajaca po dlugosci data(wejscia)
                self.layers.clear() # czyszczenie wag
                self.layers.append(data[i:i+1].dot(self.weights[0])) # iloczyn skalarny miedzy wejscie i 1. waga
                for j in range(len(self.weights) - 1):
                    self.layers.append(self.layers[j].dot(self.weights[j+1])) # iloczyn skalarny miedzy kolejnymi warstwami a wagami
                
                output = self.predict(data) # wyjscie
                error += np.sum((labels[i] - output) ** 2) # wyliczenie erroru
                correct_count += int(output == labels[i]) # wyliczenie correct_count
                delta = labels[i] - output # wyliczenie delty(gradient)
                # print('Error: ', error)
                
                for k in range(len(self.weights) -1 , 0, -1): # nauczenie wag backtrace
                   self.weights[k] += alpha * self.layers[k - 1].T.dot(delta)
                   delta = delta.dot(self.weights[k].T)
                
                self.weights[0] += alpha * data[i:i+1].T.dot(delta) # wyuczenie 1. wag
            print('Error: ', error)
            

neural = NeuralNetwork([4,8,8,8], 1, 2)
neural.fit(data,labels, iterations, alpha)