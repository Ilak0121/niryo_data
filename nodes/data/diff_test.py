import os
import time
import re
import pandas as pd
import numpy as np
import argparse

def differential(fd):
    return_fd = pd.DataFrame()
    for j in range(1,7):
        #print("[INFO] : "+str(j)+"'s axis....")
        List=[]
        Values=[]
        index_j = str(j)
        sample = fd[index_j]
        for k in range(0,len(sample.index)):
            if k > len(sample.index)-2:
                List.append(sample.index[k])
                Values.append(0)
            else:
                value = abs(sample.iloc[k+1]
                        - sample.iloc[k])
                List.append(sample.index[k])
                Values.append(value)
        fd_temp = pd.DataFrame({'timestamp':List,str(j)+'D':Values})
        fd_temp = fd_temp.set_index('timestamp')
        return_fd = pd.merge(fd_temp,return_fd,how='outer',left_index=True,right_index=True)
    return return_fd

if __name__ =="__main__":
    
    parser = argparse.ArgumentParser(description='data merging code')

    parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)
    parser.add_argument('-n','--number',help='-n [SAVE_FILES_NUMBERS]',required=True)
    args = parser.parse_args()

    merci = args.file

    for i in range(1,(int(args.number)+1)):
        print("[STATUS] : "+str(i)+"'s file starts to work....")

        fd = pd.read_csv('./tmp/'+merci+str(i)+'.csv')

        fd = fd.set_index('timestamp')

        print("[INFO] : "+str(i)+"'s file's differentialing....")
        fd = pd.merge(differential(fd),fd,left_index=True,right_index=True) ##different value add

        indexs = ['1D','2D','3D','4D','5D','6D','1d','2d','3d','4d','5d','6d','1f','2f','3f','4f','5f','6f','1','2','3','4','5','6','gx','gy','gz','ax','ay','az']
        #indexs = ['1f','2f','3f','4f','5f','6f','1','2','3','4','5','6','gx','gy','gz','ax','ay','az']
        fd=fd.reindex(columns=indexs)
        
        if not fd.isnull().values.any() == False:
            print("[WARN] : "+merci+str(i)+"'s file has nan values!!")

        fd.to_csv('./tmp/'+merci+str(i)+'.csvt')
    #os.system('rm ./tmp/*.csva; rm ./tmp/*.csvb;')# rm ./tmp/*.csvc')
