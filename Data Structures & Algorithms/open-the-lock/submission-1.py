class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends or '0000' in deadends:
            return -1
        
        def turnLock(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        q = deque([('0000', 0)]) # current pattern, turns used
        visited = {'0000'}
        while q:
            currLock, turns = q.popleft()
            if currLock == target:
                return turns
            
            for child in turnLock(currLock):
                if child not in visited and child not in deadends:
                    visited.add(child)
                    q.append((child, turns + 1))

        return -1