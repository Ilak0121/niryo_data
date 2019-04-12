import os
import pandas as pd
import numpy as np
import argparse
from math import sqrt

def rms(series):
    result = 0
    length = len(series)
    for i in range(0,length):
        result += series.iloc[i]**2
    result /= length
    result = sqrt(result)
    return result

if __name__ =="__main__":
    
    parser = argparse.ArgumentParser(description='data merging code')

    parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)
    parser.add_argument('-n','--number',help='-n [SAVE_FILES_NUMBERS]',required=True)
    args = parser.parse_args()

    merci = args.file
    
    n=993 # data length limit
    
    total_df = pd.DataFrame()

    for i in range(1,(int(args.number)+1)):
        print("[STATUS] : "+str(i)+"'s file starts to change....")
        
        fd = pd.read_csv('./tmp/'+merci+str(i)+'.csv',index_col='timestamp')
        fd = fd.iloc[0:n].loc[:,lambda df:['1','2','3','4','5','6']]

        tmp=[]
        for j in range(0,3):
            k=str(j+1)
            #tmp.append(rms(fd[k])/pd.Series(fd[k]))
            tmp.append(rms(fd[k]))
        for j in range(0,3):
            tmp[j] /= pd.Series(tmp).mean()
        for j in range(4,7):
            k=str(j)
            tmp.append(rms(fd[k]))
        tmp = pd.Series(tmp,index=['1','2','3','4','5','6'])
        total_df = total_df.append(tmp,ignore_index=True)
    total_df.to_csv('./tmp/'+merci+'.rms.csv')
