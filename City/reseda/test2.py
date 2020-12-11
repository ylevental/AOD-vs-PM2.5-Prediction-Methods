import pandas as pd

df = pd.read_csv("US_LosAngeles-LongBeach-SantaAna_Reseda.MYD04.csv")
df["Time"] = 2
df.to_csv('US_LosAngeles-LongBeach-SantaAna_Reseda.MYD04.csv', index=False)
