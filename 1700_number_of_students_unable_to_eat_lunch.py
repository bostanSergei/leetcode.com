from collections import deque


def countStudents(students: list, sandwiches: list) -> int:
    '''
    :param students: список студентов (или 0 или 1) - это характеристика того, какие сэндвичи любит каждый студент
    :param sandwiches: список сэндвичей (0 или 1) - "стек" из которого достать сэндвич можно только сверху)
    :return: вернуть количество студентов, которые останутся голодными)
    Условие такое: студет подходит к сэндвичам и либо берет сэндвич сверху (если они друг другу "подходят"),
    либо уходит в конец очереди. И так до тех пор, пока цикл приводит хоть к какому-то результату (в виде накормленного
    студента). lvl - easy. Решаю задачи через очередь. Логика ровно такая, как описано в условии задачи)
    '''
    sandwichIndex, q = 0, deque(students)

    while True:
        startLen = len(q)
        count = 0
        while count < startLen:
            currStudent = q.popleft()
            if currStudent == sandwiches[sandwichIndex]:
                sandwichIndex += 1
            else:
                q.append(currStudent)
            count += 1
        if len(q) == startLen:
            break

    return len(q)


# students = [1, 1, 0, 0]
# sandwiches = [0, 1, 0, 1]
# students = [1, 1, 1, 0, 0, 1]
# sandwiches = [1, 0, 0, 0, 1, 1]
# print(countStudents(students, sandwiches))
