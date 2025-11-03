# Insertion Sort

## Working Principle
Insertion Sort is a simple sorting algorithm that works similarly to how people sort playing cards in their hands. It builds the final sorted array one element at a time by repeatedly taking the next unsorted element and inserting it into the correct position among the already sorted elements.

The algorithm starts by assuming that the first element is already sorted. It then picks the next element and compares it with the elements before it, shifting larger elements one position to the right to make space for the new element. This process continues until all elements are sorted.

---

## Time Complexity

| Case | Complexity | Explanation |
|------|-------------|--------------|
| **Best Case** | O(n) | Occurs when the array is already sorted; only one comparison per element is needed. |
| **Average Case** | O(n²) | Each new element is compared with about half of the sorted part on average. |
| **Worst Case** | O(n²) | Occurs when the array is sorted in reverse order; every element must be compared with all others. |

---

## Space Complexity

| Type | Complexity | Explanation |
|------|-------------|--------------|
| **Auxiliary Space** | O(1) | Sorting is done in place, requiring only a constant amount of extra memory. |

---  
