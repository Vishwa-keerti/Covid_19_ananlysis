import pandas as pd 
import matplotlib.pyplot as mpl 
df = pd.read_csv("StatewiseTestingDetails.csv")
 
df['Negative'] = pd.to_numeric(df['Negative'], errors='coerce') #To change dtype from object to float
df['Negative'] = df['Negative'].fillna(0)  #to replace NaN by 0 
df['Positive'] = df['Positive'].fillna(0)
# print(df.dtypes)

#plot of National Trend Over Time
national_daily = df.groupby('Date')[['Positive', 'Negative']].sum()
mpl.figure(figsize=(10,6))
mpl.plot(national_daily.index, national_daily['Positive'], label='Positive')
mpl.plot(national_daily.index, national_daily['Negative'], label='Negative')
mpl.xlabel("Date")
mpl.ylabel("TotalSamples")
mpl.title("COVID-19 Cases in India Over Time")
mpl.legend()
mpl.grid()
mpl.tight_layout()
mpl.show()
 

print(df.head())