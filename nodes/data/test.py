import csv

with open('./normal/normal1/test1_normal') as fd1:
    with open('./normal/normal2/test1_normal') as fd2:
        rd1 = csv.reader(fd1,delimiter=',') #4,5,6
        rd2 = csv.reader(fd1,delimiter=',') #1,2,3
        line_count = 0
        for row in rd:
            print("{},{},{},{}".format(row[0],row[1],row[2],row[3]))
            line_count += 1
        print(line_count)
