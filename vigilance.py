from ast import Return
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import random
from scipy.optimize import curve_fit
import statsmodels.api as sm
from sklearn import preprocessing

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
    col = columns_names[1:17]
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
    else:
        s,e =bands_select(bands)
    for j in columns_names_bands[s:e]:
        Time,df_bands_end,ticks = selectxy(subject)
        base(df_bands_end[j],Time=Time,legend=legend,tren=tren,i=j,c=c,sbj=subject['sbj'].iloc[0][:-5],size=None)
        if path_bands != None:
            plt.xlabel("Segment [3 min ea]",fontsize=size)
            plt.ylabel("",fontsize=size)
            plt.xticks(Time, ticks[:-1])
            plt.xlim(0,len(Time))
            plt.yscale('log')
            plt.ylim([1**-10,1**11])
            #plt.title('Quantitative EEG analysis'+str(title)+' '+i+' '+status,fontsize=size)
            plt.grid() 
        else:
            plt.xlabel("Time[min]",fontsize=size)
            plt.ylabel("Sleepiness level [Qualitative]",fontsize=size)
            plt.yticks((-1,0,1,2,3,4), ticks)
            plt.xlim(-1,30)
            plt.ylim(-1,5) 
            plt.title('Qualitative EEG analysis - Expert analysis '+str(title)+' '+' '+status,fontsize=size)
            plt.grid() 

def iter_reactivity(subject,c=None,sbj_group=None,tren=None,status=None,ticks=None,path_bands=None,title=None,size=None):
    #Time = np.array(range(int(len(subject))))
    Time = np.arange(0, 45, 0.5)
    df_bands_end = subject.iloc[:, 1:]
    color = ['b','r']
    for c,j in enumerate(df_bands_end):
        print(c)
        print(j)
        plt.plot(Time,df_bands_end[j],label=subject['sbj'].iloc[0]+'_'+j,color=color[c])
        plt.xlabel("Frequency [Hz]",fontsize=size)
        plt.ylabel("Power spectral density [uV]",fontsize=size)
        #plt.xticks(Time, ticks[:])
        plt.xlim(6,15)
        plt.ylim(0,16)
        plt.legend(borderaxespad=0,fontsize=size)  
        plt.grid()

def expert(df,path_bands,group,legend,tren,size,title,c):
    ticks = ('R','N3','N2','N1','D','A')
    if group != None:
        colums = group
    for col in range(len(colums)):
        subject=df[colums[col]] 
        new_df = subject.dropna()
        Time = df['Time'][:len(new_df)]
        base(new_df,Time=Time,legend=legend,tren=tren,i=colums[col],c=c[col],sbj=subject.name,size=size)
        #base(new_df,Time=Time,legend=legend,tren=tren,i=colums[col],c=c[col],sbj=subject['sbj'].iloc[0][:-5],size=None)
        if path_bands != None:
            plt.xlabel("Segment [3min ea]",fontsize=size)
            plt.ylabel("Power [uV]",fontsize=size)
            plt.xticks(Time, ticks[:-1])
            plt.xlim(0,len(Time))
            plt.ylim(0,5) 
            #plt.title('Quantitative EEG analysis'+str(title)+' '+i+' '+status,fontsize=size)
            plt.grid() 
        else:
            plt.xlabel("Time[min]",fontsize=size)
            plt.ylabel("Sleepiness level [Qualitative]",fontsize=size)
            plt.yticks((-1,0,1,2,3,4), ticks)
            plt.xlim(-1,30)
            plt.ylim(-1,5) 
            plt.title('Qualitative EEG analysis - Expert analysis '+str(title)+' '+' '+status,fontsize=size)
            plt.grid() 
        if group == None:
            plt.grid()
            plt.show()

