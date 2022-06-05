# coding = utf - 8
from chooseBestFeatureToSplit import bestFeature
from majority import majorityCnt
from splitData import splitDataSet
from dataGeneration import createDataSet

"""
函数说明:创建决策树

Parameters:
    dataSet - 训练数据集
    labels - 分类属性标签
    featLabels - 存储选择的最优特征标签
Returns:
    myTree - 决策树

"""

def createTree(dataSet, labels, featLabels):
	# 取分类标签(是否放贷:yes or no)
	classList = [each[-1] for each in dataSet]

	'''
	两个结束条件，所有的target label都是一样，或者特征已经全部用完
	'''
	# 如果类别完全相同则停止继续划分
	if classList.count(classList[0]) == len(classList):
		return classList[0]

	# 遍历完所有特征时返回出现次数最多的类标签,此时数据集里面自有target labels
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)

	# 选择最优特征
	bestFeat = bestFeature(dataSet)
	#最优特征的标签
	bestFeatLabel = labels[bestFeat]
	featLabels.append(bestFeatLabel)

	# 根据最优特征的标签生成树
	myTree = {bestFeatLabel:{}}
	# 删除已经使用特征标签
	del(labels[bestFeat])

	# 得到训练集中所有最优特征的属性值
	featValues = [example[bestFeat] for example in dataSet]

	# 去掉重复的属性值
	uniqueVals = set(featValues)

	# 遍历此特征下的所有类别可取值，创建决策树。
	for value in uniqueVals:

		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), labels, featLabels)
	return myTree

if __name__ == '__main__':
	dataSet, labels = createDataSet()
	featLabels = []
	myTree = createTree(dataSet, labels, featLabels)
	print(myTree)
