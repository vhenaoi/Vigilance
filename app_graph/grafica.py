import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import random

def graf(d,n,col,legend=True,g=None,status=None,size=None,tren=True,c=None):
    labels = ('R','N3','N2','N1','D','A')
    i = col[n]
    new_df = d[i]
    df=new_df.dropna()
    Time = d['Time'][:len(df)]
    z = np.polyfit(Time,df,g)
    p = np.poly1d(z)
   
    if legend == True:
        if tren == True:
            plt.plot(Time,df,label="Subject "+i,color=c)
            plt.plot(Time,p(Time),linestyle='--',label="Trend "+i+' '+status,color=c)
        else:
            plt.plot(Time,p(Time),linestyle='--',label="Trend "+i+' '+status,color=c)
    if legend == False:
        if tren == True:
            plt.plot(Time,df,label="Behaviour ",color=c)
            plt.plot(Time,p(Time),linestyle='--',label="Trend ",color=c)
        else:
            plt.plot(Time,p(Time),linestyle='--',label="Trend ",color=c)

    plt.legend(loc='upper center', borderaxespad=0,ncol=4,fontsize=size)
    plt.xlabel("Time[min]",fontsize=10)
    plt.ylabel("Sleepiness level",fontsize=10)
    plt.yticks((-1,0,1,2,3,4), labels)
    plt.xlim(-1,30)
    plt.ylim(-1,5)

def graf_ind(d,col,n,size,g,status,plot=True,legend=False,tren=True,c=None):
    graf(d,n,col,legend=legend,g=g,status=status,size=size,tren=tren,c=c)
    if plot == True:
        grap_name = col[n]
        plt.title('Qualitative EEG analysis - Expert analysis'+' - '+col[n]+' '+status,fontsize=size)
        plt.grid()
        plt.show()
        plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")
    else:
        None

def graf_group(n1,n2,z,g,s):
    for n in range(n1,n2):
        graf_ind(n,size=z,g=g,status=s,plot=False,legend=True,tren=False)

