import math
import csv
with open("sd.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)

    mean=total/n
    return mean

squarred_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squarred_list.append(a)

sum=0
for i in squarred_list:
    sum=sum+i
    
result=sum/(len(data)-1)

standarddeviation=math.sqrt(result)
print(standarddeviation)
