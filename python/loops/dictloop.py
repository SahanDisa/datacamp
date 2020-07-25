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

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = len(row['country'])
    cars.loc[lab, "mycolumn"] = row['cars_per_cap']*len(row['country'])


# Print cars
print(cars)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    #cars.loc[lab, "COUNTRY"] = row["country"].upper()\
    cars["COUNTRY"] = cars["country"].apply(str.upper)
