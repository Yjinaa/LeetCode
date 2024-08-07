from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        queue = deque([(0,0)])
        visited = set()

        while queue:
            cur_amt, cur_coins = queue.popleft()
            visited.add(cur_amt)
            for coin in coins:
                new_amt = cur_amt + coin
                new_coins = cur_coins + 1
                if new_amt == amount:
                    return new_coins
                if new_amt < amount and new_amt not in visited:
                    queue.append((new_amt, new_coins))
                    visited.add(new_amt)
        return -1

            

