#import tensorflow as tf
import pandas as pd
import numpy as np
import math
     

col_link_path = './printer/print_collision_link/print_collision_link_data/collision_link'#+'1.csv'
col_mj_path = './printer/print_collision_MJ/print_collision_MJ_data/collision_MJ'#+'1.csv'
col_ej_path = './printer/print_collision_EJ/print_collision_data/collision'#+'1.csv'
normal_path= './printer/print_collision_normal/print_normal_data/normal'#+'1.csv'

n=993 # least data number

def rms(series):
    result = 0
    length = len(series)
    for i in range(0,length):
        result += series.iloc[i]**2
    result /= length
    result = math.sqrt(result)
    return result

s1 = 400
e1 = 600

for i in range(1,101):
    fd_e = pd.read_csv(col_ej_path+str(i)+'.csv',index_col='timestamp')
    fd_m = pd.read_csv(col_mj_path+str(i)+'.csv',index_col='timestamp')
    fd_l = pd.read_csv(col_link_path+str(i)+'.csv',index_col='timestamp')
    fd_n = pd.read_csv(normal_path+str(i)+'.csv',index_col='timestamp')
    
    fd_e = fd_e.iloc[s1:e1].loc[:,lambda df:['1','2','3','4','5','6']]
    fd_m = fd_m.iloc[s1:e1].loc[:,lambda df:['1','2','3','4','5','6']]
    fd_l = fd_l.iloc[s1:e1].loc[:,lambda df:['1','2','3','4','5','6']]
    fd_n = fd_n.iloc[s1:e1].loc[:,lambda df:['1','2','3','4','5','6']]

    fd_e['2'] = pd.Series(np.subtract(fd_e['2'],fd_e['3']))
    fd_m['2'] = pd.Series(np.subtract(fd_m['2'],fd_m['3']))
    fd_l['2'] = pd.Series(np.subtract(fd_l['2'],fd_l['3']))
    fd_n['2'] = pd.Series(np.subtract(fd_n['2'],fd_n['3']))

    string_e = 'e:'
    string_m = 'm:'
    string_l = 'l:'
    string_n = 'n:'
    tmp_e=[]
    tmp_m=[]
    tmp_l=[]
    tmp_n=[]
    for j in range(1,4):
        k=str(j)
        tmp_e.append(rms(fd_e[k]))
        tmp_m.append(rms(fd_m[k]))
        tmp_l.append(rms(fd_l[k]))
        tmp_n.append(rms(fd_n[k]))
    for j in range(0,3):
        tmp_e[j] /= pd.Series(tmp_e).mean()
        tmp_m[j] /= pd.Series(tmp_m).mean()
        tmp_l[j] /= pd.Series(tmp_l).mean()
        tmp_n[j] /= pd.Series(tmp_n).mean()
    for j in range(1,7):
        k=str(j)
        if j < 4:
            string_e += '%.5f'%tmp_e[j-1]+','
            string_m += '%.5f'%tmp_m[j-1]+','
            string_l += '%.5f'%tmp_l[j-1]+','
            string_n += '%.5f'%tmp_n[j-1]+','
        else:
            string_e += str(rms(fd_e[k]))+','
            string_m += str(rms(fd_m[k]))+','
            string_l += str(rms(fd_l[k]))+','
            string_n += str(rms(fd_n[k]))+','
    print(string_e)
    print(string_m)
    print(string_l)
    print(string_n)
    print("--------------------------------------")
