from ast import Return
from matplotlib import markers
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import random
from scipy.optimize import curve_fit
import statsmodels.api as sm
from sklearn import preprocessing
from scipy.interpolate import interp1d

def fit_func(x,*coeffs):
    y = np.polyval(coeffs, x)
    return y
#def func(x, a, b, c):
    #return a * np.exp(-b * x) + c

def objective(x, a, b):
	return a * x + b

def find_nearest(array, value):
    nearest = []
    for ay in array:
        if ay != 1.0:
            arr = np.asarray(ay)
            idx = (np.abs(arr - value))
            nearest.append(idx)
        else:
            pass
    min_nearest = np.min(nearest)
    arr_pos = nearest.index(min_nearest)
    if len(array) != len(nearest):
        near = array[arr_pos+1]
    else:
        near = array[arr_pos]
    return near   

def selectxy(subject):
    ticks = np.array(subject['segm'])
    #ticks = np.array(subject['segm'][:len(subject)])
    Time = range(len(ticks)-1)
    df_bands_end = subject[:-1]
    return Time,df_bands_end,ticks

def bands_select(bands):
    if bands == None:
        s = 2
        e = None
        return s,e
    elif bands == ['alpha/deltatheta']:
        s = 2
        e = 3
        return s,e
    elif bands == ['alpha/theta']:
        s = 3
        e = 4
        return s,e
    elif bands == ['alpha/delta']:
        s = 4
        e = None
        return s,e
    elif bands == ['delta']:
        s = 8
        e = 9
        return s,e
    elif bands == ['theta']:
        s = 14
        e = 15
        return s,e
    elif bands == ['deltatheta']:
        s = 15
        e = 16
        return s,e
    elif bands == ['alpha']:
        s = 35
        e = 36
        return s,e
    elif bands == ['alpha2']:
        s = 56
        e = 57
        return s,e
    elif bands == ['beta']:
        s = 48
        e = 49
        return s,e
    elif bands == ['gamma']:
        s = 55
        e = 56
        return s,e
    elif bands == ['alpha_1ch']:
        s = 8
        e = 9
        return s,e
    elif bands == ['alpha2_1ch']:
        s = 6
        e = 7
        return s,e

def mask(dataframe,sbj):
    name_mask=dataframe['sbj']==sbj
    name=dataframe[name_mask]
    return name

def select_color(num,path,sheet_name):
    df = pd.read_excel(path,sheet_name=sheet_name)
    columns_names = df.columns.values
    col = columns_names[1:(num+1)]
    color_col = []

    for c in col:
        r = random.random()
        b = random.random()
        g = random.random()
        c = (r, g, b)
        c=list(c)
        color_col.append(c[:3])
    return color_col

def iter_sbj(subject,bands,columns_names_bands=None,c=None,sbj_group=None,legend=None,tren=None,status=None,ticks=None,path_bands=None,title=None,size=None):
    if len(bands) != 1:
        for b in bands:
            s,e =bands_select([b])
            graph_bands(subject,columns_names_bands,s,e,path_bands,legend,tren,size,c,title)
    else:
        s,e =bands_select(bands)
        graph_bands(subject,columns_names_bands,s,e,path_bands,legend,tren,size,c,title)

def graph_bands(subject,columns_names_bands,s,e,path_bands,legend,tren,size,c,title):
    for j in columns_names_bands[s:e]:
        Time,df_bands_end,ticks = selectxy(subject)
        base(df_bands_end[j],Time=Time,legend=legend,tren=tren,i=j,c=c,sbj=subject['sbj'].unique()[0],size=None)
        if path_bands != None:
            plt.xlabel("Segment [3 min ea]",fontsize=size)
            plt.ylabel("",fontsize=size)
            plt.xticks(Time, ticks[:-1])
            plt.xlim(0,len(Time))
            plt.title('Quantitative EEG analysis '+str(title),fontsize=size,loc='left')
            plt.grid('On') 
        else:
            plt.xlabel("Time[min]",fontsize=size)
            plt.ylabel("Sleepiness level [Qualitative]",fontsize=size)
            plt.yticks((-1,0,1,2,3,4), ticks)
            plt.xlim(-1,30)
            plt.ylim(-1,5) 
            plt.title('Qualitative EEG analysis - Expert analysis '+str(title),fontsize=size,loc='left')
            plt.grid('On') 

