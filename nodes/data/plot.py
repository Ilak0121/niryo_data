import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

for i in range(1,11):
    fd1 = pd.read_csv('./normal/normal'+str(i)+'.csv',index_col='timestamp')
    fd2 = pd.read_csv('./collision/collision'+str(i)+'.csv',index_col='timestamp')
    
    fd = fd2

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
    plt.savefig('./dataAnalysis/graph/collision_graph'+str(i)+'.png')
    #plt.savefig('./dataAnalysis/graph/normal_graph'+str(i)+'.png')
