import pandas as pd 

data = pd.read_csv("Twitter_SearchAPI_cleaned.csv")

polarity = []

pwordsfreq = {}
nwordsfreq = {}

match = []

for x in data['Tweet']:
        matchwords = ""
        polar = 0
        x = str(x).lower()
        words = x.split()
        bagofwords = {}

        for word in words:
                if word in bagofwords:
                        bagofwords[word] += 1
                else:
                        bagofwords[word] = 1

        pwordlist = []
        with open('Positive words.txt') as fp:
                for i in fp:  
                        pwordlist.append(i.strip())

        nwordlist = []
        with open('Negative words.txt') as fn:
                for i in fn:
                        nwordlist.append(i.strip())
                                
        for key,value in bagofwords.items():
                if(key.lower() in pwordlist):
                        if(matchwords == ""):
                                matchwords = str(key)
                        else:
                                matchwords = matchwords+','+key
                        polar += value
                        if key.lower() in pwordsfreq:
                                pwordsfreq[key.lower()] += value
                        else:
                                pwordsfreq[key.lower()] = 1
                                        
                if(key.lower() in nwordlist):
                        if(matchwords == ""):
                                matchwords = str(key)
                        else:
                                matchwords = matchwords+','+key
                        polar -= value
                        if key.lower() in nwordsfreq:
                                nwordsfreq[key.lower()] += value
                        else:
                                nwordsfreq[key.lower()] = 1

        match.append(matchwords)                        
        if(polar > 0):
                polarity.append("Positive")
        elif(polar < 0):
                polarity.append("Negative")
        else:
                polarity.append("Nutral")

data['Polarity'] = polarity
data['Match'] = match

data.to_csv('Twitter_SearchAPI_cleaned.csv',index=False)

word = []
count = []
prity = []

for key,value in pwordsfreq.items():
        word.append(key);
        count.append(value);
        prity.append("Positive")

for key,value in nwordsfreq.items():
        word.append(key);
        count.append(value);
        prity.append("Negative")

df = pd.DataFrame({'Word':word,'Frequency':count,'Polarity':prity})
df.to_csv('Words_Freq.csv',index=False, encoding='utf-8')

