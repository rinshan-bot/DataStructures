class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")
    def insert(self,word):
        node = self.root
        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        node.counter += 1
    def dfs(self,node,prefix):
        if node.is_end:
            self.output.append((prefix+node.char,node.counter))

        for child in node.children.values():
            self.dfs(child,prefix+node.char)
            
    def query(self,x):
        self.output = []
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
                print(node.children)
            else:
                return []
        self.dfs(node,x[:-1])
        return sorted(self.output,key=lambda x:x[1],reverse=True)
    def a(self):
        return self.root.children
t = Trie()
t.insert("was")
t.insert("word")
t.insert("war")
t.insert("what")
t.insert("where")
t.insert("hellow")
t.query("wh")
