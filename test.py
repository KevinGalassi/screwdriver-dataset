import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = '/home/kvn/Documents/dataset_screwdriver/SCREWING/ok/'
file_name = file_path + '13_53_force_reading'+ '.csv'
sns.set_theme(style="whitegrid")


data = pd.read_csv(file_name)

data['Time'] = data["Time"].subtract(data['Time'][0])

#sns.scatterplot(data=data, x='Time', y='Fz')

sns.lineplot(x="Time", y="Fz", data=data, linewidth='2')







fail = '/home/kvn/Documents/dataset_screwdriver/SCREWING/Fail/13_32_force_reading.csv'
data = pd.read_csv(fail)

data['Time'] = data["Time"].subtract(data['Time'][0])

sns.lineplot(x="Time", y="Fz", data=data, color='r', linewidth='2')



missed = '/home/kvn/Documents/dataset_screwdriver/SCREWING/no_activation/13_8_force_reading.csv'
data = pd.read_csv(missed)
data['Time'] = data["Time"].subtract(data['Time'][0])

ax = sns.lineplot(x="Time", y="Fz", data=data, color='g', linewidth='2')

ax.set_xlabel('Time')
ax.set_ylabel('Fz')

plt.xlim(0, 6)
plt.title('Force Monitoring')

plt.show()