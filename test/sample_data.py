import pandas as pd 
df = pd.read_csv('x.csv')
df_sample = df.sample(n=100)
print(df.head(10))

df_sample.to_csv('brl_sample.csv')