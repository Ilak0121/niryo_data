import pandas as pd
import numpy as np
import argparse


if __name__ =="__main__":
    #parser = argparse.ArgumentParser(description='data merging code')

    #parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)

    for i in range(1,11):
        print("[STATUS] : "+str(i)+"'s file starts to merge...."
        fd1 = pd.read_csv('/home/ilak/workspace/lab_repo/nodes/data/collision/collision1/test'+str(i)+'_collision',names=['timestamp','6','5','4'])
        fd2 = pd.read_csv('/home/ilak/workspace/lab_repo/nodes/data/collision/collision2/test'+str(i)+'_collision',names=['timestamp','1','2','3'])

        fd = pd.merge(fd1,fd2)
        fd = fd.set_index('timestamp').sort_index(axis=1)

        if not fd.isnull().values.any() == False:
            print("[WARN] : "+str(i)+"'s file has nan values!!"

        fd.to_csv('./sum_collision/collision'+str(i)+'.csv')
