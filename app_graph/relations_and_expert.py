from vigilance import graphic
from vigilance import select_color
import os

def graph_relations_and_expert(num,path,sheet_name,sheet_name_bands,bands,group):
    c=select_color(path,sheet_name)
    #path_bands = r"C:\Users\Paperino\Desktop\Veronica\Vigilance\Gp.xlsx"
    path_bands = os.getcwd()+r'\files\Gp.xlsx'
    sheet_name_bands = sheet_name_bands
    group = group
    bands = bands
    size = 18
    legend = True
    tren = True
    plot = True
    status = 'Relations and Expert'
    title = sheet_name_bands
    graphic(num,path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size, legend=legend, tren=tren, plot=plot, group=group,status=status,bands=bands,title=title,c=c)
