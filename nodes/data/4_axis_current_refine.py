import pandas as pd
import numpy as np


if __name__ == "__main__":

    for i in range(1,11):
        fd1 = pd.read_csv('./sum_normal/normal'+str(i)+'.csv',index_col='timestamp')
        fd2 = pd.read_csv('./sum_collision/collision'+str(i)+'.csv',index_col='timestamp')

        fd1['4']=fd1['4'].subtract(fd1['5'])
        fd2['4']=fd2['4'].subtract(fd2['5'])

        fd1.to_csv('./sum_normal/normal'+str(i)+'.csv')
        fd2.to_csv('./sum_collision/collision'+str(i)+'.csv')
