import numpy as np
import tensorflow as tf


a=np.array([5]）
b=np.array([3])
c=tf.add(a,b)

sess=tf.Session()
sess.run(init)
sess.run(c)
print(c)
