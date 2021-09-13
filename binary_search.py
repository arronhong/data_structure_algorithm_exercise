def binary_search(arr, target):
	low = -1
	high = len(arr)
	while low < high - 1:
		mid = (low + high) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			low = mid
		else:
			high = mid
	return None
