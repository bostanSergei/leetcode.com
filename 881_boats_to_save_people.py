def numRescueBoats(people: list, limit: int) -> int:
    people.sort()
    left, right = 0, len(people) - 1
    count = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1

        count += 1

    return count


# people = [3,5,3,4]
# limit = 5
# print(numRescueBoats(people, limit))
