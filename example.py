import SwarmPackagePy
from SwarmPackagePy import testFunctions as tf
from SwarmPackagePy import animation, animation3D
from SwarmPackagePy import aba

aba = aba.aba(100, tf.cross_in_tray_function, -10, 10, 2, 1000)
#animation(aba.get_agents(), tf.cross_in_tray_function, -10, 10)
#animation3D(aba.get_agents(), tf.cross_in_tray_function, -10, 10)

print(aba.get_Gbest())