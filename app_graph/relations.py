from vigilance import graphic
from vigilance import select_color
import os

def graph_relations(path,sheet_name,sheet_name_bands,group,bands):
    c=select_color(path,sheet_name)
    #path_bands = r"C:\Users\Paperino\Desktop\Veronica\Vigilance\Gp.xlsx"
    path_bands = os.getcwd()+r'\files\Gp.xlsx'    
    sheet_name_bands= sheet_name_bands
    group = group
    bands = bands
    size = 18
    legend = True
    tren = None
    plot = False
    status = ''
    title = sheet_name_bands
    graphic(path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size, legend=legend, tren=tren, plot=plot, group=group,status=status,bands=bands,title=title,c=c)  