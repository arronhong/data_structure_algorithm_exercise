def binary_search(arr, target):
	low = 0
	high = len(arr) - 1
	while low <= high:
		mid = low + ((high - low) // 2)
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return None


if __name__ == '__main__':
	test_cases = [
		(([0, 5, 7, 10, 15], 5), 1),
		(([0, 5, 7, 10, 15], 11), None), 
		(([0, 5, 7, 10, 15], 15), 4), 
		(([0, 5, 7, 10, 15], 0), 0),
	]
	for (arr, tar), exp in test_cases:
    	assert exp == binary_search(arr, tar)
