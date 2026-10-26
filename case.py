#write your code here
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')

df['math score'].plot(kind = 'hist', bins = 5)
plt.show()

as
