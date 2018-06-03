# https://www.codewars.com/kata/52996b5c99fdcb5f20000004
from collections import defaultdict


def runoff(voters):
    all = {x for voter in voters for x in voter}
    votes = defaultdict(int)
    half = 0
    for voter in voters:
        if voter:
            votes[voter[0]] += 1
            half += 1
    half //= 2
    exclude = all - set(votes.keys())
    votes = sorted(votes.items(), key=lambda x: x[1])
    
    if not votes:
        return None
        
    if votes[-1][1] > half:
        return votes[-1][0]

    vote, min = votes[0]
    exclude.add(vote)
    for vote, count in votes[1:]:
        if count == min:
            exclude.add(vote)
    if len(exclude) == len(all):
        return None

    voters = [[x for x in voter if x not in exclude] for voter in voters]
    
    return runoff(voters)
    