# DSA Patterns

## Hash Map

**Problems:**

* Two Sum

**Key Idea:**
Store previously seen elements to achieve O(1) average lookup.

---

## Number Manipulation

**Problems:**

* Palindrome Number

**Key Idea:**
Compare digits by reversing or checking symmetry.

---

## String Processing

**Problems:**

* Roman to Integer

**Key Idea:**
Map Roman symbols to integer values and handle subtraction cases.

---

## String Comparison

**Problems:**

* Longest Common Prefix

**Key Idea:**
Compare characters across all strings until a mismatch occurs.

---

## Linked List

### Pattern: Dummy Node + Carry

**Problems:**

* Add Two Numbers

**Key Concepts Learned:**

* Traverse two linked lists simultaneously.
* Handle carry while adding digits.
* Create a new linked list node by node.
* Use a dummy node to simplify insertion.

---

## Sliding Window

**Problems:**

* Longest Substring Without Repeating Characters

**Key Idea:**
Maintain a moving window using two pointers while tracking unique characters with a set.

---

## Expand Around Center

**Problems:**

* Longest Palindromic Substring

**Key Idea:**
Treat every character and every gap as the center of a palindrome and expand outward.

---

## Simulation

**Problems:**

* Zigzag Conversion

**Key Idea:**
Simulate writing characters row by row while changing direction at the first and last rows.

---

## Stack

**Problems:**

* Valid Parentheses

**Key Idea:**
Use a stack to keep track of opening brackets and match them with closing brackets in LIFO order.

---

## Frequency Count

**Problems:**

* Valid Anagram

**Key Idea:**
Count the frequency of every character using a hash map and compare both strings efficiently.

---

## Hash Map + Sorting

**Problems:**

* Group Anagrams

**Key Idea:**
Sort every string to create a common key and group words with identical sorted representations.

---

## Two Pointers

**Problems:**

* Valid Palindrome

**Key Idea:**
Use one pointer from the beginning and another from the end, moving toward the center while comparing characters or values.

---

## Two Pointers + Greedy

**Problems:**

* Container With Most Water

**Key Idea:**
Calculate the area formed by two pointers and always move the pointer with the smaller height, since moving the taller one cannot increase the maximum possible area.

---

## Sorting + Two Pointers

**Problems:**

* 3Sum

**Key Idea:**
Sort the array first, fix one element, then use two pointers to find the remaining two values while skipping duplicates.

---

## Binary Search

**Problems:**

* Binary Search

**Key Idea:**
Repeatedly divide the sorted search space into halves until the target is found or the search space becomes empty.

---

## Modified Binary Search

**Problems:**

* Search in Rotated Sorted Array

**Key Idea:**
Identify which half of the rotated array is sorted and determine whether the target lies in that half before eliminating the other half.

---

---

## Binary Search on Boundaries

**Problems:**

* Find First and Last Position of Element in Sorted Array

**Key Idea:**
Run Binary Search twice—once to find the first occurrence by continuing the search to the left, and once to find the last occurrence by continuing the search to the right.

---

## Binary Search on Matrix

**Problems:**

* Search a 2D Matrix

**Key Idea:**
Treat the entire matrix as a single sorted array. Convert the middle index into row and column indices using division and modulus to perform Binary Search efficiently.

---

---

## Modified Binary Search

**Problems:**

* Find Minimum in Rotated Sorted Array

**Key Idea:**
Compare the middle element with the rightmost element to determine which half contains the minimum value. Eliminate the sorted half and continue searching in the unsorted half.

---

## Binary Search on Answer

**Problems:**

* Find Peak Element

**Key Idea:**
Instead of searching for an exact value, compare adjacent elements to determine which direction leads toward a peak. Eliminate half of the search space in every iteration.

---

## Trees

### DFS (Depth First Search)

**Problems:**
- Binary Tree Inorder Traversal
- Maximum Depth of Binary Tree

**Key Idea:**
DFS explores one branch of the tree completely before moving to another branch. In binary trees, recursion is the most common way to implement DFS.

