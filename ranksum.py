import sys, os
import numpy as np
import pandas as pd
from scipy.stats import ranksums

mainpath = "C:/Users/X553M/Desktop/ranksum/"
os.chdir(mainpath)

df = pd.read_csv("expression.csv", encoding='utf-8')
df2 = pd.read_csv("death_label.csv", encoding='utf-8')

df = pd.concat([df,df2], axis=1)
titles = list(df.columns)

drop = list(df["label"])

output = open("death_ranksum.csv","w", encoding='utf-8')

for i in titles:
    print(i)
    value1=[]
    value0=[]
    my_col = df[[i,"label"]]
    
    for j in range(0,my_col.shape[0]):
        if (str(my_col.iloc[j,1]) == "1"):
            value1.append(my_col.iloc[j,0])
        else:
            value0.append(my_col.iloc[j,0])
    value0 = np.array(value0) 
    value1 = np.array(value1)
    ttt = str(ranksums(value0,value1))
    p = ttt[ttt.find("pvalue=")+len("pvalue="):-1]
    output.write(i+","+p+"\n")
output.close()

