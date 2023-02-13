from relations_and_expert import graph_relations_and_expert
from reactivity import graph_reactivity
from individual import graph_individual
from relations import graph_relations
from expert import graph_expert
import os

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
WDN = 'WDN'
WRD = 'WRD'
Vertex = 'Vertex'
#'Relations'
relations_post = 'Relations Post'
relations_global = 'Relations Global'
relations_1ch = 'Relations 1ch'
#'Expert'
path=os.getcwd()+r'\files\Sleep.xlsx'
sheet_name="Grafico"

def opcion(num,op,sheet_name_bands,bands,group):
    if op == 'Individual bands':
        graph_individual(num,path,sheet_name,sheet_name_bands,bands,group)
    #elif op == 'Relations':
        #graph_relations(path,sheet_name,sheet_name_bands,group,bands)
    elif op == 'Qualitative':
        graph_expert(num,path,sheet_name,sheet_name_bands,bands,group)
    elif op == 'Reactivity':
        graph_reactivity(num,path,sheet_name,sheet_name_bands,bands,group)
    elif op == 'Quantitative and Qualitative':
        graph_relations_and_expert(num,path,sheet_name,sheet_name_bands,bands,group)

def _verf_bands(bands):
    #bands - sheet_name_bands: Relations
    if bands == 'alpha_theta':
        bands = ['alpha/delta']
    if bands == 'alpha_deltatheta':
        bands = ['alpha/deltatheta']
    if bands == 'alpha_delta':
        bands = ['alpha/delta']
    if bands == 'all_bands':
        bands = ['alpha/deltatheta','alpha/theta','alpha/delta']
    if bands == 'reactivity':
        bands = ['EC','EO']
    if bands == 'Ch_Post':
        bands = ['EO','C3','Cz','C4','P3','Pz','P4','O1','O2']
    if bands == 'BandsWDN1':
        bands = ['Wakefulness','Ripples','Diffuse Theta','Diffuse Theta + Vertex','K complexes +-','Diffuse Theta Before N1']
    if bands == 'BandsWDN':
        bands = ['Wakefulness','Ripples','Diffuse Theta','Diffuse Theta + Vertex','K complexes +-']
    if bands == 'BandsWRD':
        bands = ['Wakefulness','Ripples','Diffuse Theta']
    if bands == 'Bipolar':
        bands = ['Fp1-F7','F7-T7','T7-P7','P7-O1','Fp2-F8','F8-T8','T8-P8','Fp1-F3','F3-C3','C3-P3','P3-O1','Fp2-F4','F4-C4','C4-P4','P4-O2','Fz-Cz','Cz-Pz']        
    if bands == 'alpha':
        bands = ['alpha','alpha2']
    if bands == 'alpha_1ch':
        bands = ['alpha_1ch','alpha2_1ch']
    if bands == 'alpha2':
        bands = ['alpha2']
    if bands == 'delta':
        bands = ['delta']
    if bands == 'theta':
        bands = ['theta']
    if bands == 'deltatheta':
        bands = ['deltatheta']
    if bands == 'beta':
        bands = ['beta']
    if bands == 'gamma':
        bands = ['gamma']
    if bands == 'all_ind_bands':
        bands = ['alpha','alpha2','delta','theta','deltatheta','beta','gamma']
    if bands == 'Fz, Cz, Pz, O1O2':
        bands == ['Fz','Cz','Pz','O1O2']
    return bands

##Multi_Input 
def run_exe(num,sheet_name_bands,bands,group,graphics_name):
    group=[group.strip()]
    bands = _verf_bands(bands)
    if sheet_name_bands == 'True_alpha':
        sheet_name_bands = 'Vigilance3minEC_Rest1minEO'
    elif sheet_name_bands == 'Rest_alpha':
         sheet_name_bands = 'Rest3minEC_Rest1minEO'
    else:
        sheet_name_bands = sheet_name_bands
    opcion(int(num),graphics_name,sheet_name_bands,bands,group)


#sheet_name_bands = True_alpha
##sheet_name_bands = reactivity_global
#sheet_name_bands = rest_alpha

#sheet_name_bands = Vertex
##sheet_name_bands = sbj_post
###for b in alpha:
###    bands = [b]
###bands = Ch_Post

#bands = Bipolar
##bands = all_ind_bands
##m=['Nold09','Nold10','Nold11','Nold12','Nold13','Nold14']
##for sbj in m:

#opcion('Reactivity')



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
#sheet_name_bands = sbj_global
#sheet_name_bands = reactivity_post
#bands = ['alpha_1ch','alpha2_1ch']
#bands = all_bands
#bands = ['alpha','alpha2']
#bands = reactivity
#group = ['Nold14']
#opcion('Relations and Expert')
#opcion('Individual bands')
#opcion('Reactivity')