import time
import re
import sys


def test(given_time):

    given_time += 4;
    given_time = str(given_time) #start after 4 second

    p = re.compile('0$') #gets in millisecond period

    print_string=''

    while(True): #start waiting loop
        try:
            current_time = '%.3f'%time.time()
            if current_time == given_time:
                break;
        except:
            print("first loop error occur")


    while(True):
        try:
            current_time = '%.3f'%time.time()
            if not re.search(r'0$',current_time) == None:
                print(current_time)
            else:
                pass
        except (KeyboardInterrupt,EOFError):
            sys.exit(1)

        except :
            print('error occur')







if __name__ == "__main__":
    time_start = '%.3f'%time.time()
    print("the starting time is : "+ time_start)
    test(float(time_start))

