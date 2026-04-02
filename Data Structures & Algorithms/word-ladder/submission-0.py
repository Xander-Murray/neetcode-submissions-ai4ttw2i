class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        
        def combo(word):
            combos = []
    
            # Loop through every index from 0 to length-1
            for i in range(len(word)):
                
                # 1. word[:i]   -> Everything BEFORE index i
                # 2. "*"        -> The wildcard
                # 3. word[i+1:] -> Everything AFTER index i
                pattern = word[:i] + "*" + word[i+1:]
                
                combos.append(pattern)
                
            return combos

        for w in wordList:
            cmbs = combo(w)
            for c in cmbs:
                graph[c].append(w)

        visit = set()
        q = deque()

        q.append((beginWord, 1))
        visit.add(beginWord)

        while q:
            wrd, level = q.popleft() # Unpack the tuple
            
            if wrd == endWord:
                return level
            
            wrdSplits = combo(wrd)
            
            # Iterate through the patterns of the current word
            for pattern in wrdSplits:
                
                # DIRECT ACCESS: Get the list of neighbors for this pattern
                # If pattern doesn't exist, it returns [] (because of defaultdict)
                neighbors = graph[pattern]
                
                for neighbor in neighbors:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        q.append((neighbor, level + 1)) # Increase level by 1
                        
        return 0


        



