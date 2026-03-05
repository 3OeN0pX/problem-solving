def solution(emergency):
    # 1. 응급도가 높은 순서(내림차순)로 정렬된 리스트를 만든다.
    sorted_emergency = sorted(emergency, reverse=True)
    
    # 2. 각 응급도 점수가 몇 번째 순서인지 딕셔너리에 저장
    # 예시: {70: 1, 30: 2, 10: 3}
    rank_dic = {value: i + 1 for i, value in enumerate(sorted_emergency)}
    
    # 3. 원래 입력받은 emergency 리스트를 반복하며 딕셔너리에서 순위를 꺼내온다.
    answer = [rank_dic[x] for x in emergency]

    return answer