def iter_reactivity(subject,c=None,sbj_group=None,tren=None,status=None,ticks=None,path_bands=None,title=None,size=None):
    Time = np.arange(0, 45, 0.5)
    size = 10
    df_bands_end = subject.iloc[:, 1:]
    df_bands_end.dropna(how='all', axis=1, inplace=True)
    color = ['b','r']
    for c,j in enumerate(df_bands_end):
        print(c)
        #print(j)
        xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
        f = interp1d(Time,df_bands_end[j],kind='cubic')
        plt.plot(xnew,f(xnew),label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        p1 = np.where((xnew >= 6) & (xnew <= 15))
        maxValue1 = np.max(f(xnew)[p1[0]])
        p2 = np.where(f(xnew) == maxValue1)
        maxValue2 = xnew[p2[0]][0]
        plt.annotate(str(np.round(maxValue2, 2)), (maxValue2,maxValue1),color='black',size=8)
        #plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        plt.xlabel("Frequency [Hz]",fontsize=size)
        plt.ylabel("Absolute power",fontsize=size)
        #plt.xticks(Time, ticks[:])
        plt.xlim(6,15)
        plt.title(title,loc='left')
        #plt.ylim(0,16)
        plt.legend(borderaxespad=0,fontsize=size,ncol=4,bbox_to_anchor=(0.5, 0.98))  
        plt.grid('On') 
        
def iter_WDN1(subject,title=None,size=None):
    Time = np.arange(0, 45, 0.5)
    df_bands_end = subject.iloc[:, 1:]
    df_bands_end.dropna(how='all', axis=1, inplace=True)
    color = ['maroon','lightseagreen','green','blue','orange','red']
    markers = ['o','^','s','*','8','2']
    for c,j in enumerate(df_bands_end):
        xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
        f = interp1d(Time,df_bands_end[j],kind='cubic')
        plt.scatter(xnew,f(xnew),marker=markers[c],color=color[c])
        plt.plot(xnew,f(xnew),label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        p1 = np.where((xnew >= 6) & (xnew <= 15))
        maxValue1 = np.max(f(xnew)[p1[0]])
        p2 = np.where(f(xnew) == maxValue1)
        maxValue2 = xnew[p2[0]][0]
        #plt.annotate(' '+str(np.round(maxValue2, 2)), (maxValue2,maxValue1),color='black',size=10,weight='bold')
        #plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        #plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
    IAFW = 10
    IAFD = 9
    A=1100
    #IAFN1 = 5
    s_annotate = 10
    # plt.xlabel("Frequency [Hz]",fontsize=size)
    # plt.ylabel("Absolute power",fontsize=size)
    plt.axvline(x = 10, color = 'k',linestyle=':')
    plt.annotate(' 10 Hz', (10,A),color='black',size=s_annotate)
    # plt.axvline(x = 2, color = 'green',linestyle=':')
    # plt.annotate(' 2 Hz', (2,A),color='black',size=s_annotate)
    # plt.axvline(x = 3, color = 'green',linestyle=':')
    # plt.annotate(' 3 Hz', (3,A),color='black',size=s_annotate)

    # #plt.axvline(x = IAFW-2, color = 'teal', linestyle=':')
    # #plt.annotate(' Wake IAF-2Hz', (IAFW-2,50),color='black',size=s_annotate)
    # plt.axvline(x = IAFW, color = 'maroon',linestyle=':')
    # plt.annotate(' Wake IAF', (IAFW,A),color='black',size=s_annotate)

    # plt.axvline(x = IAFD-2, color = 'lightseagreen', linestyle=':')
    # plt.annotate(' Drows IAF-2Hz', (IAFD-2,A),color='black',size=s_annotate)
    # #plt.axvline(x = IAFD, color = 'firebrick',linestyle=':')
    # #plt.annotate(' Drows IAF', (IAFD,0),color='black',size=s_annotate)

    # #plt.axvline(x = IAFN1-2, color = 'mediumaquamarine', linestyle=':')
    # #plt.annotate('Sleep IAF-2Hz', (IAFN1-2,50),color='black',size=s_annotate)
    # #plt.axvline(x = IAFN1, color = 'indianred',linestyle=':')
    # #plt.annotate('Sleep IAF', (IAFN1,50),color='black',size=s_annotate)


    #plt.xticks(Time, ticks[:])
    plt.xlim(1,20)
    plt.title(title, loc='left')
    #plt.ylim(0,A)
    plt.ylim((10**-1,10**4))
    plt.yscale('log')
    plt.ylabel('Absolute power')
    plt.xlabel('Frequency [Hz]')
    plt.legend(borderaxespad=0,fontsize=10,ncol=6)  
    plt.grid('On') 
    plt.show()

def iter_WDN(subject,title=None,size=None):
    Time = np.arange(0, 45, 0.5)
    df_bands_end = subject.iloc[:, 1:]
    df_bands_end.dropna(how='all', axis=1, inplace=True)
    color = ['maroon','lightseagreen','green','blue','orange']
    markers = ['o','^','s','*','8']
    for c,j in enumerate(df_bands_end):
        xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
        f = interp1d(Time,df_bands_end[j],kind='cubic')
        plt.scatter(xnew,f(xnew),marker=markers[c],color=color[c])
        plt.plot(xnew,f(xnew),label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        p1 = np.where((xnew >= 6) & (xnew <= 15))
        maxValue1 = np.max(f(xnew)[p1[0]])
        p2 = np.where(f(xnew) == maxValue1)
        maxValue2 = xnew[p2[0]][0]
        #plt.annotate(' '+str(np.round(maxValue2, 2)), (maxValue2,maxValue1),color='black',size=10,weight='bold')
        #plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        #plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
    IAFW = 10
    IAFD = 9
    A=300
    #IAFN1 = 5
    s_annotate = 10
    # plt.xlabel("Frequency [Hz]",fontsize=size)
    # plt.ylabel("Absolute power",fontsize=size)
    plt.axvline(x = 10, color = 'k',linestyle=':')
    plt.annotate(' 10 Hz', (10,A),color='black',size=s_annotate)
    # plt.axvline(x = 2, color = 'green',linestyle=':')
    # plt.annotate(' 2 Hz', (2,A),color='black',size=s_annotate)
    # plt.axvline(x = 3, color = 'green',linestyle=':')
    # plt.annotate(' 3 Hz', (3,A),color='black',size=s_annotate)

    # #plt.axvline(x = IAFW-2, color = 'teal', linestyle=':')
    # #plt.annotate(' Wake IAF-2Hz', (IAFW-2,50),color='black',size=s_annotate)
    # plt.axvline(x = IAFW, color = 'maroon',linestyle=':')
    # plt.annotate(' Wake IAF', (IAFW,A),color='black',size=s_annotate)

    # plt.axvline(x = IAFD-2, color = 'lightseagreen', linestyle=':')
    # plt.annotate(' Drows IAF-2Hz', (IAFD-2,A),color='black',size=s_annotate)
    # #plt.axvline(x = IAFD, color = 'firebrick',linestyle=':')
    # #plt.annotate(' Drows IAF', (IAFD,0),color='black',size=s_annotate)

    # #plt.axvline(x = IAFN1-2, color = 'mediumaquamarine', linestyle=':')
    # #plt.annotate('Sleep IAF-2Hz', (IAFN1-2,50),color='black',size=s_annotate)
    # #plt.axvline(x = IAFN1, color = 'indianred',linestyle=':')
    # #plt.annotate('Sleep IAF', (IAFN1,50),color='black',size=s_annotate)


    #plt.xticks(Time, ticks[:])
    plt.xlim(1,20)
    plt.title(title, loc='left')
    #plt.ylim(0,A)
    plt.ylim((10**0,10**3))
    plt.yscale('log')
    plt.ylabel('Absolute power')
    plt.xlabel('Frequency [Hz]')
    plt.legend(borderaxespad=0,fontsize=10,ncol=6,bbox_to_anchor=(1, 1.05))  
    plt.grid('On') 
    plt.show()

def iter_WRD(subject,title=None,size=None):
    Time = np.arange(0, 45, 0.5)
    df_bands_end = subject.iloc[:, 1:]
    df_bands_end.dropna(how='all', axis=1, inplace=True)
    color = ['maroon','lightseagreen','green']
    markers = ['o','^','s']
    difference = []
    for c,j in enumerate(df_bands_end):
        xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
        f = interp1d(Time,df_bands_end[j],kind='cubic')
        p1 = np.where((xnew >= 6) & (xnew <= 15))
        maxValue1 = np.max(f(xnew)[p1[0]])
        p2 = np.where(f(xnew) == maxValue1)
        maxValue2 = xnew[p2[0]][0]
        difference.append(maxValue1)
        plt.scatter(xnew,f(xnew),marker=markers[c],color=color[c])
        plt.plot(xnew,f(xnew),label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        #plt.annotate(' '+str(np.round(maxValue2, 2))+','+str(np.round(maxValue1, 2)), (maxValue2,maxValue1),color='black',size=10,weight='bold')
        #plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        #plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
    IAFW = 10
    IAFD = 9
    A=10**3
    #IAFN1 = 5
    s_annotate = 10
    # plt.xlabel("Frequency [Hz]",fontsize=size)
    # plt.ylabel("Absolute power",fontsize=size)
    plt.axvline(x = 10, color = 'k',linestyle=':')
    plt.annotate(' 10 Hz', (10,A),color='black',size=s_annotate)
    #plt.annotate('Wakefulness-Ripples = '+str(np.round(np.abs(difference[0]-difference[1]))),(12.5,10**3),color='red',size=s_annotate,weight='bold')
    #plt.annotate('Diffuse Theta-Ripples = '+str(np.round(np.abs(difference[2]-difference[1]))),(15.5,10**3),color='red',size=s_annotate,weight='bold')
    # plt.axvline(x = 2, color = 'green',linestyle=':')
    # plt.annotate(' 2 Hz', (2,A),color='black',size=s_annotate)
    # plt.axvline(x = 3, color = 'green',linestyle=':')
    # plt.annotate(' 3 Hz', (3,A),color='black',size=s_annotate)

    # #plt.axvline(x = IAFW-2, color = 'teal', linestyle=':')
    # #plt.annotate(' Wake IAF-2Hz', (IAFW-2,50),color='black',size=s_annotate)
    # plt.axvline(x = IAFW, color = 'maroon',linestyle=':')
    # plt.annotate(' Wake IAF', (IAFW,A),color='black',size=s_annotate)

    # plt.axvline(x = IAFD-2, color = 'lightseagreen', linestyle=':')
    # plt.annotate(' Drows IAF-2Hz', (IAFD-2,A),color='black',size=s_annotate)
    # #plt.axvline(x = IAFD, color = 'firebrick',linestyle=':')
    # #plt.annotate(' Drows IAF', (IAFD,0),color='black',size=s_annotate)

    # #plt.axvline(x = IAFN1-2, color = 'mediumaquamarine', linestyle=':')
    # #plt.annotate('Sleep IAF-2Hz', (IAFN1-2,50),color='black',size=s_annotate)
    # #plt.axvline(x = IAFN1, color = 'indianred',linestyle=':')
    # #plt.annotate('Sleep IAF', (IAFN1,50),color='black',size=s_annotate)


    #plt.xticks(Time, ticks[:])
    plt.xlim(1,20)
    plt.title(title, loc='left')
    #plt.ylim(0,A)
    plt.ylim((10**0,10**3))
    plt.yscale('log')
    plt.ylabel('Absolute power')
    plt.xlabel('Frequency [Hz]')
    plt.legend(borderaxespad=0,fontsize=10,ncol=6,bbox_to_anchor=(1, 1.05)) 
    plt.grid('On')


def vertex(subject,title=None,size=None):
    #Time = np.arange(0, 1/256*1000, 0.00764)
    Time = np.arange(0, 1/512*1000, 0.00382)
    df_bands_end = subject.iloc[:, 1:]
    df_bands_end.dropna(how='all', axis=1, inplace=True)
    color = 'maroon'
    plt.figure()
    plt.plot(Time,df_bands_end,label=subject['sbj'].iloc[0],color=color)
    plt.title(title, loc='left')
    plt.ylabel('Voltage[uV]')
    plt.xlabel('Time [s]')
    plt.annotate('Fz-Cz',(0.3,7.5),color='red',size=10,weight='bold')
    plt.legend(borderaxespad=0,fontsize=10,ncol=6,bbox_to_anchor=(1, 1.05))  
    plt.grid('On') 
    plt.show()


def expert(df,path_bands,group,legend,tren,size,title,c):
    ticks = ('R','N3','N2','N1','D','A')
    if group != None:
        colums = group
    for col in range(len(colums)):
        subject=df[colums[col]] 
        new_df = subject.dropna()
        Time = df['Time'][:len(new_df)]
        if c == None:
            plt.figure()
            base(new_df,Time=Time,legend=legend,tren=tren,i=colums[col],c=None,sbj=subject.name,size=size)
        else:
            plt.figure()
            base(new_df,Time=Time,legend=legend,tren=tren,i=colums[col],c=c[col],sbj=subject.name,size=size)
        #base(new_df,Time=Time,legend=legend,tren=tren,i=colums[col],c=c[col],sbj=subject['sbj'].iloc[0][:-5],size=None)
        if path_bands != None:
            plt.xlabel("Segment [3min ea]",fontsize=size)
            plt.ylabel("",fontsize=size)
            plt.xticks(Time, ticks[:-1])
            plt.xlim(0,len(Time))
            plt.ylim(0,5) 
            plt.title('Quantitative EEG analysis'+str(title),fontsize=size,loc='left')
            plt.grid('On') 
        else:
            plt.xlabel("Time[min]",fontsize=size)
            plt.ylabel("Sleepiness level [Qualitative]",fontsize=size)
            plt.yticks((-1,0,1,2,3,4), ticks)
            plt.xlim(-1,30)
            plt.ylim(-1,5) 
            plt.title('Qualitative EEG analysis - Expert analysis '+str(title),fontsize=size,loc='left')
            plt.grid('On') 
        if group == None:
            plt.grid('On') 
            plt.show()

def group_all(group,columns_names_bands,bands,df_bands,colums,col,tren,legend,path_bands,size,c,title):
    df_group = pd.DataFrame(group,columns=[columns_names_bands[0]])
    df_group = pd.merge(df_group, df_bands, on=columns_names_bands[0])
    subject=mask(df_group,colums[col])
    sbj_group = colums[col]
    if len(subject) != 0:
        if bands == ['EC','EO']:
            if c == None:
                plt.figure()
                iter_reactivity(subject,bands,columns_names_bands,c=None,sbj_group=sbj_group,size=size,title=title)
            else:
                plt.figure()
                iter_reactivity(subject,bands,columns_names_bands,c[col],sbj_group,size=size,title=title)
        elif bands == ['EO','C3','Cz','C4','P3','Pz','P4','O1','O2']:
            if c == None:
                if title == 'Vigilance3minEC_Rest1minEO' or 'Rest3minEC_Rest1minEO':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/2)):
                        m+=2
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        plt.figure()
                        iter_reactivity(new_subject,bands,columns_names_bands,c=None,sbj_group=sbj_group,size=size,title=title)
                        n+=2                    
            else:
                if title == 'Vigilance3minEC_Rest1minEO' or 'Rest3minEC_Rest1minEO':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/2)):
                        m+=2
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        plt.figure()
                        iter_reactivity(new_subject,bands,columns_names_bands,c[col],sbj_group,size=size,title=title)
                        n+=2   
            plt.grid('On') 
            plt.show()
            plt.title(title,loc='left')
                        
        elif bands == ['Wakefulness','Ripples','Diffuse Theta','Diffuse Theta + Vertex','K complexes +-','Diffuse Theta Before N1']:
            if c == None:
                if title == 'WDN1':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/6)):
                        m+=6
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        Ch = ['Fz','Cz','O1-O2','Relevant Channel']
                        plt.figure()
                        iter_WDN1(subject=new_subject,title=Ch[p])
                        n+=6
            else:
                if title == 'WDN1':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/6)):
                        m+=6
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        Ch = ['Fz','Cz','O1-O2','Relevant Channel']
                        plt.figure()
                        iter_WDN1(subject=new_subject,title=Ch[p])
                        n+=6  
        elif bands == ['Wakefulness','Ripples','Diffuse Theta','Diffuse Theta + Vertex','K complexes +-']:
            if c == None:
                if title == 'WDN':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/12)):
                        m+=5
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        Ch = ['Fz','Cz','O1-O2','Relevant Channel']
                        plt.figure()
                        iter_WDN(subject=new_subject,title=Ch[p])
                        n+=5
            else:
                if title == 'WDN':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/12)):
                        m+=5
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        Ch = ['Fz','Cz','O1-O2','Relevant Channel']
                        plt.figure()
                        iter_WDN(subject=new_subject,title=Ch[p])
                        n+=5 
        elif bands == ['Wakefulness','Ripples','Diffuse Theta']:
            if c == None:
                if title == 'WRD':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/3)):
                        m+=3
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        Ch = ['Fz','Cz','O1-O2','Relevant Channel']
                        plt.figure()
                        iter_WRD(subject=new_subject,title=Ch[p])
                        n+=3
                        plt.grid('On') 
            else:
                if title == 'WRD':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/3)):
                        m+=3
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        Ch = ['Fz','Cz','O1-O2','Relevant Channel']
                        plt.figure()
                        iter_WRD(subject=new_subject,title=Ch[p])
                        n+=3
        elif bands == ['Fp1-F7','F7-T7','T7-P7','P7-O1','Fp2-F8','F8-T8','T8-P8','Fp1-F3','F3-C3','C3-P3','P3-O1','Fp2-F4','F4-C4','C4-P4','P4-O2','Fz-Cz','Cz-Pz']:
            if c == None:
                if title == 'Vertex':
                    s=subject.drop(['sbj'], axis=1)
                    for p in range(int(len(subject.columns)/2)):
                        new_subject = s.iloc[:,:]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        vertex(subject=new_subject)
            else:
                if title == 'Vertex':
                    s=subject.drop(['sbj'], axis=1)
                    for p in range(int(len(subject.columns)/2)):
                        new_subject = s.iloc[:,:]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        vertex(subject=new_subject)
           #plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
            # IAFW = 8.5
            # IAFD = 9
            # #IAFN1 = 5
            # s_annotate = 10
            # plt.xlabel("Frequency [Hz]",fontsize=size)
            # plt.ylabel("Absolute power",fontsize=size)
            # plt.axvline(x = 10, color = 'k',linestyle=':')
            # plt.annotate(' 10 Hz', (10,50),color='black',size=s_annotate)
            # plt.axvline(x = 2, color = 'green',linestyle=':')
            # plt.annotate(' 2 Hz', (2,50),color='black',size=s_annotate)
            # plt.axvline(x = 3, color = 'green',linestyle=':')
            # plt.annotate(' 3 Hz', (3,50),color='black',size=s_annotate)

            # #plt.axvline(x = IAFW-2, color = 'teal', linestyle=':')
            # #plt.annotate(' Wake IAF-2Hz', (IAFW-2,50),color='black',size=s_annotate)
            # plt.axvline(x = IAFW, color = 'maroon',linestyle=':')
            # plt.annotate(' Wake IAF', (IAFW,50),color='black',size=s_annotate)

            # plt.axvline(x = IAFD-2, color = 'lightseagreen', linestyle=':')
            # plt.annotate(' Drows IAF-2Hz', (IAFD-2,50),color='black',size=s_annotate)
            # #plt.axvline(x = IAFD, color = 'firebrick',linestyle=':')
            # #plt.annotate(' Drows IAF', (IAFD,0),color='black',size=s_annotate)

            # #plt.axvline(x = IAFN1-2, color = 'mediumaquamarine', linestyle=':')
            # #plt.annotate('Sleep IAF-2Hz', (IAFN1-2,50),color='black',size=s_annotate)
            # #plt.axvline(x = IAFN1, color = 'indianred',linestyle=':')
            # #plt.annotate('Sleep IAF', (IAFN1,50),color='black',size=s_annotate)


            # #plt.xticks(Time, ticks[:])
            # #plt.xlim(1,20)
            # plt.title(title, loc='right')
            # #plt.ylim(0,50)
            # plt.legend(borderaxespad=0,fontsize=10,ncol=4,bbox_to_anchor=(0.5, 0.98))  
            # plt.grid('On') 
                                    
        else:
            if c == None:
                plt.figure()
                iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=None,sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=title,size=size)
            else:
                plt.figure()
                iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=c[col],sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=title,size=size)

