
import numpy as np
import pandas as pd
import sys
import glob
import os

def csv_elaboration(phase_types, results_types,data_types, base_path ) : 

   force_df = pd.DataFrame()
   pos_df = pd.DataFrame()

   test_counter = 0
   for phase in phase_types :
      for result in results_types :
         for data_type in data_types :
            l = glob.glob(os.path.join(base_path, phase, result, data_type, '*.csv' ))
            if len(l) == 0 :
               pass
            else :
               for i, file in enumerate(l) :
                  new_df = pd.read_csv(file)
                  new_df["Time"] = new_df["Time"].subtract(new_df['Time'][0])
                  new_df['test'] = test_counter
                  test_counter += 1
                  print(test_counter)
                  new_df['phase'] = phase
                  new_df['result'] = result
                  if data_type == 'force' :
                     force_df = pd.concat([force_df, new_df], ignore_index=True)
                  if data_type == 'position' :
                     pos_df = pd.concat([pos_df, new_df], ignore_index=True)

   print('{} test loaded'.format(test_counter))

   return force_df, pos_df, test_counter
