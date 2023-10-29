import pandas as pd

df = pd.read_parquet("./resources/name_tag.gzip")

print(df.head(5))
