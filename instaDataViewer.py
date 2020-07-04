import pandas as pd
import xlrd
from matplotlib import pyplot as plt
import os

os.chdir('C:\\Users\\Shaun\\Desktop\\python practrice') ##change directory to your current working directory


df = pd.read_excel('data.xlsx')
person1 = df[df.Username =='ADD USERNAME HERE'] ##add the username here o plot his data , make sure you have collectedd sufficient data
print(person1)
plt.plot(person1.TimeStamp,person1.Followers)
plt.xlabel('Date')
plt.ylabel('Followers')
plt.show()
