import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D


aba = SwarmPackagePy.aba(50, tf.easom_function, -10, 10, 2, 20)
animation(aba.get_agents(), tf.easom_function, -10, 10)
animation3D(aba.get_agents(), tf.easom_function, -10, 10)

