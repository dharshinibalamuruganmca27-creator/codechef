# codechef
i solved some or different levels of probelms in code chef using my python language skills
Unique Elements (Duplicate Removal)

Description:
This program removes duplicate elements from a list while preserving the original order of appearance. It iterates through the input list and stores elements in a new list only if they have not appeared before. The result is a list containing each element exactly once in the order they first occurred.

Key Concept:
List traversal and duplicate checking.

Time Complexity:
O(n²) (because of item not in result check)

Space Complexity:
O(n)

2️⃣ Course Ends (Tuple Processing)

Description:
This function works with a tuple of course names and returns a tuple containing the first and last courses. If the tuple is empty, it returns an empty tuple. If it contains only one course, that course is repeated twice in the result. The original tuple remains unchanged because tuples are immutable.

Key Concept:
Tuple indexing and immutability.

Time Complexity:
O(1)

Space Complexity:
O(1)

3️⃣ Common Elements Between Two Lists

Description:
This program finds elements that are present in both lists. It ensures that each common element appears only once in the output list and maintains the order based on the first appearance in the first list.

Key Concept:
List comparison and duplicate prevention.

Time Complexity:
O(n × m)

Space Complexity:
O(n)

4️⃣ Isomorphic Strings

Description:
This program checks whether two strings follow the same character pattern. Each character in the first string must map to exactly one character in the second string and vice versa. Two dictionaries are used to ensure a one-to-one and reversible mapping.

Key Concept:
Dictionary mapping and pattern consistency.

Time Complexity:
O(n)

Space Complexity:
O(n)

5️⃣ Valid Anagram

Description:
This program determines whether two strings are anagrams. Two strings are considered anagrams if they contain the same characters with the same frequency, regardless of order. The program counts the frequency of characters and compares them.

Key Concept:
Character frequency counting.

Time Complexity:
O(n)

Space Complexity:
O(1) (since only 26 letters)

6️⃣ Longest Common Prefix

Description:
This program finds the longest prefix shared by all given strings. It starts with the first string as the assumed prefix and gradually shortens it until it matches the start of every other string.

Key Concept:
String comparison and prefix reduction.

Time Complexity:
O(N × M)
(N = number of strings, M = length of shortest string)

Space Complexity:
O(1)

7️⃣ Chef and Two Strings

Description:
This program calculates the minimum and maximum difference between two strings that may contain unknown characters represented by '?'. The minimum difference assumes unknown characters can match, while the maximum difference assumes they differ.

Key Concept:
Character comparison and conditional counting.

Time Complexity:
O(n)

Space Complexity:
O(1)

8️⃣ Card Removal

Description:
This program determines the minimum number of cards that must be removed so that all remaining cards have the same number. It finds the most frequent number and removes all other cards.

Key Concept:
Frequency counting.

Formula:
Moves = N − (maximum frequency)

Time Complexity:
O(n)

Space Complexity:
O(n)

9️⃣ Even-tual Reduction

Description:
This program checks whether a string can be completely removed by repeatedly deleting substrings where each character appears an even number of times. The whole string can be erased only if every character in the string appears an even number of times.

Key Concept:
Character frequency parity (even/odd).

Time Complexity:
O(n)

Space Complexity:
O(1)

🔟 Zero String

Description:
This program finds the minimum number of operations required to convert a binary string into a string of all zeros. Two operations are allowed: deleting a character or flipping the entire string. The program compares deleting all '1's versus flipping once and deleting all '0's to determine the minimum operations.

Formula:

min(number_of_1s, 1 + number_of_0s)

Time Complexity:
O(n)

Space Complexity:
O(1)

