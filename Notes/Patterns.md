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
* Continue until both lists and the carry are exhausted.

**Time Complexity:**
O(max(m, n))

**Space Complexity:**
O(max(m, n))
## Sliding Window

**Problems:**

* Longest Substring Without Repeating Characters

**Key Idea:**
Maintain a window using two pointers. Expand the window while characters are unique. If a duplicate appears, shrink the window from the left until the duplicate is removed.

**Time Complexity:**
O(n)

**Space Complexity:**
O(min(n, m))

---

## Expand Around Center

**Problems:**

* Longest Palindromic Substring

**Key Idea:**
Treat every character (and every gap between two characters) as the center of a palindrome and expand outward while the characters match.

**Time Complexity:**
O(n²)

**Space Complexity:**
O(1)

---

## Simulation

**Problems:**

* Zigzag Conversion

**Key Idea:**
Simulate writing characters row by row while changing direction at the first and last rows.

**Time Complexity:**
O(n)

**Space Complexity:**
O(n)
