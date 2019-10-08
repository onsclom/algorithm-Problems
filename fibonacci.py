# #slow O(2^n) solution
# def getNthFib(n):
#     if n == 1:
# 		return 0
# 	elif n == 2:
# 		return 1
# 	else:
# 		return getNthFib(n-1)+getNthFib(n-2)
	
#dynamic programming solution O(n), but bad space
# memo = {1:0, 2:1}
# def getNthFib(n):
# 	if n not in memo:
# 		memo[n] = getNthFib(n-1)+getNthFib(n-2)
# 	return memo[n]

#can still eliminate some memory by only keeping last two numbers!!!
def getNthFib(n):
	cur=1
	val=0
	first, second = 0, 1
	while cur <= n:
		if cur == 2:
			val=1
		elif cur > 2:
			val=first+second
			first = second
			second = val
		cur+=1
	return val
