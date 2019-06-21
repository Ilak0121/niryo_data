import os
import time
import re
import pandas as pd
import numpy as np
import argparse

def filtering(fd):
    return_fd = pd.DataFrame()
    for j in range(1,7):
        List=[]
        Values=[]
        index_j = str(j)
        sample = fd[index_j]
        for k in range(0,len(sample.index)):
            if k < 3 or k > len(sample)-4:
                List.append(sample.index[k])
                Values.append(sample.iloc[k])
            else:
                di = 7
                List.append(sample.index[k])
                value = ( (1/di)*sample.iloc[k-3]
                       +(1/di)*sample.iloc[k-2]
                       +(1/di)*sample.iloc[k-1]
                       +(1/di)*sample.iloc[k]
                       +(1/di)*sample.iloc[k+1]
                       +(1/di)*sample.iloc[k+2]
                       +(1/di)*sample.iloc[k+3] )
                Values.append(value)
        fd_temp = pd.DataFrame({'timestamp':List,index_j+'f':Values})
        fd_temp=fd_temp.set_index('timestamp')
        return_fd = pd.merge(fd_temp,return_fd,how='outer',left_index=True,right_index=True)
    return return_fd

def differential(fd):
    return_fd = pd.DataFrame()
    for j in range(1,7):
        #print("[INFO] : "+str(j)+"'s axis....")
        List=[]
        Values=[]
        index_j = str(j)+'f'
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
        fd_temp = pd.DataFrame({'timestamp':List,str(j)+'d':Values})
        fd_temp = fd_temp.set_index('timestamp')
        return_fd = pd.merge(fd_temp,return_fd,how='outer',left_index=True,right_index=True)
    return return_fd

if __name__ =="__main__":
    
    parser = argparse.ArgumentParser(description='data merging code')

    parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)
    #parser.add_argument('-d','--dir',help='-d [SAVE_FILES_DIRECTORY]',required=True)
    parser.add_argument('-n','--number',help='-n [SAVE_FILES_NUMBERS]',required=True)
    parser.add_argument('-l','--log',help='-l [REFERENCE LOG FILE]',required=True)
    args = parser.parse_args()

    #merci1='collision'
    #merci2='normal'
    merci = args.file

    for i in range(1,(int(args.number)+1)):
        print("[STATUS] : "+str(i)+"'s file starts to merge....")
        #fd1 = pd.read_csv('/home/ilak/workspace/lab_repo/nodes/data/collision/collision1/test'+str(i)+'_collision',names=['timestamp','6','5','4'])
        #fd2 = pd.read_csv('/home/ilak/workspace/lab_repo/nodes/data/collision/collision2/test'+str(i)+'_collision',names=['timestamp','1','2','3'])
        fd1 = pd.read_csv('./tmp/'+merci+str(i)+'.csva',names=['timestamp','6','5','4'])
        fd2 = pd.read_csv('./tmp/'+merci+str(i)+'.csvb',names=['timestamp','1','2','3'])
        fd3 = pd.read_csv('./tmp/'+merci+str(i)+'.csvc',names=['timestamp','gx','gy','gz','ax','ay','az'])

        fd = pd.merge(fd1,fd2)
        fd = pd.merge(fd,fd3)
        fd = fd.set_index('timestamp').sort_index(axis=1)
        fd['4']=fd['4'].subtract(fd['5']) #4 axis motor gets current including 5axis.
        #cutting
        log = '../controller/logging/log.'+args.log+'.'+str(i)
        startT = exceptT = checkT = None
        with open(log) as lines:
            for line in lines:
                if re.match('^\[INFO\] Starting',line) : 
                    startT = float(line.split(':')[1])
                elif re.match('^\[INFO\] Exception',line) : 
                    exceptT = float(line.split(':')[1])
                elif re.match('^\[INFO\] Checking',line) : 
                    checkT = float(line.split(':')[1])
        if not startT == None:
            fd = fd.loc[float('%.3f'%startT):]
            if not exceptT == None:
                fd = fd.loc[:float('%.3f'%exceptT)]
            elif not checkT == None:
                fd = fd.loc[:float('%.3f'%checkT)]

        print("[INFO] : "+str(i)+"'s file's filtering....")
        fd = pd.merge(filtering(fd),fd,left_index=True,right_index=True) #filtered
        print("[INFO] : "+str(i)+"'s file's differentialing....")
        fd = pd.merge(differential(fd),fd,left_index=True,right_index=True) ##different value add

        indexs = ['1d','2d','3d','4d','5d','6d','1f','2f','3f','4f','5f','6f','1','2','3','4','5','6','gx','gy','gz','ax','ay','az']
        #indexs = ['1f','2f','3f','4f','5f','6f','1','2','3','4','5','6','gx','gy','gz','ax','ay','az']
        fd=fd.reindex(columns=indexs)
        
        if not fd.isnull().values.any() == False:
            print("[WARN] : "+merci+str(i)+"'s file has nan values!!")

        fd.to_csv('./tmp/'+merci+str(i)+'.csv')
    #os.system('rm ./tmp/*.csva; rm ./tmp/*.csvb;')# rm ./tmp/*.csvc')