def group_all_glob_false(group,columns_names_bands,bands,df_bands,colums,col,tren,legend,path_bands,size,c):
    df_group = pd.DataFrame(group,columns=[columns_names_bands[0]])
    df_group = pd.merge(df_group, df_bands, on=columns_names_bands[0])
    subject=mask(df_group,colums[col])
    sbj_group = colums[col]
    if len(subject) != 0:
        if bands == ['OE','EO']:
            iter_reactivity(subject,bands,columns_names_bands,c[col],sbj_group,size=size)
        else:
            iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=c[col],sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=None,size=size)

def group_none_glob_false(df_bands,colums,col,bands,columns_names_bands,tren,legend,path_bands,size,c):
    subject=mask(df_bands,colums[col])
    sbj_group = colums[col]
    if len(subject) != 0:
        if bands == ['OE','EO']:
            iter_reactivity(subject,bands,columns_names_bands,c[col],sbj_group,size=size)
        else:
            iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=c[col],sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=None,size=size)    
    plt.grid()
    plt.show()

def group_all_glob_true( df_bands,group,columns_names_bands,colums,col,bands,tren,legend,path_bands,size,c):
    df_group = pd.DataFrame(group,columns=[columns_names_bands[0]])
    df_group = pd.merge(df_group, df_bands, on=columns_names_bands[0])
    subject=mask(df_group,colums[col]+'_glob')
    sbj_group=colums[col]+'_glob'
    if len(subject) != 0:
        iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=c[col],sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=None,size=size)                  

def group_none_glob_true(df_bands,colums,columns_names_bands,bands,col,tren,legend,path_bands,size,c):
    subject=mask(df_bands,colums[col]+'_glob')
    sbj_group=colums[col]+'_glob'
    if len(subject) != 0:
        iter_sbj(subject,bands=bands,columns_names_bands=columns_names_bands,c=c[col],sbj_group=sbj_group,legend=legend,tren=tren,status=None,ticks=None,path_bands=path_bands,title=None,size=size)    
    plt.grid()
    plt.show()

def expert_relations(df,bands,columns_names_bands,legend,tren,group=None,df_bands=None,size=None):
    df_group = pd.DataFrame(group,columns=[columns_names_bands[0]])
    df_group = pd.merge(df_group, df_bands, on=columns_names_bands[0])
    if group != None:
        colums = group
    else:
        colums = df_bands['sbj'].unique()
    s,e =bands_select(bands)  
    for j in columns_names_bands[s:e]:
        for col in range(len(colums)):
            if colums[col].find('glob') != -1:
                subject=df[colums[col][:colums[col].find('glob')-1]] 
            else:
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
            for i in range(len(df_bands_end['segm'])):
                xt.append(i)
            if tren == True:   
                fig = plt.figure()
                ax1 = fig.add_subplot(111)
                ax2 = ax1.twinx()
                ticks_ax2 = ('R','N3','N2','N1','D','A',' ')
                if len(Tend) == len(end_df): 
                    ax2.plot(Tend,end_df,label="Qualitative",c='g')
                    ax1.plot(Tend,df_bands_end[j].iloc[:len(Tend)],label="Quantitative",c='c')
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
                    fig.legend(loc = "upper center",bbox_to_anchor=(0.8, 0.9))
                    plt.title(subject.name)
                    plt.grid()
                    plt.show() 
                else:
                    print(len(Tend),len(end_df))

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
        f_results = []
        fr = []
        for f in fit_results:
            avg_f = np.average(f)
            f_results.append(avg_f)
            fr.append(f)
        fit_val=find_nearest(f_results, 1)
        fit_pos = f_results.index(fit_val)
        fit = fr[fit_pos]
        if tren == True:
            plt.plot(Time,new_df,label="Subject "+i,color=c)
            plt.plot(Time, fit_func(Time, *fit),linestyle='--', alpha=0.6,color=c, label=sbj + ' Trend Line of degree polynomial = '+ str(fit_pos))
            #plt.plot(Time,p(Time),linestyle='--',label="Trend "+i+' '+sbj,color=c)
            plt.legend(borderaxespad=0,fontsize=size)  
            plt.grid()
        elif tren == False:
            #plt.plot(Time,p(Time),linestyle='--',label="Trend "+i+' '+sbj,color=c)
            plt.plot(Time, fit_func(Time, *fit),linestyle='--', alpha=0.6,color=c, label=sbj )#+ ' Trend Line of degree polynomial = '+ str(fit_pos))
            plt.legend(borderaxespad=0,fontsize=size, loc='upper center',ncol=3,bbox_to_anchor=(0.5, 1.05))
            plt.grid()
        elif tren == None:
            plt.plot(Time,new_df,label="Subject "+i,color=c)
            plt.legend(borderaxespad=0,fontsize=size, loc='upper center',ncol=3,bbox_to_anchor=(0.5, 1.05))
            plt.grid()

    if legend == False:
        if tren == True:
            plt.plot(Time,new_df,label="Behaviour ",color=c)
            #plt.plot(Time,p(Time),linestyle='--',label="Trend "+sbj,color=c)
            #for f in fit_results:
            plt.plot(Time, fit_func(Time, *fit),linestyle='--', alpha=0.6,color=c, label=sbj + ' Trend Line of degree polynomial  = '+ str(fit_pos))

        elif tren == False:
            #plt.plot(Time,p(Time),linestyle='--',label="Trend "+sbj,color=c)
            #for f in fit_results:
            plt.plot(Time, fit_func(Time, *fit),linestyle='--', alpha=0.6,color=c, label=sbj + ' Trend Line of degree polynomial  = '+ str(fit_pos))
        
        elif tren == None:
            plt.plot(Time,new_df,label="Behaviour ",color=c)

    



