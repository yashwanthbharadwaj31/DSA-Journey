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