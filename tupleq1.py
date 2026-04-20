#Convert Touple to dictonery.


t= ('a',1,'b',2,'c',3)
d= {}
for i in range (0,len(t),2):
       d[t[i]]= t [i+1]  
print(d)       