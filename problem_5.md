# Implementation algorithm
Used Trie Search Algo, 
<br>
For finding suffixes:
1. Firstly, locate the TrieNode of  the character string that we want to search for suffixes.<br>
2. Traverse the TrieNode tree under the TrieNode recursively and whenever we hit the end of word, we add the result suffix in the list of suffixes. <br>
3. Finally, return the list of all possible suffixes.


# Run Time Complexity :
For lookup, run time complexity is O(n), where n is number of chars in word<br>
# Space Complexity:
word_length = Length of words<br>
unique_chars = unique number of characters at the same level<br>
The space complexity is of (O(word_length * unique_chars * no_of_words))