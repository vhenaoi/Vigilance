from vigilance import graphic
from vigilance import select_color


def graph_expert(num,path,sheet_name,sheet_name_bands,bands,group):
    c=None
    path_bands = None
    sheet_name_bands = sheet_name_bands
    group = group
    bands = bands
    size = 18
    legend = True
    tren = True
    plot = True
    status = ''
    title = sheet_name_bands
    graphic(num,path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size, legend=legend, tren=tren, plot=plot, group=group,status=status,bands=bands,title=title,c=c)