**Recognition:**
Question contains:
- Traversal
- Height
- Depth

Think:
- DFS
- Recursion

**Time Complexity:**
O(n)

**Space Complexity:**
O(h)

---

### Inorder Traversal

**Problems:**
- Binary Tree Inorder Traversal

**Traversal Order:**
Left → Root → Right

**Key Idea:**
Visit the left subtree, then the current node, and finally the right subtree.

---

### Maximum Depth of Binary Tree

**Problems:**
- Maximum Depth of Binary Tree

**Key Idea:**
Recursively calculate the depth of the left and right subtrees. The answer is the larger depth plus one for the current node.

---

## Comparing Trees

**Problems:**
- Same Tree
- Symmetric Tree

**Pattern:**
DFS (Recursion)

**Recognition:**
Question contains:
- Same Tree
- Equal Tree
- Compare Trees
- Symmetric Tree
- Mirror Tree

Think:
- DFS
- Recursion

---

## Same Tree

**Key Idea:**
Compare the corresponding nodes of both trees.

Conditions:
- Both nodes are null → Same
- One node is null → Different
- Values are different → Different
- Compare left subtrees.
- Compare right subtrees.

---

## Symmetric Tree

**Key Idea:**
Check whether the left subtree is the mirror image of the right subtree.

Mirror Comparison:

Left Tree            Right Tree

Left   ↔ Right

Right  ↔ Left

---

## Tree Comparison Pattern

Whenever the question asks:

- Same Tree
- Mirror Tree
- Symmetric Tree

Think:

DFS

↓

Recursion

↓

Compare corresponding nodes recursively

---

# Trees - Diameter of Binary Tree

Problem:
- #543 Diameter of Binary Tree

Pattern:
DFS + Postorder Traversal

Recognition:

Question asks:
- Longest path
- Diameter
- Maximum distance

Think:

DFS

↓

Postorder Traversal

↓

Calculate left depth

↓

Calculate right depth

↓

Update answer

Key Idea:

Diameter passing through a node

=

Left Depth + Right Depth

---

# Trees - Balanced Binary Tree

Problem:
- #110 Balanced Binary Tree

Pattern:
DFS + Bottom-Up Recursion

Recognition:

Question asks:

- Balanced Tree
- Height Difference
- Height Balanced

Think:

DFS

↓

Recursion

↓

Return Height

↓

Return -1 if unbalanced

Key Idea:

If any subtree becomes unbalanced,
immediately return -1.

Otherwise,

return

1 + max(leftHeight, rightHeight)

This avoids recalculating heights.

---

# Trees - Binary Tree Preorder Traversal

Problem:
- #144 Binary Tree Preorder Traversal

Pattern:
DFS (Preorder Traversal)

Recognition:

Question asks:
- Preorder Traversal
- Visit every node

Think:

DFS

↓

Root

↓

Left

↓

Right

Key Idea:

Visit the current node first,
then recursively traverse the left subtree,
followed by the right subtree.

---

# Trees - Validate Binary Search Tree

Problem:
- #98 Validate Binary Search Tree

Pattern:
DFS + Bounds

Recognition:

Question asks:

- Binary Search Tree
- Validate BST
- Is Valid BST

Think:

DFS

↓

Lower Bound

↓

Upper Bound

↓

Validate every node

Key Idea:

Each node must satisfy:

low < node.val < high

The valid range is updated recursively
while traversing the tree.

Never compare only with the parent.
Every node must satisfy the constraints
imposed by all its ancestors.

---

## Trees - Binary Tree Right Side View

Problem:
- #199 Binary Tree Right Side View

Pattern:
DFS (Right First)

Recognition:

Question contains:
- Right Side View
- Visible Nodes
- Rightmost Node
- Level View

Think:

DFS

↓

Visit Right Child First

↓

Store First Node of Each Level

Key Idea:

Traverse the right subtree before the left subtree.

The first node visited at every level is visible from the right side.

---

## Trees - Count Complete Tree Nodes

