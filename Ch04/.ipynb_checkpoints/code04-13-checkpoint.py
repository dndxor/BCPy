person = 3                # 사람 수
order = 2                 # 피자 주문수량
piece = 8                   # 피자 당 조각 수
result = (order * piece) // person  # 한 사람 당 먹을 수 있는 조각 수
remain = (order * piece) % person  # 남는 조각 수

print("%d 조각씩 먹을 수 있고, %d 조각이 남습니다." % (result, remain))

