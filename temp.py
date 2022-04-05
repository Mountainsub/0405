
import pandas as pd

with pd.HDFStore("./data/sum.hdf5") as store:
    temp =store.get("testcase")
    """
    a= temp["time_start"].to_list()
    l =len(a)
    print(l)
    
    b =temp["time_end"].to_list()
    
    pre_temp = 0
    """
    dict = {}
    
    """
    for i in range(15943):
        txt  = (str(a[i].hour)+":"+str(a[i].minute).zfill(2)+":"+str(a[i].second).zfill(2), str(b[i].hour)+":"+str(b[i].minute).zfill(2)+":"+str(b[i].second).zfill(2),float(b[i].timestamp())-float(a[i].timestamp()))
        if i==0:
            print(txt)
        temp = float(b[i].timestamp())-float(a[i].timestamp())
        dict[i] = temp
        
        
        if temp > 26:
            print(txt)
        elif temp > 4:
            print(txt)
        elif temp > 0.15:
            print(txt)
    
        
        
    temp = list(dict.values())      
    temp = sorted(temp, reverse=True)
    count=0
    for i in temp:
        if i > 0.1:
            print(i)
            count+= 1
        else:
            break
    #print(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])
    print(count)
    
    b = pd.to_datetime(b,  format= "%H時%M分%S秒")
    c = a.to_list()
    d = b.to_list()
    #print(temp)
    for i in range(1000):
        print(a, b)
    """
    box = []
    #print(temp.columns)
    #temp = sorted(temp, reverse=True)
    temp = temp["total"].to_list()
    
    for i,j in enumerate(temp):
        k = i+1
        try:
            temp[k]
        except:
            continue
        else:
            k = float(temp[k]) - float(temp[i])
            if k < 0:
                continue
            box.append(k)
    """
#box = sorted(box, reverse=True)
#
#box = [i for i in box if (i < 0.8 and i >= 0.7 )    ]
print(temp)
#print(np.mean(box))