Problem:
- #222 Count Complete Tree Nodes

Pattern:
DFS (Recursion)

Recognition:

Question contains:
- Count Nodes
- Complete Binary Tree
- Number of Nodes

Think:

DFS

↓

Count Left Subtree

↓

Count Right Subtree

↓

Return Total Count

Key Idea:

Every node contributes one count.

Answer =

1 + Left Count + Right Count

---

## Trees - Binary Tree Postorder Traversal

Problem:
- #145 Binary Tree Postorder Traversal

Pattern:
DFS (Postorder Traversal)

Recognition:

Question contains:
- Postorder Traversal
- Visit every node

Think:

DFS

↓

Left

↓

Right

↓

Root

Key Idea:

Visit both subtrees completely before processing the current node.

Traversal Order:

Left → Right → Root

---

## Trees - Construct Binary Tree from Preorder and Inorder Traversal

Problem:
- #105 Construct Binary Tree from Preorder and Inorder Traversal

Pattern:
DFS + Divide & Conquer + Hash Map

Recognition:

Question contains:
- Construct Tree
- Build Tree
- Preorder
- Inorder

Think:

Preorder

↓

Root comes first

↓

Find Root in Inorder

↓

Split Left & Right Subtrees

↓

Recursively Build Tree

Key Idea:

Preorder tells you the root.

Inorder tells you where to split the tree.

A Hash Map allows O(1) lookup of each node's index.

---

## Arrays - Best Time to Buy and Sell Stock

Problem:
- #121 Best Time to Buy and Sell Stock

Pattern:
Greedy

Recognition:

Question contains:
- Buy once
- Sell once
- Maximum Profit

Think:

Traverse Once

↓

Keep Minimum Price

↓

Calculate Current Profit

↓

Update Maximum Profit

Key Idea:

Keep track of the cheapest buying price seen so far.

At every day, calculate the profit if sold today.

---

## Arrays - Contains Duplicate

Problem:
- #217 Contains Duplicate

Pattern:
Hash Set

Recognition:

Question contains:
- Duplicate
- Repeated Element
- Unique Values

Think:

Traverse Array

↓

Hash Set

↓

Already Exists?

↓

Return True

Key Idea:

Hash Set provides O(1) average lookup.

If an element is already present, a duplicate exists.

---

## Arrays - Product of Array Except Self

Problem:
- #238 Product of Array Except Self

Pattern:
Prefix Product + Suffix Product

Recognition:

Question contains:
- Product Except Self
- Product of Remaining Elements
- No Division

Think:

Prefix Product

↓

Suffix Product

↓

Combine Both

Key Idea:

Compute the product of all elements to the left of each index.

Then multiply it with the product of all elements to the right.

This avoids division and solves the problem in linear time.

---

## Arrays - Maximum Subarray

Problem:
- #53 Maximum Subarray

Pattern:
Kadane's Algorithm

Recognition:

Question contains:
- Maximum Sum
- Largest Sum
- Contiguous Subarray

Think:

Current Sum

↓

Maximum Sum

↓

Restart Current Sum if Needed

Key Idea:

At every element,

choose the better option:

- Start a new subarray.
- Continue the previous subarray.

Whichever produces the larger sum becomes the new current sum.

---

## Arrays - Maximum Product Subarray

Problem:
- #152 Maximum Product Subarray

Pattern:
Dynamic Tracking

Recognition:

Question contains:
- Maximum Product
- Contiguous Subarray
- Negative Numbers

Think:

Track Maximum Product

↓

Track Minimum Product

↓

Swap on Negative Number

↓

Update Answer

Key Idea:

A negative number can turn the smallest product into the largest product.

Maintain both the current maximum and current minimum product while traversing the array.

---

## Arrays - Merge Intervals

Problem:
- #56 Merge Intervals

Pattern:
Sorting + Interval Merging

Recognition:

Question contains:
- Merge Intervals
- Overlapping Intervals
- Meeting Schedule
- Range Merging

Think:

Sort Intervals

↓

