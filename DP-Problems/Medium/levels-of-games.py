def maxLevel(H, M):
    # Initialize dp table with -1 representing invalid state.
    dp = [[[-1, -1] for _ in range(3)] for _ in range(800)]
    
    # Start at level 0 with the given health H and money M
    dp[0][0] = [H, M]
    dp[0][1] = [H, M]
    dp[0][2] = [H, M]
    
    max_level = 0
    
    for level in range(800 - 1):
        for road in range(3):
            if dp[level][road][0] <= 0 or dp[level][road][1] <= 0:
                continue
            
            # Current health and money
            curr_health, curr_money = dp[level][road]
            
            # Transition to the next level using different roads
            if road != 0:
                # Road 1: Health -20, Money +5
                new_health, new_money = curr_health - 20, curr_money + 5
                if new_health > 0 and new_money > 0:
                    dp[level + 1][0] = max(dp[level + 1][0], [new_health, new_money])
                    
            if road != 1:
                # Road 2: Health -5, Money -10
                new_health, new_money = curr_health - 5, curr_money - 10
                if new_health > 0 and new_money > 0:
                    dp[level + 1][1] = max(dp[level + 1][1], [new_health, new_money])
                    
            if road != 2:
                # Road 3: Health +3, Money +2
                new_health, new_money = curr_health + 3, curr_money + 2
                if new_health > 0 and new_money > 0:
                    dp[level + 1][2] = max(dp[level + 1][2], [new_health, new_money])
                    
        # Update the maximum level that is valid
        if any(dp[level + 1][r][0] > 0 and dp[level + 1][r][1] > 0 for r in range(3)):
            max_level = level + 1
            
    return max_level