d = pd.read_excel(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\Sleep.xlsx",sheet_name="Grafico") 
col = ['Brescia01','Brescia17','Marseille01','Marseille11','Genova09','Thessaloniki17','Lille04','Brescia20','Brescia23','Brescia26','Genova2','Nold01','Nold03','Nold04','Nold06','Nold05']
def select_color(col):
    color_col = []
    for color in col:
        r = random.random()
        b = random.random()
        g = random.random()
        c = (r, g, b)
        c=list(c)
        color_col.append(c[:3])
    return color_col

c=select_color(col)
# #In[1] Individual 
# s = '(Sleep)'
# z = 10
# g = 4 # (subj = 1 (g=2))
# for subj in range(0,6):
#     graf_ind(d,col,subj,size=z,g=g,status=s,c=c[subj])

# s = '(No Sleep)'
# g=0
# for subj in range(6,14):
#     graf_ind(d,col,subj,size=z,g=g,status=s,c=c[subj])

# s = '(Sleep)'
# graf_ind(d,col,15,size=z,g=4,status=s,c=c[subj])

# #In[2] Group
# s = '(Sleep)'
# z = 10
# g = 4 # (subj = 1 (g=2))
# for subj in range(0,6):
#     graf_ind(d,col,subj,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[subj])

# grap_name = 'AD (Sleep)'
# plt.title('Qualitative EEG analysis - Expert analysis - AD',fontsize=10)
# plt.grid()
# plt.show()
# plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")

# s = '(No Sleep)'
# g=0
# for subj in range(6,11):
#     graf_ind(d,col,subj,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[subj])

# grap_name = 'AD (No Sleep)'
# plt.title('Qualitative EEG analysis - Expert analysis - AD',fontsize=10)
# plt.grid()
# plt.show()
# plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")


# s = '(No Sleep)'
# g=0
# for subj in range(11,14):
#     graf_ind(d,col,subj,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[subj])

# s = '(Sleep)'
# graf_ind(d,col,15,size=z,g=4,status=s,plot=False,legend=True,tren=False,c=c[15])

# grap_name = 'Nold'
# plt.title('Qualitative EEG analysis - Expert analysis - Nold',fontsize=10)
# plt.grid()
# plt.show()
# plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")

# #In[3] AD vs Nold
# s = '(Sleep)'
# z = 10
# g = 4 # (subj = 1 (g=2))
# grap_name = 'AD vs Nold (Sleep)'
# for subj in range(0,6):
#     graf_ind(d,col,subj,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[subj])

# graf_ind(d,col,15,size=z,g=4,status=s,plot=False,legend=True,tren=False,c=c[subj])

# plt.title('Qualitative EEG analysis - Expert analysis - AD vs Nold',fontsize=10)
# plt.grid()
# plt.show()
# plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")

# s = '(No Sleep)'
# g=0
# grap_name = 'AD vs Nold (No Sleep)'
# for subj in range(6,11):
#     graf_ind(d,col,subj,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[subj])

# for subj in range(11,14):
#     graf_ind(d,col,subj,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[subj])

# plt.title('Qualitative EEG analysis - Expert analysis - AD vs Nold',fontsize=10)
# plt.grid()
# plt.show()
# plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")

# #In[4] Por tipo de curvatura
# s = '.'
# z = 10
# g = 4 # (subj = 1 (g=2))
# grap_name = 'Negative slope'
# graf_ind(d,col,0,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[0])
# graf_ind(d,col,1,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[1])
# graf_ind(d,col,3,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[3])
# graf_ind(d,col,4,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[4])
# graf_ind(d,col,15,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[15])
# plt.title('Qualitative EEG analysis - Expert analysis - Negative slope',fontsize=10)
# plt.grid()
# plt.show()
# plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")
# g = 4 # (subj = 1 (g=2))
# grap_name = 'Parabolic'
# graf_ind(d,col,2,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[2])
# graf_ind(d,col,5,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[5])
# plt.title('Qualitative EEG analysis - Expert analysis - Parabolic',fontsize=10)
# plt.grid()
# plt.show()
# plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")
# g = 0 # (subj = 1 (g=2))
# grap_name = 'Lineal'
# graf_ind(d,col,6,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[6])
# graf_ind(d,col,7,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[7])
# graf_ind(d,col,8,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[8])
# graf_ind(d,col,9,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[9])
# graf_ind(d,col,10,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[10])
# graf_ind(d,col,11,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[11])
# graf_ind(d,col,12,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[12])
# graf_ind(d,col,13,size=z,g=g,status=s,plot=False,legend=True,tren=False,c=c[13])
# plt.title('Qualitative EEG analysis - Expert analysis - Lineal',fontsize=10)
# plt.grid()
# plt.show()
# plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")


#In[5] Bands

def graf_bands(d,n,col,legend=True,g=None,status=None,size=None,tren=True,c=None):
    i = col
    name = d['sbj'].iloc[0]
    new_df = d[i]
    df=new_df.dropna()
    ticks = np.array(d['segm'][:len(df)])
    Time = range(len(ticks)-1)
    df = df[:-1]
    z = np.polyfit(Time,df,g)
    p = np.poly1d(z)
    
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

def graf_ind_bands(d,col,n,size,g,status,plot=True,legend=False,tren=True,c=None):
    graf_bands(d,n,col,legend=legend,g=g,status=status,size=size,tren=tren,c=c)
    if plot == True:
        grap_name = 'Quantitative'
        plt.title('Quantitative EEG analysis'+' - '+col+' '+status,fontsize=size)
        plt.grid()
        plt.show()
        plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")
    else:
        None

def graf_group_bands(n1,n2,z,g,s):
    for n in range(n1,n2):
        graf_ind_bands(n,size=z,g=g,status=s,plot=False,legend=True,tren=False)



df = pd.read_excel(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Gp.xlsx",sheet_name="Foglio2") 
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
col_bands=['alpha/deltatheta','alpha/theta','alpha/delta']
#subjects_glob[0].iloc[0]['sbj']
for i in range(len(subjects_glob)):
    for j in col_bands:
        graf_ind_bands(subjects_glob[i],j,col[i],size=z,g=g,status=s,plot=False,legend=True,tren=True,c=c[i])
    grap_name = 'Quantitative '+j
    plt.title('Quantitative EEG analysis'+' - '+col[i])
    plt.grid()
    plt.show()
    plt.savefig(r"E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Graphics"+"/"+s+"_"+grap_name+".png")

