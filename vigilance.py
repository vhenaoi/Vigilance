from ast import Return
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

def mask(dataframe,sbj):
    name_mask=dataframe['sbj']==sbj
    name=dataframe[name_mask]
    return name

def select_color(path,sheet_name):
    df = pd.read_excel(path,sheet_name=sheet_name)
    columns_names = df.columns.values
    col = columns_names[1:21]
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
            plt.ylim([1**-10, 1**11])
            plt.yscale('log')
            plt.title('Quantitative EEG analysis '+str(title),fontsize=size)
            plt.grid() 
        else:
            plt.xlabel("Time[min]",fontsize=size)
            plt.ylabel("Sleepiness level [Qualitative]",fontsize=size)
            plt.yticks((-1,0,1,2,3,4), ticks)
            plt.xlim(-1,30)
            plt.ylim(-1,5) 
            plt.title('Qualitative EEG analysis - Expert analysis '+str(title),fontsize=size)
            plt.grid() 

def iter_reactivity(subject,c=None,sbj_group=None,tren=None,status=None,ticks=None,path_bands=None,title=None,size=None):
    Time = np.arange(0, 45, 0.5)
    df_bands_end = subject.iloc[:, 1:]
    df_bands_end.dropna(how='all', axis=1, inplace=True)
    color = ['b','r']
    for c,j in enumerate(df_bands_end):
        print(c)
        #print(j)
        xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
        f = interp1d(Time,df_bands_end[j],kind='cubic')
        plt.plot(xnew,f(xnew),label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        #plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        plt.xlabel("Frequency [Hz]",fontsize=size)
        plt.ylabel("Absolute power",fontsize=size)
        #plt.xticks(Time, ticks[:])
        plt.xlim(6,15)
        #plt.ylim(0,16)
        plt.legend(borderaxespad=0,fontsize=size,loc='upper center',ncol=4,bbox_to_anchor=(0.5, 1.05))  
        plt.grid()

def expert(df,path_bands,group,legend,tren,size,title,c):
    ticks = ('R','N3','N2','N1','D','A')
    if group != None:
        colums = group
    for col in range(len(colums)):
        subject=df[colums[col]] 
        new_df = subject.dropna()
        Time = df['Time'][:len(new_df)]
        if c == None:
            base(new_df,Time=Time,legend=legend,tren=tren,i=colums[col],c=None,sbj=subject.name,size=size)
        else:
            base(new_df,Time=Time,legend=legend,tren=tren,i=colums[col],c=c[col],sbj=subject.name,size=size)
        #base(new_df,Time=Time,legend=legend,tren=tren,i=colums[col],c=c[col],sbj=subject['sbj'].iloc[0][:-5],size=None)
        if path_bands != None:
            plt.xlabel("Segment [3min ea]",fontsize=size)
            plt.ylabel("",fontsize=size)
            plt.xticks(Time, ticks[:-1])
            plt.xlim(0,len(Time))
            plt.ylim(0,5) 
            plt.title('Quantitative EEG analysis'+str(title),fontsize=size)
            plt.grid() 
        else:
            plt.xlabel("Time[min]",fontsize=size)
            plt.ylabel("Sleepiness level [Qualitative]",fontsize=size)
            plt.yticks((-1,0,1,2,3,4), ticks)
            plt.xlim(-1,30)
            plt.ylim(-1,5) 
            plt.title('Qualitative EEG analysis - Expert analysis '+str(title),fontsize=size)
            plt.grid() 
        if group == None:
            plt.grid()
            plt.show()

def group_all(group,columns_names_bands,bands,df_bands,colums,col,tren,legend,path_bands,size,c,title):
    df_group = pd.DataFrame(group,columns=[columns_names_bands[0]])
    df_group = pd.merge(df_group, df_bands, on=columns_names_bands[0])
    subject=mask(df_group,colums[col])
    sbj_group = colums[col]
    if len(subject) != 0:
        if bands == ['EC','EO']:
            if c == None:
                iter_reactivity(subject,bands,columns_names_bands,c=None,sbj_group=sbj_group,size=size)
            else:
                iter_reactivity(subject,bands,columns_names_bands,c[col],sbj_group,size=size)
        elif bands == ['EO','C3','Cz','C4','P3','Pz','P4','O1','O2']:
            if c == None:
                if title == 'Vigilance3minEC_Rest1minEO':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/2)):
                        m+=2
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        iter_reactivity(new_subject,bands,columns_names_bands,c=None,sbj_group=sbj_group,size=size)
                        n+=2
                        
            else:
                if title == 'Vigilance3minEC_Rest1minEO':
                    s=subject.drop(['sbj'], axis=1)
                    n=0
                    m=0
                    for p in range(int(len(subject.columns)/2)):
                        m+=2
                        new_subject = s.iloc[:,n:m]
                        new_subject.insert(loc=0, column='sbj', value=subject.sbj)
                        iter_reactivity(new_subject,bands,columns_names_bands,c[col],sbj_group,size=size)
                        plt.grid()
                        plt.show()
                        n+=2                  
        else:
            if c == None:
                iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=None,sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=title,size=size)
            else:
                iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=c[col],sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=title,size=size)

