# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for a,b in cars.iterrows():
    print(a)
    print(b)
    
# Adapt for loop
for lab, row in cars.iterrows() :
    print(row['country']+": "+ str(row['cars_per_cap']))
    print(lab+": "+ str(row['cars_per_cap']))
