def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {x: dice.count(x) for x in set(dice)}
    unique_dice = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    
    # 1. 네 주사위 숫자가 모두 같을 때 (set의 길이가 1)
    if len(counts) == 1:
        return 1111 * a
    
    # 2. 세 주사위 숫자가 같을 때 (counts의 가장 큰 값이 3)
    if len(counts) == 2:
        p, q = unique_dice
        if counts[p] == 3:
            return (10 * p + q) ** 2
        # 3. 주사위가 두 개씩 같을 때 (2개, 2개)
        else:
            return (p + q) * abs(p - q)
            
    # 4. 주사위 두 개만 같고 나머지는 각각 다를 때 (set의 길이가 3)
    if len(counts) == 3:
        # unique_dice는 개수 순으로 정렬되어 있으므로 첫 번째가 p, 나머지가 q, r
        p, q, r = unique_dice
        return q * r
    
    # 5. 네 주사위 숫자가 모두 다를 때 (set의 길이가 4)
    return min(dice)