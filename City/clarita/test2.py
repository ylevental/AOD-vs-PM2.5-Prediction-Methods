import pandas as pd

df = pd.read_csv("US_LosAngeles-LongBeach-SantaAna_SantaClarita.MOD04.csv")
df["Time"] = 1
df.to_csv('US_LosAngeles-LongBeach-SantaAna_SantaClarita.MOD04.csv', index=False)
