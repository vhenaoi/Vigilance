import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

def graf(d,n,col,legend=True,g=None,status=None,size=None,tren=True):
    i = col[n]
    name = d['sbj'].iloc[0]
    new_df = d[i]
    df=new_df.dropna()
    ticks = np.array(d['segm'][:len(df)])
    Time = range(len(ticks)-1)
    df = df[:-1]
    z = np.polyfit(Time,df,g)
    p = np.poly1d(z)
    r = random.random()
    b = random.random()
    g = random.random()
    c = (r, g, b)
    print(i,c)
    
    if legend == True:
        if tren == True:
            plt.plot(Time,df,label="Subject "+name,color=c)
            plt.plot(Time,p(Time),linestyle='--',label="Trend "+' '+name+' '+status,color=c)
        else:
            plt.plot(Time,p(Time),linestyle='--',label="Trend "+' '+name+' '+status,color=c)
    if legend == False:
        if tren == True:
            plt.plot(Time,df,label="Behaviour "+name,color=c)
            plt.plot(Time,p(Time),linestyle='--',label="Trend ",color=c)
        else:
            plt.plot(Time,p(Time),linestyle='--',label="Trend ",color=c)

    plt.legend(loc='upper center', borderaxespad=0,ncol=4,fontsize=size)
    plt.xlabel("Segm",fontsize=10)
    plt.ylabel("Power",fontsize=10)
    plt.xticks(Time, ticks[:-1])
    plt.xlim(0,len(Time))
    #plt.ylim(0,1)

def graf_ind(d,col,n,size,g,status,plot=True,legend=False,tren=True):
    graf(d,n,col,legend=legend,g=g,status=status,size=size,tren=tren)
    if plot == True:
        plt.title('Qualitative EEG analysis - Expert analysis'+' - '+col[n]+' '+status,fontsize=size)
        plt.grid()
        plt.show()
    else:
        None

def graf_group(n1,n2,z,g,s):
    for n in range(n1,n2):
        graf_ind(n,size=z,g=g,status=s,plot=False,legend=True,tren=False)


df = pd.read_excel(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Gp.xlsx",sheet_name="Foglio2") 
print(df)
def mask(df,sbj):
    name_mask=df['sbj']==sbj
    name=df[name_mask]
    return name

Brescia01=mask(df,'brescia01')
Brescia01_glob=mask(df,'brescia01_glob')
Brescia17=mask(df,'brescia17')
Brescia17_glob=mask(df,'brescia17_glob')
Brescia20=mask(df,'brescia20')
Brescia20_glob=mask(df,'brescia20_glob')
Brescia23=mask(df,'brescia23')
Brescia23_glob=mask(df,'brescia23_glob')
Brescia26=mask(df,'brescia26')
Brescia26_glob=mask(df,'brescia26_glob')
Genova2=mask(df,'genova2')
Genova2_glob=mask(df,'genova2_glob')
Genova9=mask(df,'genova9')
Genova9_glob=mask(df,'genova9_glob')
Lille04=mask(df,'lille04')
Lille04_glob=mask(df,'lille04_glob')
Marseille01=mask(df,'marseille01')
Marseille01_glob=mask(df,'marseille01_glob')
Marseille11=mask(df,'marseille01')
Marseille11_glob=mask(df,'marseille01_glob')
Thessaloniki17=mask(df,'thessaloniki17')
Thessaloniki17_glob=mask(df,'thessaloniki17_glob')
Nold01=mask(df,'Nold1')
Nold01_glob=mask(df,'Nold1_glob')
Nold03=mask(df,'Nold3')
Nold03_glob=mask(df,'Nold3_glob')
Nold04=mask(df,'Nold4')
Nold04_glob=mask(df,'Nold4_glob')
Nold05=mask(df,'Nold5')
Nold05_glob=mask(df,'Nold5_glob')
Nold06=mask(df,'Nold6')
Nold06_glob=mask(df,'Nold6_glob')

subjects = [Brescia01,Brescia17,Marseille01,Marseille11,Genova9,Thessaloniki17,Lille04,Brescia20,Brescia23,Brescia26,Genova2,Nold01,Nold03,Nold04,Nold06,Nold05]
subjects_glob = [Brescia01_glob,Brescia17_glob,Marseille01_glob,Marseille11_glob,Genova9_glob,Thessaloniki17_glob,Lille04_glob,Brescia20_glob,Brescia23_glob,Brescia26_glob,Genova2_glob,Nold01_glob,Nold03_glob,Nold04_glob,Nold06_glob,Nold05_glob]

s = '.'
z = 10
g = 1 # (subj = 1 (g=2))
col=['alpha/deltatheta','alpha/theta','alpha/delta']
for i in subjects_glob:
    graf_ind(i,col,0,size=z,g=g,status=s,plot=False,legend=True,tren=True,c=c)
    plt.title("Trend line of evaluated subjects",fontsize=10)
    plt.grid()
    plt.show()
