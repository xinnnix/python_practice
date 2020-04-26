import tensorflow as tf

# input > weight > hidden layer 1 (activation function) > weights > hidden layer 2
# (activation function) > weights > output layer

# compare output to intended output > cost or lost function (cross entrophy)
# optimization function (optimizer) > minimize cost (AdamOptimizer...SGD, AdaGrad)

# backpropagation

# feed forward + backprop = epoch

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100

#height * width
x = tf.placeholder('float', [None, 784])
y = tf.placeholder('float')


def neural_network_model(data):

    # (input_data * weights) + biases

    hidden_1_layer = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases': tf.Variable(tf.random_normal(n_nodes_hl1))}
