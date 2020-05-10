import pandas as pd
import math

data = pd.read_csv("newsapicleaned.csv") 

title = []
desc = []
cont = []
 
for index,row in data.iterrows():
    f = open('news '+str(index+1)+'.txt',"w+")
    file = str(row['Title'])+'\n'+str(row['Description'])+'\n'+str(row['Content']).lower()
    f.write(file)
    f.close()
    
canada = 0
cfreq = []
halifax = 0
dalu = 0
univ = 0
canadaedu = 0
fileno = []
totalwords = []
Nbydf = []
log = []
fm = []
SearchQuery = ["Canada","Halifax","University","Dalhousie University","Canada Education"]

for i in range(1,101):
    with open('news '+str(i)+'.txt') as file:
        for index,row in enumerate(file):
            if(index==2):
                if 'canada' in row:
                    canada += 1
                    cfreq.append(row.count('canada'))
                    fileno.append('news '+str(i))
                    totalwords.append(len(row.split()))
                    fm.append(row.count('canada')/len(row.split()))
                if 'halifax' in row:
                    halifax += 1
                if 'university' in row:
                    univ += 1
                if 'dalhousie university' in row:
                    dalu += 1
                if 'canada education' in row:
                    canadaedu += 1
                 
count = [canada,halifax,univ,dalu,canadaedu]
for row in count:
    if(row != 0):
        Nbydf.append(100/row)
    else:
        Nbydf.append("0")

for row in Nbydf:
    if(row != "0"):
        log.append(math.log10(float(row)))
    else:
        log.append("0")

df = pd.DataFrame({'File':fileno,'Total Words':totalwords,'Frequency':cfreq,'f/m':fm})
df.to_csv('10_b.csv',index=False)

df = pd.DataFrame({'Search Query':SearchQuery,'Document containing term(df)':count,'Total Documents(N)/number of documents term appeared(df)':Nbydf,'Log10(N/df)':log})
df.to_csv('10_a.csv',index=False)                        

maximum = 0
for index,row in enumerate(fm):
    if row > maximum:
        maximum = index

print("Article with highest relative frequency :"+fileno[maximum])
