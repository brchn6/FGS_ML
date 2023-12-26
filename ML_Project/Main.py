#%%
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


GETCWD = os.getcwd()  
PathToData = os.path.join(GETCWD + "\\diabetes+130-us+hospitals+for+years+1999-2008/diabetic_data.csv")

df = pd.read_csv(PathToData)
df
#%%

# sns.histplot(data=df, x="insulin", hue="age") 

sns.set(rc={'figure.figsize':(12,8)})
sns.histplot(data=df, x="race") 

# df.loc[1]
#%%
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="dark")

# Simulate data from a bivariate Gaussian
n = 10000
mean = [0, 0]
cov = [(2, .4), (.4, .2)]
x, y = df["discharge_disposition_id"] , df["admission_source_id"]

# Draw a combo histogram and scatterplot with density contours
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x=x, y=y, s=5, color=".15")
sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)