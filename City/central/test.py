import pandas as pd

df = pd.read_csv("ET_AddisAbaba_USDiplomaticPost:AddisAbabaCentral.MOD04.csv")
df["Time"] = 1
df.to_csv('ET_AddisAbaba_USDiplomaticPost:AddisAbabaCentral.MOD04.csv', index=False)
df = pd.read_csv("ET_AddisAbaba_USDiplomaticPost:AddisAbabaCentral.MYD04.csv")
df["Time"] = 2
df.to_csv('ET_AddisAbaba_USDiplomaticPost:AddisAbabaCentral.MYD04.csv', index=False)
