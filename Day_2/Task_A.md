Date: 28-10-2026
Problem Statement

Write a Python function to remove duplicate elements from a list while preserving the order of their first occurrence.

Approach

I use a set to keep track of elements I have already seen and a list to store unique elements in their original order. If an element is new, I add it to both. If it already exists, I skip it.

Test Inputs and Outputs:
Input:
[1, 2, 2, 3, 1]
Output:
[1, 2, 3]

TC: O(n)
SC: O(n)