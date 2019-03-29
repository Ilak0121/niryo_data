import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

for i in range(1,11):
    fd1 = pd.read_csv('./sum_normal/normal'+str(i)+'.csv',index_col='timestamp')
    fd2 = pd.read_csv('./sum_collision/collision'+str(i)+'.csv',index_col='timestamp')

    plt.style.use('ggplot')
    fig = plt.figure()
    fig.suptitle('figure sample plots')

    fig, lst = plt.subplots(3,2,figsize=(20,10))
    lst[0][0].plot(fd1['1'])
    lst[0][1].plot(fd1['2'])
    lst[1][0].plot(fd1['3'])
    lst[1][1].plot(fd1['4'])
    lst[2][0].plot(fd1['5'])
    lst[2][1].plot(fd1['6'])

    #plt.show()
    plt.savefig('./graph/normal_graph'+str(i)+'.png')
