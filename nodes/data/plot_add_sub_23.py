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

        x2 = [v['2'] for i,v in fd.iterrows()]
        x3 = [v['3'] for i,v in fd.iterrows()]

        for j in range(1,7):
            if j == 1 or j > 3:
                k=j-1
                lst[int(k/2)][k%2].plot(fd[str(j)])
                lst[int(k/2)][k%2].set_xlabel(str(j)+"'s axis")
            elif j == 2:
                x4 = np.add(x2,x3)
                lst[0][1].plot(x4)
                lst[0][1].set_xlabel("(2,3)'s axis add")
            elif j == 3:
                x4 = np.subtract(x2,x3)
                lst[1][0].plot(x4)
                lst[1][0].set_xlabel("(2,3)'s axis sub")
            else:
                pass

        #plt.show()
        plt.savefig('./tmp/'+merci+str(i)+'.add_sub.png')
        plt.cla()
        plt.close('all')
        del fig
