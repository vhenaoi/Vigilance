from vigilance import graphic
from vigilance import select_color
import os

def graph_reactivity(path,sheet_name,sheet_name_bands,bands,group):
    c=select_color(path,sheet_name)
    #path_bands = r"C:\Users\Paperino\Desktop\Veronica\Vigilance\Gp.xlsx"
    path_bands = os.getcwd()+r'\files\Gp.xlsx'
    sheet_name_bands = sheet_name_bands
    group = group
    if bands == ['EC','EO']:
        bands = bands
    else:
        print('Enter in the parameter bands the condition of closed eyes and open eyes')
    size = 18
    legend = True
    tren = True
    plot = True
    status = ''
    title = sheet_name_bands
    graphic(path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size, legend=legend, tren=tren, plot=plot, group=group,status=status,bands=bands,title=title,c=c)