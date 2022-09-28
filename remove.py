import os
import glob
from unicodedata import name
import pandas as pd
#from numpy import number

name = 'Nold'
n = ' 8'
task = 'Sleep'
path = r'E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati'
Path_in = path +'/'+task+'/'+name+n+'/'+'eLoreta'
#Path_in+'/'+name+'/'+name+n+
path_txt = Path_in+'/'+'01 txt'
path_downsampling =Path_in+'/'+'02 downsampling'
path_ROI = Path_in+'/'+'06 ROI from LORB'
path_RF_TAF = Path_in+'/'+'07 TF and TAF'
path_other = r'E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Reactivity'


# Borrar archivos filtrados
def del_txt(path_txt): 
    with os.scandir(path_txt) as segm:
        #for txt in scandir(segm):
        for entry in segm :
            # Exclude the entry name
            # starting with '.'  
            if not entry.name.startswith('.') :
                # print entry's name 
                path_del = path_txt + '/' + entry.name
                files = glob.glob(path_del+'/'+'*-flt.txt')
                for del_file in files:
                    try:
                        print(del_file)
                        os.remove(del_file)
                    except OSError as e:
                        print(f"Error:{ e.strerror}")

# Borrar archivos no filtrados
def del_downsampling(path_downsampling):
    with os.scandir(path_downsampling) as segm:
        #for txt in scandir(segm):
        for entry in segm :
            # Exclude the entry name
            # starting with '.'  
            if not entry.name.startswith('.') :
                # print entry's name 
                path_del = path_downsampling + '/' + entry.name
                files = glob.glob(path_del+'/'+'*[0-9].txt*')
                print(files)
                for del_file in files:
                    try:
                        os.remove(del_file)
                    except OSError as e:
                        print(f"Error:{ e.strerror}")

def same_number_files(path_downsampling):
    file_count = []
    with os.scandir(path_downsampling) as segm:
        for entry in segm :
            if not entry.name.startswith('.') :
                count = 0
                new_path = path_downsampling + '/' + entry.name
                for path in os.scandir(new_path):
                    if path.is_file():
                        count += 1
                #print('file count:', count)
                file_count.append(count)
    organize=sorted(file_count)
    len_end = organize[0]
    return len_end

def resize(len_end):
    with os.scandir(path_downsampling) as segm:
        for entry in segm :
            if not entry.name.startswith('.') :
                new_path = path_downsampling + '/' + entry.name
                files = sorted(glob.glob(new_path+'/'+'*.txt'))
                for del_file in files[len_end:]:
                    try:
                        os.remove(del_file)
                    except OSError as e:
                        print(f"Error:{ e.strerror}")

def load_data_txt(file):
    df = pd.read_csv(file, sep=" ",header=None)
    print(df)
    segm = glob.glob(file+'/'+'*.txt')
    for s in segm:
        files = file + '/' + name + '_segment ' +s+'-sLorRoi.txt'
        print(files)

def txt_toexcel(file,n):
    fnames = glob.glob(file+'/'+'*.txt')
    print(fnames)
    first_df, *dfs = [pd.read_csv(f, sep="\s+",header=None) for f in fnames] 
    dfs = [df.iloc[:,:] for df in dfs]

    df = pd.concat([first_df, *dfs], axis=0)
    #df.to_excel(file+'/'+file[len(file)-n:]+'.xlsx', index=False, header=False)
    df.to_excel(r'E:\Academico\Universidad\Posgrado\La Sapienza\Vigilance\EEGlab\Dati\Reactivity/'+'reactivity.xlsx', index=False, header=False)





#del_txt(path_txt)
#print(path_txt)
#del_downsampling(path_downsampling)
#txt_toexcel(path_ROI,15)
txt_toexcel(path_other,0)
#len_end=same_number_files(path_downsampling)
#resize(len_end)
#end=same_number_files(path_downsampling)
#print(end)
#load_data_txt(path_ROI_from_LORB)