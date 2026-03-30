class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_id, status, timestamp = log.split(':')
            fn_id, timestamp = int(fn_id), int(timestamp)

            if status == 'start':
                if stack:
                    output[stack[-1]] += timestamp - prev_time

                stack.append(fn_id)
                prev_time = timestamp

            else: # status == "end"
                output[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1

        return output