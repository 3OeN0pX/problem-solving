def solution(rank, attendance):
    selected = sorted((rank[i], i) for i in range(len(rank)) if attendance[i])[:3]
    a, b, c = [i for _, i in selected]
    return 10000 * a + 100 * b + c