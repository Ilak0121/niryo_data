import os
import pandas as pd
import numpy as np
import argparse


if __name__ =="__main__":
    
    parser = argparse.ArgumentParser(description='data merging code')

    parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)
    #parser.add_argument('-d','--dir',help='-d [SAVE_FILES_DIRECTORY]',required=True)
    parser.add_argument('-n','--number',help='-n [SAVE_FILES_NUMBERS]',required=True)
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

        fd = pd.merge(fd1,fd2)
        fd = fd.set_index('timestamp').sort_index(axis=1)

        fd['4']=fd['4'].subtract(fd['5']) #4 axis motor gets current including 5axis.

        if not fd.isnull().values.any() == False:
            print("[WARN] : "+merci+str(i)+"'s file has nan values!!")

        fd.to_csv('./tmp/'+merci+str(i)+'.csv')
    os.system('rm ./tmp/*.csva; rm ./tmp/*.csvb')
