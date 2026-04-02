class PrefixTree:

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        
        cur[self.end_symbol] = True



    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return self.end_symbol in cur
        

    def startsWith(self, prefix: str) -> bool:
        words = []
        current = self.root

        
        for c in prefix:
            if c not in current:
                return False
            current = current[c]
        
        return True
        