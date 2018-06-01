# https://www.codewars.com/kata/541af676b589989aed0009e7
def count_change(money, coins):
    def helper(sum=0, e_idx=0):
        if sum == money:
            return 1
        elif sum > money or e_idx >= len(coins):
            return 0
        else:
            same = helper(sum + coins[e_idx], e_idx)
            next = helper(sum + coins[e_idx + 1], e_idx + 1) if e_idx < len(coins) - 1 else 0
            skip = helper(sum, e_idx + 2)
            return same + next + skip

    return helper()