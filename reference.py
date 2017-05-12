import numpy
import scipy.special
from random import randint

# neural network class definition
class NeuralNetwork(object):
    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        # learning rate
        self.lr = learningrate
        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # calculate signals into final output laye
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)
        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        pass

    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        return final_outputs



def main():
    nn = NeuralNetwork(1, 2, 1, 0.1)

    # #input data
    # x = numpy.array([[0,0,1],  # Note: there is a typo on this line in the video
    #             [0,1,1],
    #             [1,0,1],
    #             [1,1,1]])


    # # The output of the exclusive OR function follows. 

    # # In[26]:

    # #output data
    # y = numpy.array([[0],
    #              [1],
    #              [1],
    #              [0]])



    # for i in range(60000):
    #     rand = randint(0, 3)
    #     nn.train(x[rand], y[rand])



    # outOne = nn.query([0,0,1])
    # print(outOne)

    # outOne = nn.query([0,1,1])
    # print(outOne)

    # outOne = nn.query([1,0,1])
    # print(outOne)

    # outOne = nn.query([1,1,1])
    # print(outOne)



    for i in range(8000):
        nn.train([9], [0])
        nn.train([3], [1])

    answerOne = nn.query([9])

    print(answerOne)

    answerTwo = nn.query([3])

    print(answerTwo)




if __name__ == "__main__":
    main()