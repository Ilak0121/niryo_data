import pandas as pd
import numpy as np

class collision():
    def __init__(self):
        pass
    def one(self): #mj
        return ('1d',10)
    def three(self): #3jd
        return ('3d',15) #20
    def five(self): #3jd
        return ('5d',7)

if __name__=="__main__":
    Case = collision()
    term = 6
    dire = '3jd'
    (joint, thres) = Case.one()
    for i in range(1,101):
        print("[INFO] : "+str(i)+"'s checking..")
        path = './data/'+dire+'.'+str(i)+'.csv'
        fd = pd.read_csv(path)
        for j in range(10,len(fd)-term):
            merci = fd[joint] #5d thres 9
            count = 0
            for k in range(term):
                if merci.iloc[j+k] > thres:
                    count += 1
            if count > 3:
                print(str(i)+': C')
                break


