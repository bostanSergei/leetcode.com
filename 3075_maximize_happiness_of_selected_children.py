def maximumHappinessSum(happiness: list, k: int) -> int:
    happiness.sort()
    sum_happy, count = 0, 0
    for i in range(-1, -len(happiness) - 1, -1):
        if (curr_happy := happiness[i] - count) > 0:
            sum_happy += curr_happy
        else:
            break

        count += 1
        if count == k:
            break

    return sum_happy


# happiness = [1, 1, 1, 1]
# k = 2
# print(maximumHappinessSum(happiness, k))
