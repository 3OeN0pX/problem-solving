class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # 1 부터 n 까지 스트림이 있음
        # 스트림에 숫자가 남아 있다면 스택에 PUSH
        # 스택이 비어 있지 않다면, 스택 맨 위의 숫자를 POP 할 수 있음
        # 어느 순간이라도 스택의 요소들이 target과 같아 진다면, 스트림에서 더 이상 숫자를 읽지 말고 스택 연산도 중단하길
        output = []
        target_idx = 0

        for i in range(1, n+1):
            if target_idx == len(target):
                break
            
            output.append("Push")

            if i == target[target_idx]:
                target_idx += 1
            else:
                output.append("Pop")

        return output