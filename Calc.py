import time
import pandas as pd

#https://stackoverflow.com/questions/2460177/edit-distance-in-python https://itnext.io/string-similarity-the-basic-know-your-algorithms-guide-3de3d7346227

def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)
        #print(tbl)

    return tbl[i,j]

#sources
#https://stackoverflow.com/questions/30768056/importing-external-txt-file-in-python

#load files
#len_2k_1 = open("string_len_2k.txt").read().split()
#len_2k_2 = open("string_len_2k.txt").read().split()

#https://stackoverflow.com/questions/26535114/paradoxical-time-intervals-in-python
#https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
#https://stackoverflow.com/questions/13603215/using-a-loop-in-python-to-name-variables

#future memory profiling:
#https://stackoverflow.com/questions/59114941/is-there-a-python-method-to-calculate-space-complexity

lengths = [.1,.25,.5,1,2,4]

namespace = globals()
#vars=[]
n=[]
time_x=[]

for i in lengths:
    filename="string_len_{}k.txt".format(i)
    namespace['len_%dk' % i] = open(filename).read().split()
    #vars.append(locals()['len_' + str(i) +'k'])
    #vars.append("namespace['len_%dk' % i]")
    d1 = time.time()
    ed=edit_distance(namespace['len_%dk' % i], namespace['len_%dk' % i])
    #time.sleep(1)
    d2 = time.time()
    delta = d2 - d1
    time_x.append(delta)
    n.append(len(namespace['len_%dk' % i]))

df=pd.DataFrame(n)
df2=pd.DataFrame(time_x)
df3=pd.concat([df,df2], axis=1)
#print(df3.head())
df3.columns=['n','seconds']
df3.to_csv('time_complex.csv')
