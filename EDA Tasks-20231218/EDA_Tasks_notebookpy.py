# %%
import pandas as pd
import seaborn as sns
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore") 
import sys

# %%
sys.path.append(r"C:\Users\barc\Dropbox (Weizmann Institute)\MSc_Weizmann\FGS_ML\ML_Project\pyScripts")
from Main_EDA import SeeTheData
# %%

DirPath = os.getcwd()
DataPath = os.path.join(DirPath,'AmesHousing.csv')
df = pd.read_csv(DataPath) 
display("df.describe:",df.describe())
display("---------------------------")
display("df.info:",(df.info()))
display("---------------------------")
display("df.head:",df.head())
display("---------------------------")
display("df.shape:",df.shape)


# %%
data = df[["SalePrice","PID","Lot Frontage"]]
data.dropna()

# %%
numerical = [
  'SalePrice', 'Lot Area', 'Overall Qual', 'Overall Cond', '1st Flr SF', '2nd Flr SF', 'Bedroom AbvGr']

categorical = [
  'MS Zoning', 'Lot Shape', 'Neighborhood', 'Central Air', 'Sale Condition', 'Mo Sold', 'Yr Sold']


# %%
housing = df[numerical + categorical]
housing.info()

# %%
sns.set(style= "whitegrid", palette="pastel", font_scale=1.1,
        rc={"figure.figsize": [8,5]})

sns.distplot(housing['SalePrice'], norm_hist=False, kde=False, bins=20, hist_kws={"alpha": 1}
).set(xlabel='Sale Price', ylabel='Count');

# housing[numerical].hist(figsize=(15,15), bins= 20 , layout= (3,4));
# %%
sns.countplot(housing[categorical]['MS Zoning'])
# %%
housing[categorical]
for i in housing[categorical]:
    sns.countplot(i)