import tensorflow as tf

# x1 = tf.constant(5)
# x2 = tf.constant(6)
#
# result = tf.multiply(x1, x2)
#
# # result = x1 * x2
# print(result)


with tf.compat.v1.Session() as sess:
    x1 = tf.constant(5)
    x2 = tf.constant(6)

    result = tf.multiply(x1, x2)
    output = sess.run(result)
    print(output)

# session graph empty problem....
