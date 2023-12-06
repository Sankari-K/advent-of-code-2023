    lesser = 0
    for holding_time in range(0, time + 1):
        lesser += 1
        if holding_time * (time - holding_time) > distance:
            lesser -= 1
            break
