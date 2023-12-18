import heapq


def maxKelements(nums: list, k: int) -> int:
    '''
    :param nums:
    :param k:
    :return:
    '''
    score, pq = 0, []
    for num in nums:
        heapq.heappush(pq, (-num, num))

    while k > 0:
        maxElement = heapq.heappop(pq)[1]
        score += maxElement
        upd_value = maxElement // 3 + (maxElement % 3 != 0)
        heapq.heappush(pq, (-upd_value, upd_value))
        k -= 1

    return score


# nums = [10, 10, 10, 10, 10]
# k = 5
# print(maxKelements(nums, k))
