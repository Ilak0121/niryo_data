import pandas as pd
import numpy as np

class collision():
    def __init__(self):
        pass
    def one(self): #mj
        return ('1D',85,1,0)
    def three(self): #3jd
        return ('3D',200,1,0) #20
    def five(self): #3jd
        return ('5D',20,7,3) #term, cnt

if __name__=="__main__":
    Case = collision()
    dire = '3jd'
    (joint, thres, term, cnt) = Case.five()
    for i in range(1,101):
        print("[INFO] : "+str(i)+"'s checking..")
        path = './data_2/'+dire+'.'+str(i)+'.csv'
        fd = pd.read_csv(path)
        for j in range(10,len(fd)-term):
            merci = fd[joint] #5d thres 9
            count = 0
            for k in range(term):
                if merci.iloc[j+k] > thres:
                    count += 1
            if count > cnt:
                print(str(i)+': C'+str(j+k))
                break