Compare Current Interval

↓

Overlap?

↓

Merge

↓

Otherwise Add New Interval

Key Idea:

Sorting places overlapping intervals together.

If the current interval overlaps with the previous merged interval, extend its ending point.

Otherwise, start a new interval.

## Arrays - Insert Interval

Problem:
- #57 Insert Interval

Pattern:
Interval Merging

Recognition:

Question contains:
- Intervals
- Overlapping ranges
- Insert a new interval
- Merge overlapping intervals

Think:

Process intervals in order

↓

Intervals completely before new interval?

↓

Add them

↓

Overlap with new interval?

↓

Merge

↓

Add remaining intervals

Key Idea:

Because the intervals are already sorted by starting time, process them from left to right.

There are three cases:

1. Current interval ends before the new interval starts.
2. Current interval overlaps with the new interval.
3. Current interval starts after the new interval ends.

During overlap, update the new interval using:

- minimum starting point
- maximum ending point

Then add the merged interval to the result.


## Arrays - Rotate Image

Problem:
- #48 Rotate Image

Pattern:
Matrix Transformation

Recognition:

Question contains:
- Rotate matrix
- Rotate image
- 90 degree clockwise
- Modify matrix in-place

Think:

Transpose Matrix

↓

Reverse Every Row

↓

90 Degree Clockwise Rotation

Key Idea:

A matrix can be rotated 90 degrees clockwise in two steps:

1. Transpose the matrix.
2. Reverse every row.

Example:

1 2 3
4 5 6
7 8 9

↓

Transpose

1 4 7
2 5 8
3 6 9

↓

Reverse each row

7 4 1
8 5 2
9 6 3

The rotation is performed in-place without creating another matrix.


## Pattern Recognition Added

Interval Problems:

Sort or process intervals

↓

Check overlap

↓

Merge when necessary


Matrix Rotation:

Transpose

↓

Reverse Rows

## Arrays - Merge Sorted Array

**Problem:**
- #88 Merge Sorted Array

**Pattern:**

Two Pointers — Start from the End

**Recognition:**

Look for:
- Two sorted arrays
- Merging arrays in sorted order
- Modifying an array in-place
- Extra capacity at the end of the first array

**Think:**

Initialize pointers at the ends of the valid portions of both arrays.

↓

Compare the current elements.

↓

Place the larger element at the last available position.

↓

Move the corresponding pointer backward.

↓

Continue until all elements from the second array are placed.

**Key Idea:**

Fill the first array from right to left to avoid overwriting elements that have not been processed.

The second array's pointer determines when the merge is complete.

**Complexity:**
- Time: O(m + n)
- Auxiliary Space: O(1)

---

## Arrays - Sort Colors

**Problem:**
- #75 Sort Colors

**Pattern:**

Three Pointers — Dutch National Flag

**Recognition:**

Look for:
- An array containing only 0, 1, and 2
- Sorting without using a built-in sorting function
- In-place sorting in one pass

**Think:**

Maintain three pointers:

- `low`: boundary for 0s
- `mid`: current element being examined
- `high`: boundary for 2s

↓

If `nums[mid] == 0`, swap it with `nums[low]` and increment both `low` and `mid`.

↓

If `nums[mid] == 1`, increment `mid`.

↓

If `nums[mid] == 2`, swap it with `nums[high]` and decrement `high`.

↓

Continue while `mid <= high`.

**Key Idea:**

Maintain three regions:

- Before `low`: all 0s
- Between `low` and `mid`: all 1s
- After `high`: all 2s

When swapping with `high`, do not increment `mid` immediately because the incoming element still needs to be examined.

Complexity:
- Time: O(n)
- Auxiliary Space: O(1)

---

## Pattern Recognition Added

Merging Sorted Arrays:

Two sorted arrays

↓

Compare from the end

↓

Place the larger element

↓

Move pointers backward

Sorting Three Distinct Values:

Three pointers

↓

Classify the current element

↓

Swap into the correct region

↓

Maintain the invariant until sorted