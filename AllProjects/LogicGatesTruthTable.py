def andgate(a,b):
	if a*b == 1:
		return 1
	else:
		return 0

def orgate(c,d):
	if c+d > 0:
		return 1
	else:
		return 0

def xorgate(e,f):
	if e+f == 1:
		return 1
	else:
		return 0

def nandgate(g,h):
	if g*h == 0:
		return 1
	else:
		return 0

def norgate(i,j):
	if i+j == 0:
		return 1
	else:
		return 0

def notgate(k):
	if k == 0:
		return 1
	else:
		return 0

def varA(it):
	if it % 2 == 0:
		return 1
	else:
		return 0

def varB(it):
	if it % 3 == 0 or it % 4 == 0:
		return 1
	else:
		return 0

def varC(it):
	if it in range(1,65,8) or it in range(2,65,8) or it in range(3,65,8) or it in range(4,65,8):
		return 0
	else:
		return 1

def varD(it):
	if it in range(1,65,16) or it in range(2,65,16) or it in range(3,65,16) or it in range(4,65,16) or it in range(5,65,16) or it in range(6,65,16) or it in range(7,65,16) or it in range(8,65,16):
		return 0
	else:
		return 1

def varE(it):
	if it in range(1, 17) or it in range(33, 49):
		return 0
	else:
		return 1

def varF(it):
	if it in range(1, 33):
		return 0
	else:
		return 1

def logicgate(it):
	y = nandgate(andgate(varA(it), varB(it)), norgate(orgate(varC(it), varD(it)), xorgate(varE(it), varF(it))))
	x = notgate(y)

	print(y, x)

if __name__ == "__main__":
	for x in range(1, 65):
		logicgate(x)











