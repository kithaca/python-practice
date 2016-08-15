def merge_sort(li):
	if len(li) <= 1:
		return li

	mid = len(li) / 2
	left = li[0:mid]
	right = li[mid:]

	return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
	merged = []
	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			merged.append(left.pop(0))
		else:
			merged.append(right.pop(0))

	return merged + left + right

print merge_sort([])
print merge_sort([1])
print merge_sort([1, 3, 2])
print merge_sort([4, 3, 2, 1])

li = [3, 1, 4, 6, 9, 10, 2, 7, 8, 5]
print merge_sort(li)
