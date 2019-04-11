# differential Test
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='data merging code')

    parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)
    #parser.add_argument('-d','--dir',help='-d [SAVE_FILES_DIRECTORY]',required=True)
    parser.add_argument('-n','--number',help='-n [SAVE_FILES_NUMBERS]',required=True)
    args = parser.parse_args()

    merci = args.file

    plt.style.use('ggplot')

    for i in range(1,(int(args.number)+1)):
        print("[STATUS] : "+str(i)+"'s plotting starts...")
        fig = plt.figure()
        fig.suptitle('figure sample plots')
        fig, lst = plt.subplots(3,2,figsize=(20,10))
        fd = pd.read_csv('./tmp/'+merci+str(i)+'.csv',index_col='timestamp')

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
                    value = ( (1/di)*sample.iloc[k-3]
                           +(1/di)*sample.iloc[k-2]
                           +(1/di)*sample.iloc[k-1]
                           +(1/di)*sample.iloc[k]
                           +(1/di)*sample.iloc[k+1]
                           +(1/di)*sample.iloc[k+2]
                           +(1/di)*sample.iloc[k+3] )
                    List.append(sample.index[k])
                    Values.append(value)
            fd_temp = pd.DataFrame({"x":List,"y":Values})
            lst[int((j-1)/2)][(j-1)%2].plot(fd_temp['x'],fd_temp['y'],'k-')
            lst[int((j-1)/2)][(j-1)%2].set_xlabel(str(j)+"'s axis")

        #plt.show()
        plt.savefig('./tmp/'+merci+str(i)+'.png')
        plt.cla()
        plt.close('all')
        del fig
