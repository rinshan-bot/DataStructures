Inserting Words into the Trie
In order to insert a new word into the trie, we need to first check whether any prefix of the word is already in the trie. Therefore, we will start traverse the trie from the root node, and follow the algorithm below:

<ul>
<li>Set the current node to be the root node</li>
<li>Set the current character as the first character of the input word</li>
<li>Check if the current character is a child of the current node</li>
<li>If yes, set the current node to be this child node, set the current character to the next character in the input word, and perform this step again</li>
<li>If no, it means from this character onwards, we will need to create new nodes and insert them into the trie</li>
Below is an illustration of what will happen when we want to add the word won into the trie above.</li>
