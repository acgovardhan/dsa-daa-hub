# Merge Sort

## Working Principle
Merge Sort is a **divide-and-conquer** sorting algorithm that divides the array into smaller subarrays, sorts each subarray, and then merges them back together in sorted order.

The algorithm works as follows:
1. **Divide** the array into two halves until each subarray contains only one element.
2. **Conquer** by recursively sorting the subarrays.
3. **Combine** by merging the sorted subarrays to produce the final sorted array.

During the merge process, two sorted halves are compared element by element, and the smaller element is placed first, ensuring that the merged result remains sorted.

---

## Time Complexity

| Case | Complexity | Explanation |
|------|-------------|--------------|
| **Best Case** | O(n log n) | Even if the array is already sorted, it still divides and merges log(n) times. |
| **Average Case** | O(n log n) | Every split and merge operation takes logarithmic levels of depth and linear time complexity per level. |
| **Worst Case** | O(n log n) | Regardless of input order, the array is always divided and merged completely. |

---

## Space Complexity

| Type | Complexity | Explanation |
|------|-------------|--------------|
| **Auxiliary Space** | O(n) | Requires additional space for temporary arrays during merging. |

---