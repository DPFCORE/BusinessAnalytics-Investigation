import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_excel(r'D:\C\green500_top_202306.xlsx')
df = df.set_index(keys='Rank')
counlist = list(df[df['Country'] == 'China'].index)

print(len(counlist))
print(counlist)
Doc = df[df['Country'] == 'China']
Dou = df[df['Country'] == 'United States']
Doo = df[df['Country']!='China']
Doo = df[df['Country']!='United States']
print(len(Dou))
list1 = [len(Dou),len(Doc),len(Doo)]
plt.pie(x=list1,labels=['US','China','Other'],autopct='%1.1f%%')
list2 = list(df['Country'])
print(list2)
list3 = []
i=0
set1 = set(list3)
print(set1)
list4 = set(list2)
i=1
list5 = []
for a in list4:
    list5.append(0)

dict1 = dict(zip(list4,list5))
for a in list2:
    for b in list2:
        if b == a:
            i+=1
    dict1[a] = i
    i=0
dict1_sorted_values = sorted(dict1.items(),key = lambda x:x[1],reverse = True)
print(dict1_sorted_values)
plt.show()
dict2 = dict(dict1_sorted_values)
print(list(dict2.keys()))
print(list(dict2.values()))
sns.barplot(x=list(dict2.keys()),y=list(dict2.values()))
plt.show()
print(df['Country'] == 'China')