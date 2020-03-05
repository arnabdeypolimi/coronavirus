import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("result_4_3_20.csv")

f, ax = plt.subplots(figsize=(18, 10))
# sns.lmplot('country','total',data=df[['country', 'total']])
sns.set()


cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
sns.scatterplot(x="country", y="new case",hue="recovered", size="total", cmap=cmap, sizes=(10, 200),data=df[['country','new case','recovered', 'total']])