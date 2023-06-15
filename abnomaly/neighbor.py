from sklearn.neighbors import LocalOutlierFactor
import pandas as pd


# 创建DataFrame对象data，包含待处理的数据列
data = pd.DataFrame({'column': [8,8,8,8,8,1,1,1,1,1,1,1,8,1,1,1,1,8,8,8,8,8]})

# 创建LOF模型，设定邻近点数量和阈值
lof = LocalOutlierFactor(n_neighbors=1, contamination=0.1)

# 计算LOF值
lof_scores = lof.fit_predict(data[['column']])
print(lof_scores)
# 根据LOF值进行过滤
filtered_data = data[lof_scores > 0]
print(filtered_data)
