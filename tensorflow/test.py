import tensorflow as tf
rank1_tensor = tf.Variable(['lol', 'ok', 'okayy'], tf.string)
rank2_tensor = tf.Variable([['lol'], ['okay']], tf.string)

print(tf.rank(rank2_tensor))
