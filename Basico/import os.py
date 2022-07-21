import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', 'basico')
print(mymodule_dir)
sys.path.append( mymodule_dir )

import Ejercicios_18_Repaso

Ejercicios_18_Repaso.suma([2, 3])