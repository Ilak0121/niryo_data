import pandas as pd
import numpy as np
from pandas import DataFrame, Series
mean_rms_normal=mean_rms_collision=0
mean_normal=mean_collision=0

for i in range(1,11):
    rms1=rms2=0
    mean1=mean2=0
    
    fd1 = pd.read_csv('./normal/normal'+str(i)+'.csv')
    fd2 = pd.read_csv('./collision/collision'+str(i)+'.csv')
    
    for j in fd1['1'].index:
        rms1 += fd1['1'][i]**2
        mean1 += fd1['1'][i]
    for k in fd2['1'].index:
        rms2 += fd2['1'][i]**2
        mean2 += fd2['1'][i]
        
    rms1 /= (fd1['1'].idxmax()+1)
    rms2 /= (fd1['1'].idxmax()+1)
    mean1 /= (fd1['1'].idxmax()+1)
    mean2 /= (fd1['1'].idxmax()+1)
    mean_rms_normal += round(rms1,2)
    mean_rms_collision += round(rms2,2)
    mean_normal += round(mean1,2)
    mean_collision += round(mean2,2)
    
    print(str(i)+"'s normal / collision rms : "+str(round(rms1,2))+" / "+ str(round(rms2,2)))
    print(str(i)+"'s normal / collision mean : "+str(round(mean1,2))+" / "+ str(round(mean2,2)))
    print("---------------------------------")
print("total normal rms :"+str(round(mean_rms_normal/10,2))+",collision rms:"+str(round(mean_rms_collision/10,2)))
print("total normal mean :"+str(round(mean_normal/10,2))+",collision mean:"+str(round(mean_collision/10,2)))