'''def group_none(df_bands,colums,col,bands,columns_names_bands,tren,legend,path_bands,size,c,title):
    subject=mask(df_bands,colums[col])
    sbj_group = colums[col]
    if len(subject) != 0:
        if bands == ['EC','EO']:
            if c == None:
                iter_reactivity(subject,bands,columns_names_bands,c=None,sbj_group=sbj_group,title=title,size=size)
            else:
                iter_reactivity(subject,bands,columns_names_bands,c[col],sbj_group,title=title,size=size)
        else:
            if c == None:
                iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=None,sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=title,size=size)    
            else:    
                iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=c[col],sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=title,size=size)    

    plt.grid()
    plt.show()
'''
def expert_relations(df,bands,columns_names_bands,legend,tren,group=None,df_bands=None,size=None,title=None):
    df_group = pd.DataFrame(group,columns=[columns_names_bands[0]])
    df_group = pd.merge(df_group, df_bands, on=columns_names_bands[0])
    if group != None:
        colums = group
    else:
        colums = df_bands['sbj'].unique()
    if len(bands) != 1:
        for col in range(len(colums)):
            subject=df[colums[col]]  
            if subject.name == 'Nold01':
                print('NOLD01')    
            new_df = subject.dropna()
            sub = df_bands[df_bands['sbj']==subject.name]
            T,df_bands_end,ticks_ax1 = selectxy(sub)
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
                ax2.plot(xnew,f2(xnew),label="Qualitative ", c='c')
                #plt.scatter(Tend,end_df,label="Qualitative",c='r')
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
                plt.grid()
                plt.show() 
    else:
        s,e =bands_select(bands)
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
                    ax2.plot(xnew,f1(xnew),label="Qualitative"+j,c='g')
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
            plt.title(title + ' ' +subject.name)
            plt.grid()
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
            plt.grid()
        elif tren == False:
            pass
            #plt.plot(Time,p(Time),linestyle='--',label="Trend "+i+' '+sbj,color=c)
            #plt.plot(Time, fit_func(Time, *fit),linestyle='--', alpha=0.6,color=c, label=sbj )#+ ' Trend Line of degree polynomial = '+ str(fit_pos))
            #plt.legend(borderaxespad=0,fontsize=size, loc='upper center',ncol=3,bbox_to_anchor=(0.5, 1.05))
            #plt.grid()
        elif tren == None:
            #plt.plot(Time,new_df,label="Subject "+i,color=c)
            xnew = np.linspace(Time.min(),Time.max(),300) #300 represents number of points to make between T.min and T.max
            f = interp1d(Time,new_df,kind='cubic')
            plt.plot(xnew,f(xnew),label="Subject "+i,color=c)
            plt.legend(borderaxespad=0,fontsize=size, loc='upper center',ncol=3,bbox_to_anchor=(0.5, 1.05))
            plt.grid()

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

    



def graphic(path,sheet_name,path_bands,sheet_name_bands,size, legend, tren, plot, group,status,bands,title,c):
    df = pd.read_excel(path,sheet_name=sheet_name)
    columns_names = df.columns.values
    colums = columns_names[1:21]
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
        for col in range(len(colums)):
            print(colums[col])   
            if group != None:
                if status == 'Relations and Expert':
                    expert_relations(df,bands,columns_names_bands,legend=legend,tren=tren,df_bands=df_bands,size=size,title=title)                
                else:
                    group_all(group,columns_names_bands,bands,df_bands,colums,col,tren,legend,path_bands,size,c,title)   
            elif group == None:
                if status == 'Relations and Expert':
                    expert_relations(df,bands,columns_names_bands,legend=legend,tren=tren,df_bands=df_bands,size=size,title=title)                   
                #else:
                #    group_none(df_bands,colums,col,bands,columns_names_bands,tren,legend,path_bands,size,c,title)            
            else:
                pass
    else:
        expert(df,path_bands,group,legend,tren,size,title,c)
       

    if group != None:
        if plot == False:
            pass
        elif plot == True:
            plt.title(title)
            plt.grid()
            plt.show()





            