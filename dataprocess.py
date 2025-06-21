import pandas as pd
df = pd.read_csv("parkinsons/parkinsons.data")

df.to_csv("parkinsons/parkinsons.csv", index=False)