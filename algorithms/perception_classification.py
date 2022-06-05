import numpy as np 
import matplotlib.pyplot as plt 

class MyPerception:
    def __init__(self):
        # We don't know the dimension of the inputs
        self.weight = None
        self.bias = 0
        self.l_rate = 1

    def fit(self, x_train, y_train):
        # initialize the weight
        # length equals to the number of features
        self.weight = np.zeros(x_train.shape[1])
        i = 0
        while i < x_train.shape[0]:
            x = x_train[i]
            y = y_train[i]

            # update the weights and bias, and the index i returns back to 0
            if y * (np.dot(self.weight, x) + self.bias) <= 0:
                self.weight += self.l_rate * np.dot(y, x)
                self.bias += self.l_rate * y
                i = 0
            else:
                i += 1

def draw(x, weight, bias):
    x_new = np.array([[0], [6]])
    y_new = - bias / weight[1] - weight[0] * x_new / weight[1]
    # plot label 1
    plt.plot(x[:2, 0], x[:2, 1], 'g*', label='A')
    # plot label 2
    plt.plot(x[2:, 0], x[2:, 1], 'r+', label='B')
    # plot the decision line
    plt.plot(x_new, y_new, 'b-')
    plt.axis([0, 6, 0, 6])
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend(loc = 'best')
    plt.show()


def main():
    x_train = np.array([[3, 3], [4, 3], [1, 1]])
    y_train = np.array([1, 1, -1])
    perception = MyPerception()
    perception.fit(x_train, y_train)
    print(perception.weight)
    print(perception.bias)

    draw(x_train, perception.weight, perception.bias)

if __name__ == '__main__':
    main()