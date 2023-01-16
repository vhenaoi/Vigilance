from vigilance import graphic
from vigilance import select_color

def graph_relations_and_expert(num,path,sheet_name,sheet_name_bands,group,bands):
    c=select_color(num,path,sheet_name)
    #path_bands = r"C:\Users\Paperino\Desktop\Veronica\Vigilance\Gp.xlsx"
    path_bands = 'Gp.xlsx'
    sheet_name_bands = sheet_name_bands
    group = group
    bands = bands
    size = 18
    legend = True
    tren = True
    plot = True
    status = 'Relations and Expert'
    title = sheet_name_bands
    graphic(path=path,sheet_name=sheet_name,path_bands=path_bands,sheet_name_bands=sheet_name_bands,size=size, legend=legend, tren=tren, plot=plot, group=group,status=status,bands=bands,title=title,c=c)
