import pandas as pd

df = pd.read_csv("ET_AddisAbaba_USDiplomaticPost:AddisAbabaSchool.MYD04.csv")
df["Time"] = 2
df.to_csv('ET_AddisAbaba_USDiplomaticPost:AddisAbabaSchool.MYD04.csv', index=False)
