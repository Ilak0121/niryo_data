
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
        return ('5',20,5,0) #term, cnt

def test2(args,dire):
    (joint, thres, term, cnt) = args
    check = 0
    number = 101
    if dire == '35jd':
        number = 2
    elif dire == 'n3jd':
        number = 52

    for i in range(1,number):
        #print("[INFO] : "+str(i)+"'s checking..")
        path = './data_2/'+dire+'.'+str(i)+'.csv'
        fd = pd.read_csv(path)
        for j in range(10,len(fd)-term):
            merci = fd[joint] #5d thres 9
            count = 0
            rms = 0
            for k in range(term):
                rms += merci.iloc[j+k] ** 2
            rms /= term
            print(str(fd['timestamp'].iloc[j+k])+' : '+str(rms))
            '''
            if rms > 14000:
                count += 1
                #print(str(i)+' : ')
            if count > cnt:
                check += 1
                #print(str(i)+': C'+str(j+k))
                break
            '''
    print("# of collision of "+str(joint)+" : "+str(check))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='collision test code')

    parser.add_argument('-f','--file',help='-f [SAVE_FILE_NAME]',required=True)
    args = parser.parse_args()

    Case = collision()

    test2(Case.five(),args.file)


