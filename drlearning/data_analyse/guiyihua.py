import csv
import pandas as pd
import numpy as np

readers = csv.reader(open('data/alldatainit.csv'))
a = []
for rowre in readers:
    a.append(rowre)
a = np.array(a, dtype='float32')
df_test = pd.DataFrame(a)
print(df_test)
df_test_1 = df_test
df_test_1 = (df_test_1 - df_test_1.min()) / (df_test_1.max() - df_test_1.min())
print(df_test_1)

df_test_1.to_csv("data/归一化.csv", encoding="utf-8", header=False, index=None)
