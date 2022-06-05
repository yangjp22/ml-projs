# coding = utf-8
import numpy as np

"""
函数说明:按照给定特征划分数据集,因为一旦确定了某一列的值作为根节点时，就需要将其删除，找剩下的列继续计算

Parameters:
    dataSet - 待划分的数据集
    axis - 划分数据集的第index个特征
    value - 需要返回的第index个特征的值等于value
Returns:
    无
"""
def splitDataSet(dataSet, axis, value):

	retDataSet1 = dataSet[dataSet[:, axis] == value, 0: axis]
	retDataSet2 = dataSet[dataSet[:, axis] == value, axis + 1 :]

	retDataSet = np.concatenate((retDataSet1, retDataSet2), axis = 1)

	return retDataSet
