import pandas as pd
import numpy as np
import argparse

class collision():
    def __init__(self):
        pass
    def one(self): #mj
        return ('1D',85,1,0)
    def two(self): #mj
        return ('2D',250,1,0)
    def three(self): #3jd
        return ('3D',200,1,0) #20
    def five(self): #3jd
        return ('5D',20,7,3) #term, cnt

def test(args,dire):
    (joint, thres, term, cnt) = args
    Case = collision()
    check = 0
    number = 101

    if dire == '35jd':
        number = 11
    elif dire == 'n3jd':
        number = 52

    for i in range(1,number):
        #print("[INFO] : "+str(i)+"'s checking..")
        path = './data_2/'+dire+'.'+str(i)+'.csv'
        fd = pd.read_csv(path)
        for j in range(10,len(fd)-term):
            merci = fd[joint] #5d thres 9
            count = 0
            for k in range(term):
                if merci.iloc[j+k] > thres:
                    count += 1
            if count > cnt:
                check += 1
                #print(str(i)+': C'+str(j+k))
                break
    print("# of collision of "+str(joint)+" : "+str(check))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='collision test code')

    parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)
    args = parser.parse_args()

    Case = collision()

    test(Case.one(),args.file)
    test(Case.two(),args.file)
    test(Case.three(),args.file)
    test(Case.five(),args.file)


