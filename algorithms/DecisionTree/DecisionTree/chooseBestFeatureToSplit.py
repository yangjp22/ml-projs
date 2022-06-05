# conding = utf - 8

from infoGain import calcInfoGain
import numpy as np
from dataGeneration import createDataSet

def bestFeature(dataSet):

	# 统计总共的特征数目
	numColumn = dataSet.shape[1] - 1
	# 保存最好的列索引
	index = 0
	# 存储最大的信息增益
	maxInfoGain = 0.0

	for i in range(numColumn):
		newdata = np.concatenate((dataSet[:, i].reshape(-1, 1), dataSet[:, -1].reshape(-1, 1)), axis=1)
		interInfo = calcInfoGain(newdata)

		# 如果新的列的信息增益大于当前最大的信息增益， 则更新最大增益和想对应的索引
		if interInfo > maxInfoGain:
			index = i
			maxInfoGain = interInfo

	# 输出最大信息增益所对的列号
	return index

if __name__ == '__main__':
	dataSet, labels = createDataSet()
	final = bestFeature(dataSet)
	print(final)
