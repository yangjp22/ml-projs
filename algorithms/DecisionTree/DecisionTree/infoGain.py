# coding = utf - 8

from shannonEntropy import calcShannonEnt
from dataGeneration import createDataSet
import numpy as np

'''
计算数据集的信息增益

Parameters : 两列，第一列为feature variable，第二列为target labels
Return: 在此feature variable下的信息增益

'''
def calcInfoGain(dataSet):
	# 统计所有数据量，计算prob（X = xi)
	length = len(dataSet)
	# 计算互信息
	mutualInfo = 0.0
	# 计算出初始时刻的信息熵
	baseEntropy = calcShannonEnt(dataSet)
	# 统计特征变量中的种类个数
	uniqueFeatures = list(set(dataSet[ :, 0]))

	# 对每个种类进行迭代
	for each in uniqueFeatures:
		# 用于存储筛选特定类别的数据
		interDataSet = []
		for row in dataSet:
			# 把满足某种类的行筛选出来
			if row[0] == each:
				interDataSet.append(row)
		# 计算筛选某类别下的信息熵
		interEntropy = calcShannonEnt(interDataSet)
		# 计算此类别的prob
		prob = len(interDataSet) / float(length)
		# 更新互信息
		mutualInfo += prob * interEntropy

	# 信息增益 = 初始信息熵 - 互信息
	infoGain = baseEntropy - mutualInfo

	return infoGain

if __name__ == '__main__':
	dataSet, features = createDataSet()
	num = dataSet.shape[1] - 1
	tules = []
	for i in range(num):
		newdata = np.concatenate((dataSet[:, i].reshape(-1 , 1), dataSet[:, -1].reshape(-1 , 1)), axis = 1)
		tule = calcInfoGain(newdata)
		tules.append(tule)
	print(tules)

