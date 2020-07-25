#np_height and Np-baseball not defined
#add some values
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key,value in europe.items():
    print("the capital of "+key+" is "+value)

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np.nditer(np_height):
    print(str(x)+" inches")

# For loop over np_baseball
for y in np.nditer(np_baseball):
    print(y)
