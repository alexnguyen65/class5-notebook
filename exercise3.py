import pandas as pd
insurance_df = pd.read_csv(filepath_or_buffer='insurance.csv',
                           sep=',',
                           header=0)
#print(insurance_df)
print(insurance_df.to_string())
print(insurance_df.columns)
print(insurance_df.index)
print(insurance_df.dtypes)
print(insurance_df.shape)
print(insurance_df.info())
print(insurance_df.describe())

print(insurance_df['age'])
print(insurance_df[['age','children','charges']])
tempo = insurance_df[['age','children','charges']]
print(tempo[:5])

print("Mean:")
print(insurance_df['charges'].mean)


