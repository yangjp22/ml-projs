# coding = utf-8

from math import log
from dataGeneration import createDataSet

"""
函数说明:计算给定数据的经验熵(香农熵)

Parameters:
    dataSet - 数据集
Returns:
    shannonEnt - 经验熵(香农熵)

"""
def calcShannonEnt(dataSet):
	# 返回数据集的行数
	numEntires = len(dataSet)
	# 保存每个标签(Label)出现次数的字典
	labelCounts = {}
	# 对每组特征向量进行统计
	for featVec in dataSet:
		# 提取标签(Label)信息
		currentLabel = featVec[-1]
		# 如果标签(Label)没有放入统计次数的字典,添加进去
		if currentLabel not in labelCounts.keys():

			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1  # Label计数
		# labelCounts[currentLabel] = labelCounts.get(currentLabel, 0) + 1

	shannonEnt = 0.0  # 经验熵(香农熵)
	for key in labelCounts:  # 计算香农熵
		prob = float(labelCounts[key]) / numEntires  # 选择该标签(Label)的概率
		shannonEnt -= prob * log(prob, 2)  # 利用公式计算
	return shannonEnt  # 返回经验熵(香农熵)


if __name__ == '__main__':
	dataSet, features = createDataSet()
	print(dataSet)
	print(calcShannonEnt(dataSet))