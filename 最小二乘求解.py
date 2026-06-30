import numpy

def 最小二乘拟合(拟合因变量,拟合自变量):
	X矩阵 = None

	if (拟合因变量.ndim > 2):
		raise ValueError("拟合自变量应当为二维矩阵，而非shape={}".format(拟合自变量.shape))
	elif (拟合因变量.ndim == 1):
		拟合因变量 = 拟合因变量.reshape((拟合因变量.shape[0],1))

	if (拟合自变量.ndim > 2):
		raise ValueError("拟合自变量应当为二维矩阵，而非shape={}".format(拟合自变量.shape))
	elif (拟合自变量.ndim == 1):
		拟合自变量 = 拟合自变量.reshape((拟合自变量.shape[0],1))
	
	if (拟合因变量.shape[0] != 拟合自变量.shape[0]):
		raise ValueError("拟合变量个数不匹配（自变量shape={}，因变量shape={}）".format(拟合因变量.shape,拟合自变量.shape))
	
	##  print("拟合自变量")
	##  print(拟合自变量)
	##  print("拟合因变量")
	##  print(拟合因变量)

	自变量个数 = 拟合自变量.shape[1]
	因变量个数 = 拟合因变量.shape[1]
	
	拟合矩阵 = numpy.empty(shape=(因变量个数,自变量个数+1))

	X矩阵 = numpy.mat(numpy.hstack(tup=(numpy.ones(shape=(拟合自变量.shape[0],1)),拟合自变量)))
	##  print("X矩阵")
	##  print(X矩阵)
	A矩阵 = numpy.mat(X矩阵.transpose())*numpy.mat(X矩阵)
	##  print("A矩阵")
	##  print(A矩阵)
	A逆矩阵 = A矩阵.I
	##  print("A逆矩阵")
	##  print(A逆矩阵)
	##  print("X矩阵.transpose()")
	##  print(X矩阵.transpose())
	##  print("numpy.mat(拟合因变量)")
	##  print(numpy.mat(拟合因变量))

	拟合矩阵 = A逆矩阵 * X矩阵.transpose() * numpy.mat(拟合因变量)

	def 拟合函数(自变量序列):
		自变量组合序列 = numpy.hstack(tup=([1],自变量序列))
		#自变量组合序列 = numpy.mat(自变量组合序列).transpose()
		自变量组合序列 = numpy.mat(自变量组合序列)
		因变量序列 = 自变量组合序列*拟合矩阵
		return numpy.array(因变量序列)[0]

	return 拟合函数,拟合矩阵


if __name__=="__main__":
	##  a = numpy.array([1,2,3,4,5])
	##  b = a
	
	##  a = numpy.array([1,2,3,4,5])
	##  b = numpy.array([a,a+1]).transpose()

	##  a = numpy.array([[1,2,3,4,5],[10,4,6,8,2]])
	##  b = a[0]+a[1]
	##  a = a.transpose()

	a = numpy.array([[1,2,3,4,5],[10,4,6,8,2]])
	b = numpy.array([a[0]+a[1],a[1]-a[0]])
	a = a.transpose()
	b = b.transpose()

	拟合函数,拟合矩阵 = 最小二乘拟合(b,a)
	print("拟合矩阵")
	print(拟合矩阵)

	##  print("拟合函数(numpy.array([9]))")
	##  print(拟合函数(numpy.array([9])))
	print("拟合函数(numpy.array([9,10]))")
	print(拟合函数(numpy.array([9,10])))
