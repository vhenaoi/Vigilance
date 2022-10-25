from relations_and_expert import graph_relations_and_expert
from reactivity import graph_reactivity
from individual import graph_individual
from relations import graph_relations
from expert import graph_expert

#group
Nold = ['Nold01','Nold03','Nold04','Nold05','Nold06','Nold07','Nold08']
ADMCI1 = ['Marseille11','Genova09','Thessaloniki17','Brescia01','Marseille01','Brescia17']
ADMCI2 =['Lille04','Brescia20','Brescia23','Genova02','Brescia26']
all = ['Nold01','Nold03','Nold04','Nold05','Nold06','Nold07','Nold08','Marseille11','Genova09','Thessaloniki17','Brescia01','Marseille01','Brescia17','Lille04','Brescia20','Brescia23','Genova02','Brescia26','Brescia33','Genova05','Leipzig01','Marseille07','Toulouse05']
all_true_alpha = ['Nold03','Nold04','Nold05','Nold06','Nold07','Nold08','Marseille11','Genova09','Thessaloniki17','Brescia01','Marseille01','Brescia17','Lille04','Brescia20','Brescia23','Brescia26']
new = ['Brescia33','Genova05','Leipzig01','Marseille07','Toulouse05']

#Channels
Marseille_ch = ['Fp1','Fp2','F7','F3','Fz','F4','F8','T7/T3','C3','Cz','C4','T8/T4','P7/T5','P3','Pz','P4','P8/T6','O1','O2']
Brescia_ch = ['P8/T6','T8/T4','F8','O2','P4','C4','F4','Fp2','Pz','Cz','Fz','O1','P3','C3','F3','Fp1','P7/T5','T7/T3','F7']
Lille_ch =	['Fp1','Fp2','F7','F3','Fz','F4','F8','T7/T3','C3','Cz','C4','T8/T4','P7/T5','P3','Pz','P4','P8/T6','O1','O2']
Salinicco_ch =	['Fp1','Fp2','F3','F4','C3','C4','P3','P4','O1','O2','F7','F8','T7/T3','T8/T4','P7/T5','P8/T6','Fz','Cz','Pz']
Genova_ch = ['Fp2','F4','C4','P4','O2','F8','T8/T4','P8/T6','Fp1','F3','C3','P3','O1','F7','T7/T3','P7/T5','Fz','Cz','Pz']
Nold_ch =	['Fp1','Fp2','F7','F3','Fz','F4','F8','T7/T3','C3','Cz','C4','T8/T4','P7/T5','P3','Pz','P4','P8/T6','O1','O2']


#bands - sheet_name_bands: Relations
alpha_theta = ['alpha/delta']
alpha_deltatheta = ['alpha/deltatheta']
alpha_theta = ['alpha/theta']
all_bands = ['alpha/deltatheta','alpha/theta','alpha/delta']

reactivity =  ['EC','EO']
Ch_Post = ['EO','C3','Cz','C4','P3','Pz','P4','O1','O2']
BandsWDN1 = ['W','D','N1']

#bands ind - sheet_name_bands: Individual bands
alpha = ['alpha','alpha2']
alpha2 = ['alpha2']
delta = ['delta']
theta = ['theta']
deltatheta = ['deltatheta']
beta = ['beta']
gamma = ['gamma']
all_ind_bands = ['alpha','alpha2','delta','theta','deltatheta','beta','gamma']

#sheet_name_bands
#'Individual bands'
sbj_post = 'SBJ Post'
sbj_global = 'SBJ Global'
sbj_1ch = 'SBJ 1ch'
#'Reactivity'
reactivity_post = 'Reactivity Post'
reactivity_global = 'Reactivity Global'
True_alpha = 'Vigilance3minEC_Rest1minEO'
rest_alpha = 'Rest3minEC_Rest1minEO'
WDN1 = 'WDN1'
#'Relations'
relations_post = 'Relations Post'
relations_global = 'Relations Global'
relations_1ch = 'Relations 1ch'
#'Expert'
#path = r"C:\Users\Paperino\Desktop\Veronica\Vigilance\Sleep.xlsx"
path=r'Sleep.xlsx'
sheet_name="Grafico"

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

##Multi_Input 
#sheet_name_bands = True_alpha
##sheet_name_bands = reactivity_global
#sheet_name_bands = rest_alpha
#sheet_name_bands = WDN1
##sheet_name_bands = sbj_post
###for b in alpha:
###    bands = [b]
###bands = Ch_Post
#bands = BandsWDN1
##bands = all_ind_bands
##m=['Nold09','Nold10','Nold11','Nold12','Nold13','Nold14']
##for sbj in m:
#group = ['Nold09']
#opcion('Reactivity')
##opcion('Individual bands')


#Input
'''sheet_name_bands = True_alpha
bands = reactivity
group = ['Marseille11']
opcion('Reactivity')'''

##Input Expert
#sheet_name_bands = sbj_1ch
#sheet_name_bands = relations_1ch
#sheet_name_bands = sbj_post
#sheet_name_bands = relations_post
sheet_name_bands = sbj_global
##sheet_name_bands = reactivity_post
#bands = ['alpha_1ch','alpha2_1ch']
#bands = all_bands
bands = ['alpha','alpha2']
##bands = reactivity
group = ['Nold10']
opcion('Relations and Expert')
#opcion('Individual bands')
##opcion('Reactivity')