def average(salary: list) -> float:
    min_salary, max_salary = 10 ** 6, 0
    salary_dict = {}
    for i in salary:
        if i not in salary_dict:
            salary_dict[i] = 0

        salary_dict[i] += 1

        if i > max_salary:
            max_salary = i

        if i < min_salary:
            min_salary = i

    count, sum_salary = 0, 0
    for key, val in salary_dict.items():
        if key not in [min_salary, max_salary]:
            count += val
            sum_salary += val * key

    return sum_salary / count
