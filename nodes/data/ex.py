import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='data merging code')

    parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)
    args = parser.parse_args()

    merci = args.file

    plt.style.use('ggplot')

    fig = plt.figure()
    i=2
    fd = pd.read_csv('./tmp/'+merci+str(i)+'.csv',index_col='timestamp')

    plt.plot(fd[str(5)],'k-')
    plt.savefig('./tmp/'+merci+str(i)+'.5.png')
    plt.cla()
    plt.close('all')
    del fig
