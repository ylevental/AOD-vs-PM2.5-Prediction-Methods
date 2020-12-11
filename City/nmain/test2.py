import pandas as pd

df = pd.read_csv("US_LosAngeles-LongBeach-SantaAna_LosAngeles-N.11.Mai.MOD04.csv")
df["Time"] = 1
df.to_csv('US_LosAngeles-LongBeach-SantaAna_LosAngeles-N.11.Mai.MOD04.csv', index=False)
