Challenge 03 - Array Binary Search
Challenge
Given a sorted array (list) and a number as a key, without using any built-in methods, return the index position of an element that matches the key.  If there is no match in the list, return -1.

Approach & Efficiency
Find the middle index of the list, then check if the key matches the value at the middle index.  If it does return the index.  If the value doesn't match the key, retry the search on the first half if the key is less than the midpoint, or the second half if the key is greater than the midpoint.  Each recursion, will reduce the search by half. If no match is found in the list, return -1.

Efficiency: Big O(logn) - The function is a binary search and follows a natural log efficiency pattern.

Solution
![solution code]https://github.com/rgvh/data-structures-and-algorithms-python/blob/array_binary_search/assets/array_binary_search.jpg

The whiteboarded coded did not run correctly for each test.  I referred to https://www.sanfoundry.com/python-program-implement-binary-search-without-recursion/ for hints.

Checklist
- [x] Top-level README “Table of Contents” is updated
 - [x] Feature tasks for this challenge are completed
 - [x] Unit tests written and passing
     - [x] “Happy Path” - Expected outcome
     - [x] Expected failure
     - [ ] Edge Case (if applicable/obvious)
 - [x] README for this challenge is complete
     - [x] Summary, Description, Approach & Efficiency, Solution
     - [x] Link to code
     - [x] Picture of whiteboard