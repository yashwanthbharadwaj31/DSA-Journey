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
Sort the array first, fix one element, then use two pointers to find the remaining two values while skipping duplicates to avoid repeated triplets.
