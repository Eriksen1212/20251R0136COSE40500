# Quick Sort

## 1. What Is Quick Sort?
Quick Sort is a divide-and-conquer sorting algorithm. It works by:
1. **Choosing a pivot** element from the array.  
2. **Partitioning** the other elements into two sub-arrays:
   - Left: elements less than the pivot  
   - Right: elements greater than (or equal to) the pivot  
3. **Recursively** applying the same process to the sub-arrays.

## 2. Time & Space Complexity
- **Average time:** O(n log n)  
- **Worst-case time:** O(n²) (when pivot is always min/max)  
- **Space:** O(log n) (recursive call stack)

## 3. In-place Partition Pseudocode

```text
function quick_sort(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quick_sort(A, low, p - 1)
        quick_sort(A, p + 1, high)

function partition(A, low, high):
    pivot = A[high]
    i = low
    for j from low to high - 1:
        if A[j] ≤ pivot:
            swap A[i] and A[j]
            i = i + 1
    swap A[i] and A[high]
    return i
