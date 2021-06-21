# Inserting Words into the Trie
In order to insert a new word into the trie, we need to first check whether any prefix of the word is already in the trie. Therefore, we will start traverse the trie from the root node, and follow the algorithm below:

<ul>
<li>Set the current node to be the root node</li>
<li>Set the current character as the first character of the input word</li>
<li>Check if the current character is a child of the current node</li>
<li>If yes, set the current node to be this child node, set the current character to the next character in the input word, and perform this step again</li>
<li>If no, it means from this character onwards, we will need to create new nodes and insert them into the trie</li>
</ul>
<ul>
  <li>t.insert("was")</li>
  <li>t.insert("word")</li>
  <li>t.insert("war")</li>
  <li>t.insert("what")</li>
  <li>t.insert("where")</li>
  <li>t.query("wh")</li>
</ul>
So the output will be looks like the image in the directory
# Searching
## Seach wh
<ul>
<li>Starting from the root node, we are able to find the node w and a</li>
<li>From the node a, we can go on to traverse the trie to retrieve all words starting with the prefix wa</li>
<li>When we arrive at the node s, we check whether it is the end of a word (yes), and the word was was output</li>
<li>Similarity, when we arrive at the node x, the word wax is output</li>
</ul>