def graphic(path=None,sheet_name=None,path_bands=None,sheet_name_bands=None,size=None, legend=True, tren=True, plot=True, group=None,status=None,path_save=None,save=False,bands=None,title=None,glob=None,c=None):
    df = pd.read_excel(path,sheet_name=sheet_name)
    columns_names = df.columns.values
    colums = columns_names[1:17]
    #c=select_color(colums)

    if path_bands != None:
        df_bands = pd.read_excel(path_bands,sheet_name=sheet_name_bands)
        columns_names_bands = df_bands.columns.values 
        scaler = preprocessing.MinMaxScaler()
        huber = sm.robust.scale.Huber()
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
            if group != None and glob == False:
                group_all_glob_false(group,columns_names_bands,bands,df_bands,colums,col,tren,legend,path_bands,size,c)   
            elif group == None and glob == False:
                group_none_glob_false(df_bands,colums,col,bands,columns_names_bands,tren,legend,path_bands,size,c)
            elif group != None and glob == True:
                if status == 'Relations and Expert':
                    expert_relations(df,bands,columns_names_bands,legend,tren,df_bands,size)                   
                else:
                    group_all_glob_true( df_bands,group,columns_names_bands,colums,col,bands,tren,legend,path_bands,size,c)
            elif group == None and glob == True:
                if status == 'Relations and Expert':
                    expert_relations(df,bands,columns_names_bands,legend,tren,group,df_bands,size)                   
                else:
                    group_none_glob_true(df_bands,colums,columns_names_bands,bands,col,tren,legend,path_bands,size,c)              
            else:
                pass
    else:
        expert(df,path_bands,group,legend,tren,size,title)
       

    if group != None:
        if plot == False:
            pass
        elif plot == True:
            plt.grid()
            plt.show()

    if save != None:
        plt.savefig(path_save+"/"+status+"_"+save+".png")


