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

    for i in range(1,(int(args.number)+1)):
        fd = pd.read_csv('./tmp/'+merci+str(i)+'.csv',index_col='timestamp')
        
        plt.style.use('ggplot')
        fig = plt.figure()
        fig.suptitle('figure sample plots')

        fig, lst = plt.subplots(3,2,figsize=(20,10))
        lst[0][0].plot(fd['1'])
        lst[0][1].plot(fd['2'])
        lst[1][0].plot(fd['3'])
        lst[1][1].plot(fd['4'])
        lst[2][0].plot(fd['5'])
        lst[2][1].plot(fd['6'])

        #plt.show()
        plt.savefig('./tmp/'+merci+str(i)+'.png')
        #plt.savefig('./dataAnalysis/graph/normal_graph'+str(i)+'.png')
