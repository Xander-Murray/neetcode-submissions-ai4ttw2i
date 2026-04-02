class WordDictionary:

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        
        cur[self.end_symbol] = True



    def search(self, word: str) -> bool:
        def dfs(i, node):
            cur = node
            for j in range(i, len(word)):
                c = word[j]

                if c == ".":
                    for ch, nxt in cur.items():
                        if ch == self.end_symbol:
                            continue
                        if dfs(j + 1, nxt):
                            return True
                    return False

                if c not in cur:
                    return False
                cur = cur[c]

            return self.end_symbol in cur  # end of word reached

        return dfs(0, self.root)
