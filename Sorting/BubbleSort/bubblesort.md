# Bubble Sort

## Working Principle
Bubble Sort is a simple comparison-based sorting algorithm. It works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order.

Each pass through the array "bubbles up" the largest element to its correct position at the end of the list. The process is repeated for all remaining elements until the entire array is sorted.

---

## Time Complexity

| Case | Complexity | Explanation |
|------|-------------|--------------|
| **Best Case** | O(n) | Occurs when the array is already sorted, only one pass is needed if optimized with a swap flag. |
| **Average Case** | O(n²) | On average, each element is compared with many others in multiple passes. |
| **Worst Case** | O(n²) | Occurs when the array is sorted in reverse order, requiring maximum swaps. |

---

## Space Complexity

| Type | Complexity | Explanation |
|------|-------------|--------------|
| **Auxiliary Space** | O(1) | Sorting is done in place, using only a constant amount of extra memory. |

---