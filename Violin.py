import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path = r"E:\Academico\Universidad\Posgrado\Tesis\Paquetes\Vigilance\Gp.xlsx"
sheet_name = "Foglio2"

df = pd.read_excel(path,sheet_name=sheet_name)
#sns.catplot(x='segm',y='alpha/theta',data=df,kind="swarm",legend=True,hue='sbj')
sns.catplot(x='segm',y='alpha/theta',data=df,kind="violin",legend=False,color='0.9',inner=None)
#sns.pointplot(x='segm',y='alpha/theta', data=df.groupby('segm', as_index=False).median(),scale=0.3,order=['segm1','segm2','segm3','segm4','segm5','segm6','segm7'],color='black')
#sns.pointplot(x='segm',y='alpha/theta', data=df,scale=0.3,order=['segm1','segm2','segm3','segm4','segm5','segm6','segm7'],color='black',hue='sbj',legend=False)
#sns.boxplot(x='segm',y='alpha/theta', data=df, width=0.01, showfliers=False)
sns.swarmplot(data=df, x='segm',y='alpha/theta', size=3,hue='sbj',order=['segm1','segm2','segm3','segm4','segm5','segm6','segm7'])
plt.legend(loc = "upper center",ncol=6,bbox_to_anchor=(1.5, 1.5))
plt.show()
