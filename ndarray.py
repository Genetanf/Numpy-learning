# 載入 numpy 套件
import numpy as np
# 建立一維陣列
# data=np.array([3,2,6,4,])
# print(data)
# data=np.empty(4)    # 創造一個有四個資料的一維陣列，資料未指定
# print(data)
# data=np.zeros(3)    
# print(data)
# data=np.ones(3)
# print(data)
# data=np.arange(5)
# print(data)


# 建立二維陣列
# data=np.array([     # 創造一個 3x3 的二維陣列
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# print(data)
# data=np.empty([3,3])    # 創造一個 3x3 的二維陣列，資料未指定
# print(data)
# data=np.ones([3,3])
# print(data)

# 建立三維陣列
# data=np.array([
#     [
#         [3,1],[2,4]
#     ],
#     [
#         [5,4],[6,7]
#     ]
# ])
# print(data)


# 建立高維(四維)陣列
data=np.array([     # 創造一個 1x1x2x2 的四維陣列
    [
        [
            [3,4],[5,6]
        ]
    ]
])
print(data)
data=np.ones([2,1,1,3])
print(data)