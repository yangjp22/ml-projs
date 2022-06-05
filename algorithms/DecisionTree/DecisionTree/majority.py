# coding = utf- 8
import operator

"""
函数说明:统计classList中出现此处最多的元素(类标签)

Parameters:
    classList - 类标签列表
Returns:
    sortedClassCount[0][0] - 出现此处最多的元素(类标签)

"""
def majorityCnt(classList):
	# 统计classList中每个元素出现的次数
	classCount = {}

	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote] = 0
		classCount[vote] += 1
		# classCount[vote] = classCount.get(vote, 0) + 1

	# classCount = collections.Counter(classList)

	# 根据字典的值降序排序
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
	# 返回classList中出现次数最多的元素
	return sortedClassCount[0][0]

if __name__ == '__main__':
	string = 'qeqreqrqdafareqwerqadfa'
	print(majorityCnt(list(string)))