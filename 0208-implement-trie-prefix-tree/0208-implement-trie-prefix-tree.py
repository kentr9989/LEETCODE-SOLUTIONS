class TrieNode:
    def __init__(self):
        self.children = {}
        self.lastWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.lastWord = True
        # self.print_trie()
        # print(curr)
        
        
    def print_trie(self, node=None, prefix=""):
        if node is None:
            node = self.root  # Start from the root node
        if node.lastWord:
            print(f"{prefix} (endOfWord)")
        for c, child in node.children.items():
            self.print_trie(child, prefix + c)  # Recursive call for each child    

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        if curr.lastWord == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)