# def group_none(df_bands,colums,col,bands,columns_names_bands,tren,legend,path_bands,size,c,title):
#     subject=mask(df_bands,colums[col])
#     sbj_group = colums[col]
#     if len(subject) != 0:
#         if bands == ['EC','EO']:
#             if c == None:
#                 iter_reactivity(subject,bands,columns_names_bands,c=None,sbj_group=sbj_group,title=title,size=size)
#             else:
#                 iter_reactivity(subject,bands,columns_names_bands,c[col],sbj_group,title=title,size=size)
#         else:
#             if c == None:
#                 iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=None,sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=title,size=size)    
#             else:    
#                 iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=c[col],sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=title,size=size)    

#     plt.grid('On') 
#     plt.show()

def expert_relations(df,group,columns_names_bands,col,legend,tren,df_bands,size=None,title=None,bands=None):
    df_group = pd.DataFrame(group,columns=[columns_names_bands[0]])
    df_group = pd.merge(df_group, df_bands, on=columns_names_bands[0])
    if group != None:
        colums = group
    else:
        colums = df_bands['sbj'].unique()
    if len(columns_names_bands[2:]) != 1:
        subject=df[colums[col]]  
        sub = df_bands[df_bands['sbj']==subject.name]
        T,df_bands_end,ticks_ax1 = selectxy(sub)
        new_df = subject.dropna()
        xt = []
        if (len(T) <= len(new_df[::3])):
            print(new_df.name,' T < df')
            Tend = T
            end_df = new_df[::3].iloc[:len(T)]
            print(len(Tend),len(end_df))
        elif (len(T) > len(new_df[::3])):
            print(new_df.name,' T > df')
            Tend = T[:len(new_df[::3])]
            end_df = new_df[::3]
            print(len(Tend),len(end_df))
        for i in range(len(df_bands_end['segm'])):
            xt.append(i)
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax2 = ax1.twinx()
        ticks_ax2 = ('R','N3','N2','N1','D','A',' ')
        if len(Tend) == len(end_df):
            xnew = np.linspace(Tend[0],Tend[len(Tend)-1],300) #300 represents number of points to make between T.min and T.max
            f2 = interp1d(Tend,end_df,kind='cubic')
            ax2.plot(xnew,f2(xnew),label="Qualitative ", c='k')
            #plt.scatter(Tend,end_df,label="Qualitative",c='r')
            if bands != None:
                for b in bands:
                    s,e =bands_select([b]) 
                    for j in columns_names_bands[s:e]:
                        f1 = interp1d(Tend,df_bands_end[j].iloc[:len(Tend)],kind='cubic')
                        ax1.plot(xnew,f1(xnew),label=j)
                        #ax1.plot(Tend,df_bands_end[j].iloc[:len(Tend)],label="Quantitative",c='c')
                        ax1.yaxis.set_label_position("right")
                        ax1.yaxis.tick_right() 
                        ax2.yaxis.set_label_position("left")
                        ax2.yaxis.tick_left()
                        ax2.set_ylim([-1,5])
                        ax2.set_yticklabels(ticks_ax2)
                        ax1.set_xticks(np.array(xt))
                        ax1.set_xticklabels(list(df_bands_end['segm']))
                        ax2.set_ylabel("Qualitative")
                        ax1.set_ylabel("Quantitative")
                fig.legend(borderaxespad=0,fontsize=10,loc='upper left',ncol=2,bbox_to_anchor=(0.5, 1.0))
                plt.title(title + ' ' +subject.name,loc='left')
                plt.grid('On') 
                plt.show() 
            else:
                for b in columns_names_bands[2:]:
                    s,e =bands_select([b]) 
                    for j in columns_names_bands[s:e]:
                        f1 = interp1d(Tend,df_bands_end[j].iloc[:len(Tend)],kind='cubic')
                        ax1.plot(xnew,f1(xnew),label=j)
                        #ax1.plot(Tend,df_bands_end[j].iloc[:len(Tend)],label="Quantitative",c='c')
                        ax1.yaxis.set_label_position("right")
                        ax1.yaxis.tick_right() 
                        ax2.yaxis.set_label_position("left")
                        ax2.yaxis.tick_left()
                        ax2.set_ylim([-1,5])
                        ax2.set_yticklabels(ticks_ax2)
                        ax1.set_xticks(np.array(xt))
                        ax1.set_xticklabels(list(df_bands_end['segm']))
                        ax2.set_ylabel("Qualitative")
                        ax1.set_ylabel("Quantitative")
                fig.legend(borderaxespad=0,fontsize=10,loc='upper left',ncol=2,bbox_to_anchor=(0.5, 1.0))
                plt.title(title + ' ' +subject.name,loc='left')
                plt.grid('On') 
                plt.show()
    else:
        s,e =bands_select(columns_names_bands[2:])
        for j in columns_names_bands[s:e]:
            for col in range(len(colums)):
                subject=df[colums[col]]      
                new_df = subject.dropna()
                sub = df_bands[df_bands['sbj']==subject.name]
                T,df_bands_end,ticks_ax1 = selectxy(sub)
                xt = []
                if (len(T) < len(new_df[::3])) == True:
                    print('T < df')
                    Tend = T
                    end_df = new_df[::3].iloc[:len(T)]
                    print(len(Tend),len(end_df))
                elif (len(T) > len(new_df[::3])) == True:
                    print('T > df')
                    Tend = T[:len(new_df[::3])]
                    end_df = new_df[::3]
                    print(len(Tend),len(end_df))
                else:
                    Tend = T
                for i in range(len(df_bands_end['segm'])):
                    xt.append(i)

                fig = plt.figure()
                ax1 = fig.add_subplot(111)
                ax2 = ax1.twinx()
                ticks_ax2 = ('R','N3','N2','N1','D','A',' ')
                if len(Tend) == len(end_df): 
                    xnew = np.linspace(Tend[0],Tend[len(Tend)-1],300) #300 represents number of points to make between T.min and T.max
                    f1 = interp1d(Tend,df_bands_end[j].iloc[:len(Tend)],kind='cubic')
                    f2 = interp1d(Tend,end_df,kind='cubic')
                    ax2.plot(xnew,f1(xnew),label="Qualitative",c='k')
                    ax1.plot(xnew,f2(xnew),label="Quantitative"+j,c='c')
                    #ax2.plot(Tend,end_df,label="Qualitative",c='g')
                    #ax1.plot(Tend,df_bands_end[j].iloc[:len(Tend)],label="Quantitative",c='c')
            ax1.yaxis.set_label_position("right")
            ax1.yaxis.tick_right() 
            ax2.yaxis.set_label_position("left")
            ax2.yaxis.tick_left()
            ax2.set_ylim([-1,5])
            ax2.set_yticklabels(ticks_ax2)
            ax1.set_xticks(np.array(xt))
            ax1.set_xticklabels(list(df_bands_end['segm']))
            ax2.set_ylabel("Qualitative")
            ax1.set_ylabel("Quantitative")
            fig.legend(borderaxespad=0,fontsize=size,loc='upper center',ncol=2,bbox_to_anchor=(0.5, 1.0))
            plt.title(title + ' ' +subject.name,loc='left')
            plt.grid('On') 
            plt.show() 


