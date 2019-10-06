#recursive binarySearch
def recBinarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, lo, high):
	if high==lo:
		if array[high]==target:
			return high
		else:
			return -1

	mid = lo+int((high-lo)/2)
	
	if array[mid]==target:
		return mid
	
	if target > array[mid]:
		return binarySearchHelper(array, target, mid+1, high)
	else:
		return binarySearchHelper(array, target, lo, mid-1)
		
#iterative binarySearch
def iterativeBinarySearch(array, target):
	start=0
	end=len(array)-1
	
	while start <= end:
		mid = (start+end)//2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			end=mid-1
		else:
			start=mid+1
	
	return -1