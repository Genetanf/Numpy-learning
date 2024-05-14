import numpy as np

# 逐元運算 (elementwise)
# data=np.array([3,2,10])
# data2=np.array([1,3,6])
# result=data+data2
# print("加法",result)
# result=data*data2
# print("乘法",result)
# result=data>data2
# print("大於",result)
# result=data==data2
# print("是否相等",result)

# 矩陣運算 (matrix)
# data=np.array([
#     [1,3]   # 1*2
# ])
# data2=np.array([
#     [2,-1,3],
#     [-2,4,1]    # 2*3
# ])

# result=data.dot(data2)  # 做內積，變 1*3 矩陣
# print("內積",result)

# result=data@data2   # 同樣做內積
# print("內積",result)

# result=np.outer(data,data2)     # 做外積，變 2*6 矩陣
# print("外積",result)


# 統計運算 (statistics)
data=np.array([
    [2,1,7],
    [-5,3,8]
])

# result=data.sum()
# print("總和",result)

# result=data.max()
# print("最大值",result)

# result=data.mean()
# print("平均數",result)

# result=data.std()
# print("標準差",result)

# result=data.sum(axis=0) # 針對欄做總和 column (針對第一個維度做總和)
# print("column sum:",result)

# result=data.sum(axis=1) # 針對列做總和 row (針對第二個維度做總和)
# print("row sum:",result)

# result=data.max(axis=0)
# print(result)

# result=data.mean(axis=1)
# print(result)

result=data.cumsum()    # 逐值累加，並記錄結果
print(result)

result=data.cumsum(axis=0)
print(result)