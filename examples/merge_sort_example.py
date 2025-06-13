"""
Merge Sort – Divide and Conquer Example
"""

def merge(left, right):
    result = []
    i = j = 0
    # Merge two sorted lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted:", data)
    print("Sorted:  ", merge_sort(data))
