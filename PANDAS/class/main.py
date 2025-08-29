import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading files e.g csv files 
df = pd.read_csv('titanic_expanded.csv')

print(df.info())

#creating data frames
mydata = {
    'cars': ['benz', 'toyota', 'tesla'],
    'sold': [15, 22, 13]
}

sales = pd.DataFrame(mydata, index=[1, 2, 3])
print(sales.loc[1])


#series
data = [4, 5, 10]

myvar = pd.Series(data, index= ['a', 'b', 'c'])
print(myvar)
print(myvar['c'])


scores = {"day1": 700, "day2": 380, "day3": 390, 'day4': 600, 'day5': 900}

myvar = pd.Series(scores)

print(myvar)

df = pd.read_json('school_data.json')
print(df)

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
    "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
   "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
   "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 

df = pd.read_csv('fitness_data_cleaned.csv')
for x in df.index:
  if df.loc[x, "Pulse"] > 120:
    df.loc[x, "Pulse"] = 120

print(df.corr())


# TODAY
df =pd.read_csv("data.csv")

df.plot()
plt.show()


# Generate some random data
np.random.seed(0)
x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)

# Create the hexbin plot
plt.hexbin(x, y, gridsize=20, cmap='inferno')

# Add a colorbar
plt.colorbar(label='Density')

# Set title and labels
plt.title('Hexbin Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()



ages = [20, 25, 30, 35, 40]
salaries = [30000, 40000, 50000, 60000, 70000]

plt.plot(ages, salaries, marker='+', linestyle='--', color='r')
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Salary vs Age")
plt.show()

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Emma", "Kamsy", "Anaconda", "Michael"],
    "Age": [25, 30, 35, 40, 14, 18, 16],
    "Salary": [50000, 60000, 70000, 80000, 20000, 40000, 35000]
}
df =pd.DataFrame(data)
high_salary =df[df["Salary"] > 55000]
print(high_salary)







