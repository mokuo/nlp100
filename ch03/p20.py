import pandas as pd

df = pd.read_json("./jawiki-country.json", orient="records", lines=True)
uk_df = df.query("title == 'イギリス'")
uk_text = uk_df.iloc[0]["text"]

with open("./uk.txt", mode="w") as f:
    f.write(uk_text)
