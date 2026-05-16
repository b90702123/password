import pandas as pd

data=pd.Series([1, 2, 3, 4, 5])
data.max()
data.median()
data.mean()
data.min()
data.sum()
data.std()
data.describe()
data.value_counts()
data.unique()
data.nunique()

data=pd.DataFrame({'A':[1, 2, 3], 'B':[4, 5, 6], 'C':[7, 8, 9]})
data.iloc[0]
data.loc[0]
data.iloc[0:2]
data.loc[0:2]
data['A']
data[['A', 'B']]