#['Nold01_glob','Nold03_glob','Nold04_glob','Nold05_glob','Nold06_glob']
#['Nold01','Nold03','Nold04','Nold05','Nold06']
#['Marseille11_glob','Genova09_glob','Thessaloniki17_glob','Brescia01_glob','Marseille01_glob','Brescia17_glob']
#['Marseille11','Genova09','Thessaloniki17','Brescia01','Marseille01','Brescia17']
#['Lille04_glob','Brescia20_glob','Brescia23_glob','Genova2_glob','Brescia26_glob']
#['Lille04','Brescia20','Brescia23','Genova2','Brescia26']

def opcion(op):
    #path = r"C:\Users\Pluto\Desktop\Veronica\Sleep.xlsx"
    path = r"C:\Users\Pluto\Desktop\Veronica\Vigilance\Sleep.xlsx"
    sheet_name="Grafico"
    c=select_color(path,sheet_name)
    if op == 'Individual bands':
        path_bands = r"C:\Users\Pluto\Desktop\Veronica\Gp.xlsx"
        sheet_name_bands = "SBJ"
        #group = ['Lille04_glob','Brescia20_glob','Brescia23_glob','Genova2_glob','Brescia26_glob']
        group = None
        path_save = r"C:\Users\Pluto\Desktop\Veronica\Graphics"
        bands = ['alpha2']
        size = 18
        legend = True
        tren = True
        plot = True
        glob = True
        save = None
        status = ''
        title = ''
        graphic(path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size,legend=legend, tren=tren, plot=plot, group=group,status=status,path_save=path_save,save=save,bands=bands,title=title,glob=glob,c=c)
    elif op == 'Relations':
        path_bands = r"C:\Users\Pluto\Desktop\Veronica\Gp.xlsx"
        sheet_name_bands= "Foglio2"
        group = None
        #['Nold01_glob','Nold03_glob','Nold04_glob','Nold05_glob','Nold06_glob']
        path_save = r"C:\Users\Pluto\Desktop\Veronica\Graphics"
        bands = ['alpha/delta','alpha/theta','alpha/deltatheta']
        size = 18
        legend = True
        tren = None
        plot = True
        glob = True
        save = None
        status = ''
        title = ''
        graphic(path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size, legend=legend, tren=tren, plot=plot, group=group,status=status,path_save=path_save,save=save,bands=bands,title=title,glob=glob,c=c)
    elif op == 'Expert':
        path_bands = None 
        sheet_name_bands= None
        #group = ['Lille04','Brescia20','Brescia23','Genova2','Brescia26']
        group = None
        path_save = r"C:\Users\Pluto\Desktop\Veronica\Graphics"
        size = 18
        legend = True
        tren = True
        plot = True
        glob = True
        save = None
        status = ''
        title = ''
        graphic(path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size, legend=legend, tren=tren, plot=plot, group=group,status=status,path_save=path_save,save=save,bands=None,title=title,glob=glob,c=c)
    elif op == 'Reactividad':
        path_bands = r"C:\Users\Pluto\Desktop\Veronica\Gp.xlsx"
        sheet_name_bands = "Reactivity"
        #group = ['Brescia17']
        group=None
        path_save = None
        bands = ['OE','EO']
        size = 18
        legend = True
        tren = True
        plot = True
        glob = False
        save = None
        status = ''
        title = ''
        graphic(path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size, legend=legend, tren=tren, plot=plot, group=group,status=status,path_save=path_save,save=save,bands=bands,title=title,glob=glob,c=c)
    elif op == 'Relations and Expert':
            #path_bands = r"C:\Users\Pluto\Desktop\Veronica\Gp.xlsx"
            path_bands = r"C:\Users\Pluto\Desktop\Veronica\Vigilance\Gp.xlsx"
            sheet_name_bands = "SBJ"
            group = None
            path_save = None
            bands = ['alpha2']
            size = 18
            legend = True
            tren = True
            plot = True
            glob = True
            save = None
            status = 'Relations and Expert'
            title = ''
            graphic(path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size, legend=legend, tren=tren, plot=plot, group=group,status=status,path_save=path_save,save=save,bands=bands,title=title,glob=glob,c=c)
