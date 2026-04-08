
import pandas as pd

df = pd.DataFrame({'顏色': ['紅', '藍', '綠']})
one_hot = pd.get_dummies(df['顏色'])

print(one_hot)
