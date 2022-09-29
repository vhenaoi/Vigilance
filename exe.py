from relations_and_expert import graph_relations_and_expert
from reactivity import graph_reactivity
from individual import graph_individual
from relations import graph_relations
from expert import graph_expert

#group
Nold = ['Nold01','Nold03','Nold04','Nold05','Nold06']
ADMCI1 = ['Marseille11','Genova09','Thessaloniki17','Brescia01','Marseille01','Brescia17']
ADMCI2 =['Lille04','Brescia20','Brescia23','Genova2','Brescia26']

#bands
alpha_theta = ['alpha/delta']
alpha_deltatheta = ['alpha/deltatheta']
alpha_theta = ['alpha/theta']
all_bands = ['alpha/delta','alpha/deltatheta','alpha/theta']
reactivity =  ['OE','EO']
#bands ind
alpha = ['alpha']
alpha2 = ['alpha2']
delta = ['delta']
theta = ['theta']
deltatheta = ['deltatheta']
beta = ['beta']
gamma = ['gamma']

#sheet_name_bands
#'Individual bands'
sbj_post = 'SBJ Post'
sbj_global = 'SBJ Global'
#'Reactivity'
reactivity_post = 'Reactivity Post'
reactivity_global = 'Reactivity Global'
#'Relations'
relations_post = 'Relations Post'
relations_global = 'Relations Global'
#'Expert'
path = r"C:\Users\Paperino\Desktop\Veronica\Vigilance\Sleep.xlsx"
sheet_name="Grafico"

#Input
group = Nold
bands = alpha
sheet_name_bands = sbj_post

def opcion(op):
    if op == 'Individual bands':
        graph_individual(path,sheet_name,sheet_name_bands,group,bands)
    #elif op == 'Relations':
        #graph_relations(path,sheet_name,sheet_name_bands,group,bands)
    elif op == 'Expert':
        graph_expert(path,sheet_name,sheet_name_bands,group,bands)
    elif op == 'Reactivity':
        graph_reactivity(path,sheet_name,sheet_name_bands,group,bands)
    elif op == 'Relations and Expert':
        graph_relations_and_expert(path,sheet_name,sheet_name_bands,group,bands)

opcion('Relations and Expert')