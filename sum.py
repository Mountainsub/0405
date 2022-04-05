
import pandas as pd
import numpy as np
import time 
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import random
import math
import datetime

from lib.ddeclient import DDEClient
from price_logger import ClientHolder 
from price_logger import LastNPerfTime


class tameru:
    def __init__(self):
        self.hdffilename = "./data/sum.hdf5"
        self.store = pd.HDFStore(self.hdffilename)
        self.key_name = "testcase" 
        self.key_name2 = "timecase"

    def hozon(self, data_dict):
        #print("OK")
        self.store.append(self.key_name, data_dict)

    def hozon2(self, data_dict):
        #print("OK")
        self.store.append(self.key_name2, data_dict)
      


if __name__ == "__main__":
    t1 = time.time()
    calc = 0
    timer = LastNPerfTime(2**20)
    object_pass = "value"
    

    while True:
        holder = tameru()
        
        timer.start()
        calc = 0
        x = 1
        for i in range(18):
            idx = i *126
            filename = "./data/" + str(idx).zfill(3)+ ".hdf5"
             
            try:
                with pd.HDFStore(filename) as store:
                    temp =store.get(object_pass)
            except:
                pass
            else:
                end = temp.tail(1)
                v = float(end["0"])
                while v==0:
                    now = datetime.datetime.now()
                    print(i, "attention", now)
                    with pd.HDFStore(filename) as store:
                        store.append("zero",pd.DataFrame({"caution":[now]})) 
                    x += 1
                    v = temp.tail(x)
                else:
                    print(i, "threw")
                    x = 1
                calc += v
            
        
        dict = {"total": [calc]}
        timer.end()
                
        series = pd.DataFrame(dict)

        holder.hozon(series)
        temp = timer.get_sum_time()    
        dict = {"time": [temp]}
        df = pd.DataFrame(dict)
        holder.hozon2(df)   
        timer.count_one()
        
    
        print("取得時間:"+str(temp),"計算値" + str(calc))