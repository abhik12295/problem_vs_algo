
# Implementation algorithm
Used Trie Search Algo, 
<br>
For finding suffixes:
1. Firstly, locate the TrieNode of  the character string that we want to search for suffixes.<br>
2. Traverse the TrieNode tree under the TrieNode recursively and whenever we hit the end of word, we add the result suffix in the list of suffixes. <br>
3. Finally, return the list of all possible suffixes.


# Run Time Complexity :
For lookup, insert, search, run time complexity is O(n), where n is number of chars in word<br>
# Space Complexity:
token_length = Length of words<br>
unique_tokens = unique number of tokens<br>
no_of_tokens = e.g. /home/about contains 2 tokens
The space complexity is of (O(token_length * unique_tokens * no_of_tokens))