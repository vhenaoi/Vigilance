import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path = r"C:\Users\Paperino\Desktop\Veronica\Vigilance\Gp.xlsx"
sheet_name = "ADMCI"

df = pd.read_excel(path,sheet_name=sheet_name)
fig, ax = plt.subplots()
df_violin = [df[df['segm']=='segm1']['alpha/delta'],df[df['segm']=='segm2']['alpha/delta'],df[df['segm']=='segm3']['alpha/delta'],df[df['segm']=='segm4']['alpha/delta'],df[df['segm']=='segm5']['alpha/delta'],df[df['segm']=='segm6']['alpha/delta'],df[df['segm']=='segm7']['alpha/delta']]
ax.violinplot(df_violin,showmedians=True)
plt.ylim(-2,8)


#sns.catplot(x='segm',y='alpha/theta',data=df,kind="swarm",legend=True,hue='sbj')
sns.catplot(x='segm',y='alpha/theta',data=df,kind="violin",legend=False,color='0.9',inner=None,order=['segm1','segm2','segm3','segm4','segm5','segm6','segm7'])
#sns.pointplot(x='segm',y='alpha/theta', data=df,scale=0.3,order=['segm1','segm2','segm3','segm4','segm5','segm6','segm7'],color='black',markers="+")
sns.pointplot(x='segm',y='alpha/theta', data=df.groupby('segm', as_index=False).median(),scale=0.3,order=['segm1','segm2','segm3','segm4','segm5','segm6','segm7'],color='red')
sns.pointplot(x='segm',y='alpha/theta', data=df,scale=0.05,order=['segm1','segm2','segm3','segm4','segm5','segm6','segm7'],hue='sbj',color='grey')
#sns.boxplot(x='segm',y='alpha/theta', data=df, width=0.01, showfliers=False)
sns.swarmplot(data=df, x='segm',y='alpha/theta', size=3,hue='sbj',order=['segm1','segm2','segm3','segm4','segm5','segm6','segm7'])
plt.legend(loc = "upper center",ncol=6,bbox_to_anchor=(1.5, 1.5))
plt.ylim(-2,8)
plt.show()
