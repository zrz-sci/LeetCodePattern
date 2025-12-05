# LeetCode Pattern Study Plan

This repository is for studying LeetCode problems by classic patterns and mapping them to LeetCode (EN) and LeetCode China (CN) whenever there is a close match.

> Note: Some course-specific or custom problems do not have an exact LeetCode problem. For those, the problem is kept as a standalone exercise and links may be omitted or marked as "custom implementation".

---

## Patterns Overview

- [LeetCode Pattern Study Plan](#leetcode-pattern-study-plan)
  - [Patterns Overview](#patterns-overview)
  - [0. Warmup](#0-warmup)
  - [1. Pattern: Two Pointers](#1-pattern-two-pointers)
  - [2. Pattern: Fast \& Slow Pointers](#2-pattern-fast--slow-pointers)
  - [3. Pattern: Sliding Window](#3-pattern-sliding-window)
  - [4. Pattern: Merge Intervals](#4-pattern-merge-intervals)
  - [5. Pattern: Cyclic Sort](#5-pattern-cyclic-sort)
  - [6. Pattern: In-place Reversal of a Linked List](#6-pattern-in-place-reversal-of-a-linked-list)
  - [7. Pattern: Stacks](#7-pattern-stacks)
  - [8. Pattern: Monotonic Stack](#8-pattern-monotonic-stack)
  - [9. Pattern: Hash Maps](#9-pattern-hash-maps)
  - [10. Pattern: Tree BFS](#10-pattern-tree-bfs)
  - [11. Pattern: Tree DFS](#11-pattern-tree-dfs)
  - [12. Pattern: Two Heaps](#12-pattern-two-heaps)
  - [13. Pattern: Subsets](#13-pattern-subsets)
  - [14. Pattern: Modified Binary Search](#14-pattern-modified-binary-search)
  - [15. Pattern: Bitwise XOR](#15-pattern-bitwise-xor)
  - [16. Pattern: Top K Elements](#16-pattern-top-k-elements)
  - [17. Pattern: K-way Merge](#17-pattern-k-way-merge)
  - [18. Pattern: 0-1 Knapsack (DP)](#18-pattern-0-1-knapsack-dp)
  - [19. Pattern: Topological Sort (Graph)](#19-pattern-topological-sort-graph)
  - [20. Pattern: Union Find / Disjoint Set](#20-pattern-union-find--disjoint-set)
  - [21. Pattern: Graph BFS/DFS](#21-pattern-graph-bfsdfs)
  - [22. Pattern: Shortest Path (Dijkstra/ BFS)](#22-pattern-shortest-path-dijkstra-bfs)
  - [23. Pattern: Backtracking](#23-pattern-backtracking)
  - [24. Pattern: Matrix / Grid Traversal](#24-pattern-matrix--grid-traversal)
  - [25. Pattern: Prefix Sum \& Difference Array](#25-pattern-prefix-sum--difference-array)
  - [26. Pattern: Sweep Line](#26-pattern-sweep-line)
  - [27. Pattern: Trie](#27-pattern-trie)
  - [28. Pattern: Segment Tree / Binary Indexed Tree](#28-pattern-segment-tree--binary-indexed-tree)
  - [29. Pattern: Misc \& Test Your Knowledge](#29-pattern-misc--test-your-knowledge)

Below are the detailed problem lists for the first 30 patterns. For each problem, **EN** links to leetcode.com and **CN** links to leetcode.cn.

---

## 0. Warmup

- Contains Duplicate (easy) [LeetCode 217] --- [EN](https://leetcode.com/problems/contains-duplicate/) · [CN](https://leetcode.cn/problems/contains-duplicate/)

- Pangram (easy)  
	Note: use any pangram-check problem or implement your own. No specific LeetCode mapping.

- Reverse Vowels of a String (easy) [LeetCode 345] --- [EN](https://leetcode.com/problems/reverse-vowels-of-a-string/) · [CN](https://leetcode.cn/problems/reverse-vowels-of-a-string/)

- Valid Palindrome (easy) [LeetCode 125] --- [EN](https://leetcode.com/problems/valid-palindrome/) · [CN](https://leetcode.cn/problems/valid-palindrome/)

- Valid Anagram (easy) [LeetCode 242] --- [EN](https://leetcode.com/problems/valid-anagram/) · [CN](https://leetcode.cn/problems/valid-anagram/)

- Shortest Word Distance (easy) [LeetCode 243] --- [EN](https://leetcode.com/problems/shortest-word-distance/) · [CN](https://leetcode.cn/problems/shortest-word-distance/)

- Number of Good Pairs (easy) [LeetCode 1512] --- [EN](https://leetcode.com/problems/number-of-good-pairs/) · [CN](https://leetcode.cn/problems/number-of-good-pairs/)

- Sqrt (medium) – "Sqrt(x)" [LeetCode 69] --- [EN](https://leetcode.com/problems/sqrtx/) · [CN](https://leetcode.cn/problems/sqrtx/)

---

## 1. Pattern: Two Pointers

- Pair with Target Sum (easy) – similar to "Two Sum II - Input array is sorted" [LeetCode 167] --- [EN](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) · [CN](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)

- Find Non-Duplicate Number Instances (easy) – use "Single Number" as main practice [LeetCode 136] --- [EN](https://leetcode.com/problems/single-number/) · [CN](https://leetcode.cn/problems/single-number/)

- Squaring a Sorted Array (easy) [LeetCode 977] --- [EN](https://leetcode.com/problems/squares-of-a-sorted-array/) · [CN](https://leetcode.cn/problems/squares-of-a-sorted-array/)

- Triplet Sum to Zero (medium) – "3Sum" [LeetCode 15] --- [EN](https://leetcode.com/problems/3sum/) · [CN](https://leetcode.cn/problems/3sum/)

- Triplet Sum Close to Target (medium) – "3Sum Closest" [LeetCode 16] --- [EN](https://leetcode.com/problems/3sum-closest/) · [CN](https://leetcode.cn/problems/3sum-closest/)

- Triplets with Smaller Sum (medium)  
	Note: course-specific problem, implement as custom exercise.

- Dutch National Flag Problem (medium) – "Sort Colors" [LeetCode 75] --- [EN](https://leetcode.com/problems/sort-colors/) · [CN](https://leetcode.cn/problems/sort-colors/)

- Quadruple Sum to Target (Problem Challenge 1, medium) – "4Sum" [LeetCode 18] --- [EN](https://leetcode.com/problems/4sum/) · [CN](https://leetcode.cn/problems/4sum/)

- Comparing Strings containing Backspaces (Problem Challenge 2, medium) – "Backspace String Compare" [LeetCode 844] --- [EN](https://leetcode.com/problems/backspace-string-compare/) · [CN](https://leetcode.cn/problems/backspace-string-compare/)

- Minimum Window Sort (Problem Challenge 3, medium) – similar to "Shortest Unsorted Continuous Subarray" [LeetCode 581] --- [EN](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) · [CN](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/)

---

## 2. Pattern: Fast & Slow Pointers

- Linked List Cycle (easy) [LeetCode 141] --- [EN](https://leetcode.com/problems/linked-list-cycle/) · [CN](https://leetcode.cn/problems/linked-list-cycle/)

- Middle of the Linked List (easy) [LeetCode 876] --- [EN](https://leetcode.com/problems/middle-of-the-linked-list/) · [CN](https://leetcode.cn/problems/middle-of-the-linked-list/)

- Start of Linked List Cycle (medium) – "Linked List Cycle II" [LeetCode 142] --- [EN](https://leetcode.com/problems/linked-list-cycle-ii/) · [CN](https://leetcode.cn/problems/linked-list-cycle-ii/)

- Happy Number (medium) [LeetCode 202] --- [EN](https://leetcode.com/problems/happy-number/) · [CN](https://leetcode.cn/problems/happy-number/)

- Palindrome Linked List (Problem Challenge 1, medium) [LeetCode 234] --- [EN](https://leetcode.com/problems/palindrome-linked-list/) · [CN](https://leetcode.cn/problems/palindrome-linked-list/)

- Rearrange a Linked List (Problem Challenge 2, medium) – similar to "Reorder List" [LeetCode 143] --- [EN](https://leetcode.com/problems/reorder-list/) · [CN](https://leetcode.cn/problems/reorder-list/)

- Cycle in a Circular Array (Problem Challenge 3, hard) – "Circular Array Loop" [LeetCode 457] --- [EN](https://leetcode.com/problems/circular-array-loop/) · [CN](https://leetcode.cn/problems/circular-array-loop/)

---

## 3. Pattern: Sliding Window

- Maximum Sum Subarray of Size K (easy) [LeetCode 643] ("Maximum Average Subarray I") --- [EN](https://leetcode.com/problems/maximum-average-subarray-i/) · [CN](https://leetcode.cn/problems/maximum-average-subarray-i/)

- Smallest Subarray With a Greater Sum (easy)  
	Note: course-specific problem; implement your own sliding window solution for minimal-length subarray with sum ≥ target.

- Longest Substring with K Distinct Characters (medium)  
	Note: typical sliding window template; implement as custom problem (no exact LeetCode match).

- Fruits into Baskets (medium) [LeetCode 904] --- [EN](https://leetcode.com/problems/fruit-into-baskets/) · [CN](https://leetcode.cn/problems/fruit-into-baskets/)

- Longest Substring with Same Letters after Replacement (hard) – "Longest Repeating Character Replacement" [LeetCode 424] --- [EN](https://leetcode.com/problems/longest-repeating-character-replacement/) · [CN](https://leetcode.cn/problems/longest-repeating-character-replacement/)

- Longest Subarray with Ones after Replacement (hard) – similar to "Max Consecutive Ones III" [LeetCode 1004] --- [EN](https://leetcode.com/problems/max-consecutive-ones-iii/) · [CN](https://leetcode.cn/problems/max-consecutive-ones-iii/)

- Permutation in a String (Problem Challenge 1, hard) [LeetCode 567] --- [EN](https://leetcode.com/problems/permutation-in-string/) · [CN](https://leetcode.cn/problems/permutation-in-string/)

- String Anagrams (Problem Challenge 2, hard) – "Find All Anagrams in a String" [LeetCode 438] --- [EN](https://leetcode.com/problems/find-all-anagrams-in-a-string/) · [CN](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)

- Smallest Window containing Substring (Problem Challenge 3, hard) – "Minimum Window Substring" [LeetCode 76] --- [EN](https://leetcode.com/problems/minimum-window-substring/) · [CN](https://leetcode.cn/problems/minimum-window-substring/)

- Words Concatenation (Problem Challenge 4, hard) – "Substring with Concatenation of All Words" [LeetCode 30] --- [EN](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) · [CN](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/)

- Counting/Subarrays with Product Less than a Target (Problem Challenge 5/6, hard) – "Subarray Product Less Than K" [LeetCode 713] --- [EN](https://leetcode.com/problems/subarray-product-less-than-k/) · [CN](https://leetcode.cn/problems/subarray-product-less-than-k/)

---

## 4. Pattern: Merge Intervals

- Merge Intervals (medium) [LeetCode 56] --- [EN](https://leetcode.com/problems/merge-intervals/) · [CN](https://leetcode.cn/problems/merge-intervals/)

- Insert Interval (medium) [LeetCode 57] --- [EN](https://leetcode.com/problems/insert-interval/) · [CN](https://leetcode.cn/problems/insert-interval/)

- Intervals Intersection (medium) – "Interval List Intersections" [LeetCode 986] --- [EN](https://leetcode.com/problems/interval-list-intersections/) · [CN](https://leetcode.cn/problems/interval-list-intersections/)

- Conflicting Appointments (medium)  
	Note: use "Meeting Rooms" or "Meeting Rooms II" as close variants.  
	EN example: [EN](https://leetcode.com/problems/meeting-rooms-ii/) · [CN](https://leetcode.cn/problems/meeting-rooms-ii/)

- Minimum Meeting Rooms (Problem Challenge 1, hard) – "Meeting Rooms II" [LeetCode 253] --- [EN](https://leetcode.com/problems/meeting-rooms-ii/) · [CN](https://leetcode.cn/problems/meeting-rooms-ii/)

- Maximum CPU Load (Problem Challenge 2, hard)  
	Note: course-specific max-CPU-load interval problem; implement as custom exercise.

- Employee Free Time (Problem Challenge 3, hard) [LeetCode 759] --- [EN](https://leetcode.com/problems/employee-free-time/) · [CN](https://leetcode.cn/problems/employee-free-time/)

---

## 5. Pattern: Cyclic Sort

- Cyclic Sort (easy)  
	Note: template problem for cyclic sort; implement as custom exercise.

- Find the Missing Number (easy) – "Missing Number" [LeetCode 268] --- [EN](https://leetcode.com/problems/missing-number/) · [CN](https://leetcode.cn/problems/missing-number/)

- Find all Missing Numbers (easy) – "Find All Numbers Disappeared in an Array" [LeetCode 448] --- [EN](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) · [CN](https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/)

- Find the Duplicate Number (easy) – "Find the Duplicate Number" [LeetCode 287] --- [EN](https://leetcode.com/problems/find-the-duplicate-number/) · [CN](https://leetcode.cn/problems/find-the-duplicate-number/)

- Find all Duplicate Numbers (easy) – "Find All Duplicates in an Array" [LeetCode 442] --- [EN](https://leetcode.com/problems/find-all-duplicates-in-an-array/) · [CN](https://leetcode.cn/problems/find-all-duplicates-in-an-array/)

- Find the Corrupt Pair (Problem Challenge 1, easy) – similar to "Set Mismatch" [LeetCode 645] --- [EN](https://leetcode.com/problems/set-mismatch/) · [CN](https://leetcode.cn/problems/set-mismatch/)

- Find the Smallest Missing Positive Number (Problem Challenge 2, medium) – "First Missing Positive" [LeetCode 41] --- [EN](https://leetcode.com/problems/first-missing-positive/) · [CN](https://leetcode.cn/problems/first-missing-positive/)

- Find the First K Missing Positive Numbers (Problem Challenge 3, hard)  
	Note: course-specific problem; implement as custom exercise.

---

## 6. Pattern: In-place Reversal of a Linked List

- Reverse a Linked List (easy) [LeetCode 206] --- [EN](https://leetcode.com/problems/reverse-linked-list/) · [CN](https://leetcode.cn/problems/reverse-linked-list/)

- Reverse a Sub-list (medium) – "Reverse Linked List II" [LeetCode 92] --- [EN](https://leetcode.com/problems/reverse-linked-list-ii/) · [CN](https://leetcode.cn/problems/reverse-linked-list-ii/)

- Reverse every K-element Sub-list (medium) – "Reverse Nodes in k-Group" [LeetCode 25] --- [EN](https://leetcode.com/problems/reverse-nodes-in-k-group/) · [CN](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

- Reverse alternating K-element Sub-list (Problem Challenge 1, medium)  
	Note: course-specific variant; implement by modifying the k-group reverse logic.

- Rotate a Linked List (Problem Challenge 2, medium) – "Rotate List" [LeetCode 61] --- [EN](https://leetcode.com/problems/rotate-list/) · [CN](https://leetcode.cn/problems/rotate-list/)

---

## 7. Pattern: Stacks

- Balanced Parentheses (Problem 1, easy) – "Valid Parentheses" [LeetCode 20] --- [EN](https://leetcode.com/problems/valid-parentheses/) · [CN](https://leetcode.cn/problems/valid-parentheses/)

- Reverse a String (Problem 2, easy) – "Reverse String" [LeetCode 344] --- [EN](https://leetcode.com/problems/reverse-string/) · [CN](https://leetcode.cn/problems/reverse-string/)

- Decimal to Binary Conversion (Problem 3, medium)  
	Note: practice implementing decimal to binary using a stack; no specific LeetCode mapping.

- Next Greater Element (Problem 4, easy) – "Next Greater Element I" [LeetCode 496] --- [EN](https://leetcode.com/problems/next-greater-element-i/) · [CN](https://leetcode.cn/problems/next-greater-element-i/)

- Sorting a Stack (Problem 5, easy)  
	Note: practice problem to sort a stack using recursion/another stack.

- Simplify Path (Problem 6, medium) – "Simplify Path" [LeetCode 71] --- [EN](https://leetcode.com/problems/simplify-path/) · [CN](https://leetcode.cn/problems/simplify-path/)

---

## 8. Pattern: Monotonic Stack

- Remove Nodes From Linked List (easy)  
	Note: choose any linked list node-removal problem as practice, e.g. removing nodes that satisfy a condition.  
	Example: [EN](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) · [CN](https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)

- Remove All Adjacent Duplicates In String (easy) [LeetCode 1047] --- [EN](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) · [CN](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/)

- Next Greater Element (easy) – "Next Greater Element II" [LeetCode 503] --- [EN](https://leetcode.com/problems/next-greater-element-ii/) · [CN](https://leetcode.cn/problems/next-greater-element-ii/)

- Daily Temperatures (easy) [LeetCode 739] --- [EN](https://leetcode.com/problems/daily-temperatures/) · [CN](https://leetcode.cn/problems/daily-temperatures/)

- Remove All Adjacent Duplicates in String II (medium) [LeetCode 1209] --- [EN](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) · [CN](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string-ii/)

- Sum of Subarray Minimums (medium) [LeetCode 907] --- [EN](https://leetcode.com/problems/sum-of-subarray-minimums/) · [CN](https://leetcode.cn/problems/sum-of-subarray-minimums/)

- Remove K Digits (hard) [LeetCode 402] --- [EN](https://leetcode.com/problems/remove-k-digits/) · [CN](https://leetcode.cn/problems/remove-k-digits/)

---

## 9. Pattern: Hash Maps

- First Non-repeating Character (Problem 1, easy) – "First Unique Character in a String" [LeetCode 387] --- [EN](https://leetcode.com/problems/first-unique-character-in-a-string/) · [CN](https://leetcode.cn/problems/first-unique-character-in-a-string/)

- Largest Unique Number (Problem 2, easy) – "Largest Unique Number" [LeetCode 1133] --- [EN](https://leetcode.com/problems/largest-unique-number/) · [CN](https://leetcode.cn/problems/largest-unique-number/)

- Maximum Number of Balloons (Problem 3, easy) – "Maximum Number of Balloons" [LeetCode 1189] --- [EN](https://leetcode.com/problems/maximum-number-of-balloons/) · [CN](https://leetcode.cn/problems/maximum-number-of-balloons/)

- Longest Palindrome (Problem 4, easy) – "Longest Palindrome" [LeetCode 409] --- [EN](https://leetcode.com/problems/longest-palindrome/) · [CN](https://leetcode.cn/problems/longest-palindrome/)

- Ransom Note (Problem 5, easy) – "Ransom Note" [LeetCode 383] --- [EN](https://leetcode.com/problems/ransom-note/) · [CN](https://leetcode.cn/problems/ransom-note/)

---

## 10. Pattern: Tree BFS

- Level Order Traversal (easy) – "Binary Tree Level Order Traversal" [LeetCode 102] --- [EN](https://leetcode.com/problems/binary-tree-level-order-traversal/) · [CN](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

- Reverse Level Order Traversal (easy) – variation of "Binary Tree Level Order Traversal" [LeetCode 102] --- [EN](https://leetcode.com/problems/binary-tree-level-order-traversal/) · [CN](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

- Zigzag Traversal (medium) – "Binary Tree Zigzag Level Order Traversal" [LeetCode 103] --- [EN](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) · [CN](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)

- Level Averages in a Binary Tree (easy) – similar to "Average of Levels in Binary Tree" [LeetCode 637] --- [EN](https://leetcode.com/problems/average-of-levels-in-binary-tree/) · [CN](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)

- Minimum Depth of a Binary Tree (easy) [LeetCode 111] --- [EN](https://leetcode.com/problems/minimum-depth-of-binary-tree/) · [CN](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)

- Connect Level Order Siblings (medium) – similar to "Populating Next Right Pointers in Each Node" [LeetCode 116] --- [EN](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) · [CN](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

- Connect All Level Order Siblings (medium) – variation of the same idea as [LeetCode 116]; treat as custom exercise.

- Right View of a Binary Tree (medium) – "Binary Tree Right Side View" [LeetCode 199] --- [EN](https://leetcode.com/problems/binary-tree-right-side-view/) · [CN](https://leetcode.cn/problems/binary-tree-right-side-view/)

---

## 11. Pattern: Tree DFS

- Binary Tree Path Sum (easy) – "Path Sum" [LeetCode 112] --- [EN](https://leetcode.com/problems/path-sum/) · [CN](https://leetcode.cn/problems/path-sum/)

- All Paths for a Sum (medium) – similar to "Path Sum II" [LeetCode 113] --- [EN](https://leetcode.com/problems/path-sum-ii/) · [CN](https://leetcode.cn/problems/path-sum-ii/)

- Sum of Path Numbers (medium) – "Sum Root to Leaf Numbers" [LeetCode 129] --- [EN](https://leetcode.com/problems/sum-root-to-leaf-numbers/) · [CN](https://leetcode.cn/problems/sum-root-to-leaf-numbers/)

- Path With Given Sequence (medium) – custom DFS path-matching problem; implement as standalone exercise.

- Count Paths for a Sum (medium) – similar to "Path Sum III" [LeetCode 437] --- [EN](https://leetcode.com/problems/path-sum-iii/) · [CN](https://leetcode.cn/problems/path-sum-iii/)

---

## 12. Pattern: Two Heaps

- Find the Median of a Number Stream (hard) – "Find Median from Data Stream" [LeetCode 295] --- [EN](https://leetcode.com/problems/find-median-from-data-stream/) · [CN](https://leetcode.cn/problems/find-median-from-data-stream/)

- Sliding Window Median (hard) – "Sliding Window Median" [LeetCode 480] --- [EN](https://leetcode.com/problems/sliding-window-median/) · [CN](https://leetcode.cn/problems/sliding-window-median/)

- Maximize Capital (hard) – "IPO" [LeetCode 502] --- [EN](https://leetcode.com/problems/ipo/) · [CN](https://leetcode.cn/problems/ipo/)

---

## 13. Pattern: Subsets

- Subsets (easy) [LeetCode 78] --- [EN](https://leetcode.com/problems/subsets/) · [CN](https://leetcode.cn/problems/subsets/)

- Subsets With Duplicates (medium) – "Subsets II" [LeetCode 90] --- [EN](https://leetcode.com/problems/subsets-ii/) · [CN](https://leetcode.cn/problems/subsets-ii/)

- Permutations (medium) [LeetCode 46] --- [EN](https://leetcode.com/problems/permutations/) · [CN](https://leetcode.cn/problems/permutations/)

- String Permutations by Changing Case (medium) – "Letter Case Permutation" [LeetCode 784] --- [EN](https://leetcode.com/problems/letter-case-permutation/) · [CN](https://leetcode.cn/problems/letter-case-permutation/)

- Balanced Parentheses (hard) – "Generate Parentheses" [LeetCode 22] --- [EN](https://leetcode.com/problems/generate-parentheses/) · [CN](https://leetcode.cn/problems/generate-parentheses/)

- Unique Generalized Abbreviations (hard) – "Generalized Abbreviation" [LeetCode 320] --- [EN](https://leetcode.com/problems/generalized-abbreviation/) · [CN](https://leetcode.cn/problems/generalized-abbreviation/)

---

## 14. Pattern: Modified Binary Search

- Binary Search (easy) – template problem; use classic binary search on a sorted array.

- Order-agnostic Binary Search (easy) – custom variation handling both ascending/descending sorted arrays.

- Ceiling of a Number (medium) – find smallest element ≥ target in sorted array; treat as custom binary-search exercise.

- Next Letter (medium) – similar to "Find Smallest Letter Greater Than Target" [LeetCode 744] --- [EN](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) · [CN](https://leetcode.cn/problems/find-smallest-letter-greater-than-target/)

- Number Range (medium) – "Find First and Last Position of Element in Sorted Array" [LeetCode 34] --- [EN](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) · [CN](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

- Search in a Sorted Infinite Array (medium) – custom variant; simulate infinite array by growing search bounds.

- Minimum Difference Element (medium) – find element with minimum difference from target; custom binary-search-style exercise.

- Bitonic Array Maximum (medium) – "Peak Index in a Mountain Array" [LeetCode 852] --- [EN](https://leetcode.com/problems/peak-index-in-a-mountain-array/) · [CN](https://leetcode.cn/problems/peak-index-in-a-mountain-array/)

- Search Bitonic Array (hard) – search key in bitonic array; combine binary searches on increasing/decreasing parts (custom exercise).

- Search in a Rotated Array (hard) – "Search in Rotated Sorted Array" [LeetCode 33] --- [EN](https://leetcode.com/problems/search-in-rotated-sorted-array/) · [CN](https://leetcode.cn/problems/search-in-rotated-sorted-array/)

- Rotation Count (hard) – similar to finding pivot/rotation count in rotated sorted array (related to [LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)); treat as custom exercise.

---

## 15. Pattern: Bitwise XOR

- Single Number (easy) [LeetCode 136] --- [EN](https://leetcode.com/problems/single-number/) · [CN](https://leetcode.cn/problems/single-number/)

- Two Single Numbers (medium) – "Single Number III" [LeetCode 260] --- [EN](https://leetcode.com/problems/single-number-iii/) · [CN](https://leetcode.cn/problems/single-number-iii/)

- Complement of Base 10 Number (easy) – "Number Complement" [LeetCode 476] --- [EN](https://leetcode.com/problems/number-complement/) · [CN](https://leetcode.cn/problems/number-complement/)

---

## 16. Pattern: Top K Elements

- Top K Numbers (easy) – standard "k largest elements" heap exercise; can relate to "Kth Largest Element in an Array" [LeetCode 215] --- [EN](https://leetcode.com/problems/kth-largest-element-in-an-array/) · [CN](https://leetcode.cn/problems/kth-largest-element-in-an-array/)

- Kth Smallest Number (easy) – "Kth Smallest Element in a Sorted Matrix" [LeetCode 378] --- [EN](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) · [CN](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/)

- K Closest Points to the Origin (medium) [LeetCode 973] --- [EN](https://leetcode.com/problems/k-closest-points-to-origin/) · [CN](https://leetcode.cn/problems/k-closest-points-to-origin/)

- Connect Ropes (easy/medium) – similar to "Minimum Cost to Connect Sticks" [LeetCode 1167] --- [EN](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) · [CN](https://leetcode.cn/problems/minimum-cost-to-connect-sticks/)

- Top K Frequent Numbers (medium) – "Top K Frequent Elements" [LeetCode 347] --- [EN](https://leetcode.com/problems/top-k-frequent-elements/) · [CN](https://leetcode.cn/problems/top-k-frequent-elements/)

- Frequency Sort (medium) – "Sort Characters By Frequency" [LeetCode 451] --- [EN](https://leetcode.com/problems/sort-characters-by-frequency/) · [CN](https://leetcode.cn/problems/sort-characters-by-frequency/)

- Kth Largest Number in a Stream (medium) – "Kth Largest Element in a Stream" [LeetCode 703] --- [EN](https://leetcode.com/problems/kth-largest-element-in-a-stream/) · [CN](https://leetcode.cn/problems/kth-largest-element-in-a-stream/)

- 'K' Closest Numbers (medium) – custom variant; can be related to k-closest-elements-in-sorted-array style problems.

- Maximum Distinct Elements (medium) – custom problem using a heap and hash map; treat as standalone.

- Sum of Elements (medium) – custom exercise: sum elements between two ranks using heaps.

- Rearrange String (hard) – "Reorganize String" [LeetCode 767] --- [EN](https://leetcode.com/problems/reorganize-string/) · [CN](https://leetcode.cn/problems/reorganize-string/)

- Rearrange String K Distance Apart (hard) – "Rearrange String k Distance Apart" [LeetCode 358] --- [EN](https://leetcode.com/problems/rearrange-string-k-distance-apart/) · [CN](https://leetcode.cn/problems/rearrange-string-k-distance-apart/)

- Task Scheduler (hard) [LeetCode 621] --- [EN](https://leetcode.com/problems/task-scheduler/) · [CN](https://leetcode.cn/problems/task-scheduler/)

- Frequency Stack (hard) – similar idea to "Maximum Frequency Stack" [LeetCode 895] --- [EN](https://leetcode.com/problems/maximum-frequency-stack/) · [CN](https://leetcode.cn/problems/maximum-frequency-stack/)

---

## 17. Pattern: K-way Merge

- Merge K Sorted Lists (hard) [LeetCode 23] --- [EN](https://leetcode.com/problems/merge-k-sorted-lists/) · [CN](https://leetcode.cn/problems/merge-k-sorted-lists/)

- Kth Smallest Number in M Sorted Lists (medium) – custom variant using a min-heap over k sorted lists.

- Kth Smallest Number in a Sorted Matrix (medium) [LeetCode 378] --- [EN](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) · [CN](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/)

- Smallest Number Range (hard) – "Smallest Range Covering Elements from K Lists" [LeetCode 632] --- [EN](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) · [CN](https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/)

---

## 18. Pattern: 0-1 Knapsack (DP)

- 0-1 Knapsack (medium) – classic knapsack DP; can implement in 2D or 1D optimized form.

- Equal Subset Sum Partition (medium) – "Partition Equal Subset Sum" [LeetCode 416] --- [EN](https://leetcode.com/problems/partition-equal-subset-sum/) · [CN](https://leetcode.cn/problems/partition-equal-subset-sum/)

- Subset Sum (medium) – classic subset-sum DP; related to [LeetCode 416](https://leetcode.com/problems/partition-equal-subset-sum/).

- Minimum Subset Sum Difference (hard) – custom partition-difference DP; treat as standalone.

- Count of Subset Sum (hard) – count subsets achieving a given sum; custom extension of subset-sum DP.

- Target Sum (hard) [LeetCode 494] --- [EN](https://leetcode.com/problems/target-sum/) · [CN](https://leetcode.cn/problems/target-sum/)

- Can Partition Equal Subset Sum (review) – same as Equal Subset Sum Partition [LeetCode 416]; revisit as practice.

---

## 19. Pattern: Topological Sort (Graph)

- Topological Sort (medium) – classic Kahn's algorithm / DFS-based topo sort on DAG; treat as core pattern.

- Tasks Scheduling (medium) – generic course-schedule style problem using topological ordering.

- Tasks Scheduling Order (medium) – "Course Schedule II" [LeetCode 210] --- [EN](https://leetcode.com/problems/course-schedule-ii/) · [CN](https://leetcode.cn/problems/course-schedule-ii/)

- All Tasks Scheduling Orders (hard) – custom extension: enumerate all valid topological sorts.

- Minimum Height Trees (medium) [LeetCode 310] --- [EN](https://leetcode.com/problems/minimum-height-trees/) · [CN](https://leetcode.cn/problems/minimum-height-trees/)

---

## 20. Pattern: Union Find / Disjoint Set

- Graph Valid Tree (medium) – custom exercise; implement Union Find / BFS to check if an undirected graph is a tree. Closely related to connectivity + cycle detection.

- Number of Connected Components in an Undirected Graph (medium) – similar to standard connected-components counting via Union Find or DFS.

- Redundant Connection (medium) [LeetCode 684] --- [EN](https://leetcode.com/problems/redundant-connection/) · [CN](https://leetcode.cn/problems/redundant-connection/)

- Redundant Connection II (hard) [LeetCode 685] --- [EN](https://leetcode.com/problems/redundant-connection-ii/) · [CN](https://leetcode.cn/problems/redundant-connection-ii/)

- Number of Islands II (hard) [LeetCode 305] --- [EN](https://leetcode.com/problems/number-of-islands-ii/) · [CN](https://leetcode.cn/problems/number-of-islands-ii/)

- Accounts Merge (medium) [LeetCode 721] --- [EN](https://leetcode.com/problems/accounts-merge/) · [CN](https://leetcode.cn/problems/accounts-merge/)

---

## 21. Pattern: Graph BFS/DFS

- Number of Islands (medium) [LeetCode 200] --- [EN](https://leetcode.com/problems/number-of-islands/) · [CN](https://leetcode.cn/problems/number-of-islands/)

- Clone Graph (medium) [LeetCode 133] --- [EN](https://leetcode.com/problems/clone-graph/) · [CN](https://leetcode.cn/problems/clone-graph/)

- Max Area of Island (medium) [LeetCode 695] --- [EN](https://leetcode.com/problems/max-area-of-island/) · [CN](https://leetcode.cn/problems/max-area-of-island/)

- Surrounded Regions (medium) [LeetCode 130] --- [EN](https://leetcode.com/problems/surrounded-regions/) · [CN](https://leetcode.cn/problems/surrounded-regions/)

- Word Ladder (hard) [LeetCode 127] --- [EN](https://leetcode.com/problems/word-ladder/) · [CN](https://leetcode.cn/problems/word-ladder/)

- Word Ladder II (hard) [LeetCode 126] --- [EN](https://leetcode.com/problems/word-ladder-ii/) · [CN](https://leetcode.cn/problems/word-ladder-ii/)

---

## 22. Pattern: Shortest Path (Dijkstra/ BFS)

- Shortest Path in Binary Matrix (medium) [LeetCode 1091] --- [EN](https://leetcode.com/problems/shortest-path-in-binary-matrix/) · [CN](https://leetcode.cn/problems/shortest-path-in-binary-matrix/)

- Path With Minimum Effort (medium) [LeetCode 1631] --- [EN](https://leetcode.com/problems/path-with-minimum-effort/) · [CN](https://leetcode.cn/problems/path-with-minimum-effort/)

- Network Delay Time (medium) [LeetCode 743] --- [EN](https://leetcode.com/problems/network-delay-time/) · [CN](https://leetcode.cn/problems/network-delay-time/)

- Cheapest Flights Within K Stops (medium) [LeetCode 787] --- [EN](https://leetcode.com/problems/cheapest-flights-within-k-stops/) · [CN](https://leetcode.cn/problems/cheapest-flights-within-k-stops/)

- Maze / Shortest Path in Maze (medium) – custom exercise; BFS on grid with walls.

---

## 23. Pattern: Backtracking

- Combinations (medium) [LeetCode 77] --- [EN](https://leetcode.com/problems/combinations/) · [CN](https://leetcode.cn/problems/combinations/)

- Combination Sum (medium) [LeetCode 39] --- [EN](https://leetcode.com/problems/combination-sum/) · [CN](https://leetcode.cn/problems/combination-sum/)

- Combination Sum II (medium) [LeetCode 40] --- [EN](https://leetcode.com/problems/combination-sum-ii/) · [CN](https://leetcode.cn/problems/combination-sum-ii/)

- Palindrome Partitioning (medium) [LeetCode 131] --- [EN](https://leetcode.com/problems/palindrome-partitioning/) · [CN](https://leetcode.cn/problems/palindrome-partitioning/)

- N-Queens (hard) [LeetCode 51] --- [EN](https://leetcode.com/problems/n-queens/) · [CN](https://leetcode.cn/problems/n-queens/)

- Word Search (medium) [LeetCode 79] --- [EN](https://leetcode.com/problems/word-search/) · [CN](https://leetcode.cn/problems/word-search/)

---

## 24. Pattern: Matrix / Grid Traversal

- Spiral Matrix (medium) [LeetCode 54] --- [EN](https://leetcode.com/problems/spiral-matrix/) · [CN](https://leetcode.cn/problems/spiral-matrix/)

- Rotate Image (medium) [LeetCode 48] --- [EN](https://leetcode.com/problems/rotate-image/) · [CN](https://leetcode.cn/problems/rotate-image/)

- Game of Life (medium) [LeetCode 289] --- [EN](https://leetcode.com/problems/game-of-life/) · [CN](https://leetcode.cn/problems/game-of-life/)

- Set Matrix Zeroes (medium) [LeetCode 73] --- [EN](https://leetcode.com/problems/set-matrix-zeroes/) · [CN](https://leetcode.cn/problems/set-matrix-zeroes/)

- Flood Fill (easy) [LeetCode 733] --- [EN](https://leetcode.com/problems/flood-fill/) · [CN](https://leetcode.cn/problems/flood-fill/)

- Number of Enclaves (medium) [LeetCode 1020] --- [EN](https://leetcode.com/problems/number-of-enclaves/) · [CN](https://leetcode.cn/problems/number-of-enclaves/)

---

## 25. Pattern: Prefix Sum & Difference Array

- Range Sum Query - Immutable (easy) [LeetCode 303] --- [EN](https://leetcode.com/problems/range-sum-query-immutable/) · [CN](https://leetcode.cn/problems/range-sum-query-immutable/)

- Range Sum Query 2D - Immutable (medium) [LeetCode 304] --- [EN](https://leetcode.com/problems/range-sum-query-2d-immutable/) · [CN](https://leetcode.cn/problems/range-sum-query-2d-immutable/)

- Subarray Sum Equals K (medium) [LeetCode 560] --- [EN](https://leetcode.com/problems/subarray-sum-equals-k/) · [CN](https://leetcode.cn/problems/subarray-sum-equals-k/)

- Continuous Subarray Sum (medium) [LeetCode 523] --- [EN](https://leetcode.com/problems/continuous-subarray-sum/) · [CN](https://leetcode.cn/problems/continuous-subarray-sum/)

- Car Pooling (medium) [LeetCode 1094] --- [EN](https://leetcode.com/problems/car-pooling/) · [CN](https://leetcode.cn/problems/car-pooling/)

- Corporate Flight Bookings (medium) [LeetCode 1109] --- [EN](https://leetcode.com/problems/corporate-flight-bookings/) · [CN](https://leetcode.cn/problems/corporate-flight-bookings/)

---

## 26. Pattern: Sweep Line

- Meeting Rooms (easy) [LeetCode 252] --- [EN](https://leetcode.com/problems/meeting-rooms/) · [CN](https://leetcode.cn/problems/meeting-rooms/)

- Meeting Rooms II (medium) [LeetCode 253] --- [EN](https://leetcode.com/problems/meeting-rooms-ii/) · [CN](https://leetcode.cn/problems/meeting-rooms-ii/)

- Merge Intervals (medium) [LeetCode 56] --- [EN](https://leetcode.com/problems/merge-intervals/) · [CN](https://leetcode.cn/problems/merge-intervals/)

- Employee Free Time (hard) [LeetCode 759] --- [EN](https://leetcode.com/problems/employee-free-time/) · [CN](https://leetcode.cn/problems/employee-free-time/)

- Maximum Number of Events That Can Be Attended (medium) [LeetCode 1353] --- [EN](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) · [CN](https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/)

---

## 27. Pattern: Trie

- Implement Trie (Prefix Tree) (medium) [LeetCode 208] --- [EN](https://leetcode.com/problems/implement-trie-prefix-tree/) · [CN](https://leetcode.cn/problems/implement-trie-prefix-tree/)

- Add and Search Word - Data structure design (medium) [LeetCode 211] --- [EN](https://leetcode.com/problems/add-and-search-word-data-structure-design/) · [CN](https://leetcode.cn/problems/add-and-search-word-data-structure-design/)

- Replace Words (medium) [LeetCode 648] --- [EN](https://leetcode.com/problems/replace-words/) · [CN](https://leetcode.cn/problems/replace-words/)

- Design Add and Search Words Data Structure (medium) [LeetCode 211] --- [EN](https://leetcode.com/problems/add-and-search-word-data-structure-design/) · [CN](https://leetcode.cn/problems/add-and-search-word-data-structure-design/)

- Word Search II (hard) [LeetCode 212] --- [EN](https://leetcode.com/problems/word-search-ii/) · [CN](https://leetcode.cn/problems/word-search-ii/)

---

## 28. Pattern: Segment Tree / Binary Indexed Tree

- Range Sum Query - Mutable (medium) [LeetCode 307] --- [EN](https://leetcode.com/problems/range-sum-query-mutable/) · [CN](https://leetcode.cn/problems/range-sum-query-mutable/)

- Range Sum Query 2D - Mutable (hard) – custom extension; implement 2D BIT/segment tree as advanced exercise.

- Count of Smaller Numbers After Self (hard) [LeetCode 315] --- [EN](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) · [CN](https://leetcode.cn/problems/count-of-smaller-numbers-after-self/)

- Inversion Count of Array (hard) – custom exercise; can be solved via BIT/segment tree or merge sort.

---

## 29. Pattern: Misc & Test Your Knowledge

- LRU Cache (medium) [LeetCode 146] --- [EN](https://leetcode.com/problems/lru-cache/) · [CN](https://leetcode.cn/problems/lru-cache/)

- LFU Cache (hard) [LeetCode 460] --- [EN](https://leetcode.com/problems/lfu-cache/) · [CN](https://leetcode.cn/problems/lfu-cache/)

- Min Stack (easy) [LeetCode 155] --- [EN](https://leetcode.com/problems/min-stack/) · [CN](https://leetcode.cn/problems/min-stack/)

- Design HashMap / HashSet (easy/medium) [LeetCode 706] --- [EN](https://leetcode.com/problems/design-hashmap/) · [CN](https://leetcode.cn/problems/design-hashmap/)

- Implement Stack using Queues (easy) [LeetCode 225] --- [EN](https://leetcode.com/problems/implement-stack-using-queues/) · [CN](https://leetcode.cn/problems/implement-stack-using-queues/)

- Implement Queue using Stacks (easy) [LeetCode 232] --- [EN](https://leetcode.com/problems/implement-queue-using-stacks/) · [CN](https://leetcode.cn/problems/implement-queue-using-stacks/)

- Design Circular Queue (medium) [LeetCode 622] --- [EN](https://leetcode.com/problems/design-circular-queue/) · [CN](https://leetcode.cn/problems/design-circular-queue/)

- Random Pick Index / Reservoir Sampling style problem (medium) – e.g. "Random Pick Index" [LeetCode 398] --- [EN](https://leetcode.com/problems/random-pick-index/) · [CN](https://leetcode.cn/problems/random-pick-index/)

- Shuffle an Array (medium) [LeetCode 384] --- [EN](https://leetcode.com/problems/shuffle-an-array/) · [CN](https://leetcode.cn/problems/shuffle-an-array/)

- Design Twitter (medium/hard) [LeetCode 355] --- [EN](https://leetcode.com/problems/design-twitter/) · [CN](https://leetcode.cn/problems/design-twitter/)

---

You can now use this `README` as a complete pattern-based index over 30 patterns; feel free to refine or adjust individual mappings as you review problems.

