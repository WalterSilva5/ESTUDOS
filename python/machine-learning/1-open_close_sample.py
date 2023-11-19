import pandas as pd
import quandl
qdata = quandl.get('WIKI/GOOGL')
df = pd.DataFrame(qdata)

print("first index: ", df.index[0])

print("keys: ", df.columns)

sum_total = lambda key: sum([x[0] for x in df[[key]].values])

keys = ["Open", "Close"]
for key in keys:
    print(f"[{key}] total: ", sum_total(key))
