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
            k=j-1
            lst[int(k/2)][k%2].plot(fd[str(j)+'f'],'k-')
            lst[int(k/2)][k%2].set_xlabel(str(j)+"'s axis")

        #plt.show()
        plt.savefig('./tmp/'+merci+str(i)+'.filtered.png')
        plt.cla()
        plt.close('all')
        del fig
