import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {u'stratifying_var': np.random.uniform(0, 100, 20),
     u'price': np.random.normal(100, 5, 20)})

df[u'quartiles'] = pd.qcut(
    df[u'stratifying_var'],
    4,
    labels=[u'0-25%', u'25-50%', u'50-75%', u'75-100%'])

# 绘制箱体图
df.boxplot(column=u'price', by=u'quartiles')
plt.show()
