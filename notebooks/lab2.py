
# coding: utf-8

# In[17]:

import tensorflow as tf
import numpy as np


# Tensor
# - tf.zeros(10)
# - tf.constant([[1,2],[3,4]])
# 
# Graph
# - obsahuje Tensory ~ operace
# 
# Session
# - obsahuje Grafy
# - obsahuje promenne
# 
# Variable
# - tf.Variable(tf.ones([10]))
# 
# ts.initialize_all_variables() - prida operaci co inicializuje vsechny promenne

# In[3]:

s = tf.Session()
i = tf.initialize_all_variables()


# In[9]:

tf.get_default_graph().as_graph_def()


# In[21]:

i = tf.placeholder(shape=[None,10], dtype=tf.int8)
d = i*i
s.run(d, feed_dict={i:(np.ones([3,10])*2)})


# tf.scalar_summary("acc", accuracy)

# du hyperparam search
# - pocet vrste 1..3
# - aktivacni fce: tanh, relu
# - provest spravne validaci
# - NE velikost skrytych vrstev

# In[ ]:



