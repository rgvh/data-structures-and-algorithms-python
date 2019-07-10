Challenge 02 - Array Shift
Challenge
Given an array (list) and a number as arguments, return a list with the number inserted in the middle of a list without using any built-in methods.

Approach & Efficiency
Find the middle index of the list for both even and odd lenghts, split the list into two halves, append the number to the end of the first half, and joint the lists together.

Efficiency: O(N) - Since a loop is used, the efficieny of the function follows a linear path as inputs increase.

Solution
![solution code]https://github.com/rgvh/data-structures-and-algorithms-python/blob/array_reverse/assets/array_shift.jpg

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