def base(new_df,Time,legend=None,tren=None,i=None,c=None,sbj=None,size=None):
    #lista = [mod1,mod2,mod3,mod4,mod5,mod6]
    #func=modelo(lista,Time,new_df)
    #print(func)
    fit_results = []
    for n in range(0, 5):
        try: 
            p0 = np.ones(n)
            popt1, pcov1 = curve_fit(fit_func, Time, new_df, p0=p0)
            fit_results.append(popt1)
        except:
            pass
    #z = np.polyfit(Time,new_df,g)
    #p = np.poly1d(z)
    if legend == True:
        '''f_results = []
        fr = []
        for f in fit_results:
            avg_f = np.average(f)
            f_results.append(avg_f)
            fr.append(f)
        fit_val=find_nearest(f_results, 1)
        fit_pos = f_results.index(fit_val)
        fit = fr[fit_pos]'''
        if tren == True:
            if sbj == i:
                #plt.plot(Time,new_df,label="Subject "+sbj,color=c)
                xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
                f = interp1d(Time,new_df,kind='cubic')
                plt.plot(xnew,f(xnew),label="Subject "+sbj,color=c)
            else:
                #plt.plot(Time,new_df,label="Subject "+sbj+' '+i,color=c)
                xnew = np.linspace(Time[0],Time[len(Time)-1],300) #300 represents number of points to make between T.min and T.max
                f = interp1d(Time,new_df,kind='cubic')
                plt.plot(xnew,f(xnew),label="Subject "+sbj+' '+i,color=c)
            #plt.plot(Time, fit_func(Time, *fit),linestyle='--', alpha=0.6,color=c, label=sbj + ' Trend Line of degree polynomial = '+ str(fit_pos))
            #plt.plot(Time,p(Time),linestyle='--',label="Trend "+i+' '+sbj,color=c)
            plt.legend(borderaxespad=0,fontsize=size,loc='upper center',ncol=4,bbox_to_anchor=(0.5, 1.05))  
            plt.grid('On') 
        elif tren == False:
            pass
            #plt.plot(Time,p(Time),linestyle='--',label="Trend "+i+' '+sbj,color=c)
            #plt.plot(Time, fit_func(Time, *fit),linestyle='--', alpha=0.6,color=c, label=sbj )#+ ' Trend Line of degree polynomial = '+ str(fit_pos))
            #plt.legend(borderaxespad=0,fontsize=size, loc='upper center',ncol=3,bbox_to_anchor=(0.5, 1.05))
            #plt.grid('On') 
        elif tren == None:
            #plt.plot(Time,new_df,label="Subject "+i,color=c)
            xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
            f = interp1d(Time,new_df,kind='cubic')
            plt.plot(xnew,f(xnew),label="Subject "+i,color=c)
            plt.legend(borderaxespad=0,fontsize=size, loc='upper center',ncol=3,bbox_to_anchor=(0.5, 1.05))
            plt.grid('On') 

    if legend == False:
        if tren == True:
            #plt.plot(Time,new_df,label="Behaviour ",color=c)
            xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
            f = interp1d(Time,new_df,kind='cubic')
            plt.plot(xnew,f(xnew),label="Behaviour ",color=c)
            #plt.plot(Time,p(Time),linestyle='--',label="Trend "+sbj,color=c)
            #for f in fit_results:
            #plt.plot(Time, fit_func(Time, *fit),linestyle='--', alpha=0.6,color=c, label=sbj + ' Trend Line of degree polynomial  = '+ str(fit_pos))

        elif tren == False:
            pass
            #plt.plot(Time,p(Time),linestyle='--',label="Trend "+sbj,color=c)
            #for f in fit_results:
            #plt.plot(Time, fit_func(Time, *fit),linestyle='--', alpha=0.6,color=c, label=sbj + ' Trend Line of degree polynomial  = '+ str(fit_pos))
        
        elif tren == None:
            #plt.plot(Time,new_df,label="Behaviour ",color=c)
            xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
            f = interp1d(Time,new_df,kind='cubic')
            plt.plot(xnew,f(xnew),label='Behaviour',color=c)

    



