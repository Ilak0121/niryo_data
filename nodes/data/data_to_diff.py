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

        df = pd.DataFrame()

        for j in range(1,7):

            List=[]
            Values=[]
            index_j = str(j)
            sample = fd[index_j]
            for k in range(0,len(sample.index)):
                if k == 0 or k == len(sample)-1:
                    List.append(sample.index[k])
                    Values.append(sample.iloc[k])
                else:
                    if sample.iloc[k]-sample.iloc[k-1] > 0 and sample.iloc[k+1]-sample.iloc[k]<0:
                        List.append(sample.index[k])
                        Values.append(sample.iloc[k])
            fd_temp = pd.DataFrame({"timestamp":List,index_j:Values})
            fd_temp = fd_temp.set_index('timestamp')
            df = pd.merge(df,fd_temp,left_index=True,right_index=True,how='outer')

        #print(df)
        #print(df['1'].mean(),df['2'].mean(),df['3'].mean())
        df.to_csv('./tmp/'+merci+str(i)+'.diff.csv')

