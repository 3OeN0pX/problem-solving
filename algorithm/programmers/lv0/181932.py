def solution(code):
    ret = []
    mode = 0

    for idx, ch in enumerate(code):
        if ch == "1":
            if mode == 1:
                mode = 0
            else:
                mode = 1
        else:
            if mode == 1 and (idx % 2 == 1):
                ret.append(ch)
            if mode == 0 and (idx % 2 == 0):
                ret.append(ch)

    if not ret:
        answer = "EMPTY"
    else:
        answer = "".join(ret)


    return answer