def graphic(num,path,sheet_name,path_bands,sheet_name_bands,size, legend, tren, plot, bands,status,group,title,c):
    df = pd.read_excel(path,sheet_name=sheet_name)
    columns_names = df.columns.values
    colums = columns_names[1:(num+1)]
    #c=select_color(colums)

    if path_bands != None:
        df_bands = pd.read_excel(path_bands,sheet_name=sheet_name_bands)
        columns_names_bands = df_bands.columns.values 
        #scaler = preprocessing.MinMaxScaler()
        #huber = sm.robust.scale.Huber()
        #for col_names in range(len(columns_names_bands)):
            #if 'mean' in columns_names_bands[col_names]:
                #k = huber(np.array(df_bands[columns_names_bands[col_names]]))[0]
                #df_bands[columns_names_bands[col_names]]=df_bands[columns_names_bands[col_names]]/k
                #l = np.array(df_bands[columns_names_bands[col_names]]).reshape(-1,1)
                #normalizedlist=scaler.fit_transform(l)
                #new_column=pd.DataFrame(normalizedlist,columns=[columns_names_bands[col_names]])
                #df_bands[columns_names_bands[col_names]] = new_column[columns_names_bands[col_names]]
                #df_bands.to_excel(r'E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\scaler.xlsx')
            #elif '/' in columns_names_bands[col_names]:
                #k = huber(np.array(df_bands[columns_names_bands[col_names]]))[0]
                #df_bands[columns_names_bands[col_names]]=df_bands[columns_names_bands[col_names]]/k
                #l = np.array(df_bands[columns_names_bands[col_names]]).reshape(-1,1)
                #normalizedlist=scaler.fit_transform(l)
                #new_column=pd.DataFrame(normalizedlist,columns=[columns_names_bands[col_names]])
                #df_bands[columns_names_bands[col_names]] = new_column[columns_names_bands[col_names]]
        col=0
        if group != None:
            if status == 'Relations and Expert':
                expert_relations(df,group,columns_names_bands,col,legend=legend,tren=tren,df_bands=df_bands,size=size,title=title,bands=bands)                
            else:
                for col in range(len(colums)):
                    try:
                        group_all(group,columns_names_bands,bands,df_bands,colums,col,tren,legend,path_bands,size,c,title)   
                    except:
                        pass
        elif group == None:
            if status == 'Relations and Expert':
                expert_relations(df,group,columns_names_bands,legend=legend,tren=tren,df_bands=df_bands,size=size,title=title,bands=bands)                   
            #else:
            #    group_none(df_bands,colums,col,bands,columns_names_bands,tren,legend,path_bands,size,c,title)            
    else:
        expert(df,path_bands,group,legend,tren,size,title,c)
       

    if group != None:
        if plot == False:
            pass
        elif plot == True:
            #plt.title(title)
            plt.grid('On') 
            plt.show()





            