import numpy as np
import pandas as pd
import sys
import glob
import os

phase_types = ['screwing', 'unscrewing']
results_types = ['ok', 'fail', 'misfire']
data_types = ['force', 'position']
base_path = 'dataset'

# Panda dataset Creation

file_list = []

force_list = []
pose_list = []


for phase in phase_types :
   for result in results_types :
      for data_type in data_types :
         l = glob.glob(os.path.join(base_path, phase, result, data_type, '*.csv' ))
         if len(l) == 0 :
            pass
         else :
            if data_type == 'force' :
               for file in l :
                  force_list.append(file)
            if data_type == 'position' :
               for file in l :
                  force_list.append(file)




df = pd.DataFrame(columns=['Time', 'Fx', 'Fy', 'Fz','Cx', 'Cy', 'Cz', 'test'])
for i, file in enumerate(force_list) :
   new_df = pd.read_csv(file)
   new_df["Time"] = new_df["Time"].subtract(new_df['Time'][0])
   new_df['test'] = i
   df.append(new_df)

