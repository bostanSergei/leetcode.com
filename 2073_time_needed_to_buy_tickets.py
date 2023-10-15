def timeRequiredToBuy(tickets: list, k: int) -> int:
    '''
    :param tickets: список целых чисел. Каждый элемент в списке - человек, который хочет купить билет в кассе.
    Значение - количество билетов, которое он хочет купить.
    :param k: индекс "человека" (по которому будем ориентироваться)
    :return: нужно вернуть количество секунд, которое требуется для того, чтобы указанный человек, купил
    необходимое ему количество билетов. Логика следующая: в самом начале к "кассе" подходит первый человек и
    за один подход он может купить только один билет. После этого он идет в конец очереди и снова ждёт своего часа)
    На "обслуживание" одного человека уходит ровно 1 секунда. Если человек купил требуемое количество билетов,
    он выходит из очереди. Если на примере: [3, 1, 2, 5] -> каждый человек из очереди покупает по одному билету
    и очередь снова доходит до первого человека -> [2, 0, 1, 4] -> на это ушло 4 секунды -> если бы нас
    интересовала судьба второго человека, то мы бы могли сказали, что требуется всего 2 секунды на решение задачи.
    На втором круге список принял бы вид [1, _, 0, 3] -> второй человек "ушел" из очереди. При этом если бы нас
    интересовала судьба третьего человека, то мы бы вернули результат 6 секунд (первый круг 4 секунды и второй
    круг 2 секунды (второй из очереди ушел)). И так далее.
    lvl - easy. В задаче важно подумать про граничные случаи, именно поэтому в моем решении присутствует переменная
    diff - которая "гарантирует" правильный ответ в зависимости от входных данных. Это, пожалуй самое сложное,
    над чем пришлось подумать) В остальном - классика.
    '''
    count = 0
    while tickets[k] > 0:
        count += sum([1 for i in tickets if i > 0])
        tickets = [i - 1 for i in tickets]

    diff = sum([1 for i in range(len(tickets)) if tickets[i] >= 0 and i > k])
    return count - diff


# tickets = [15, 66, 3, 47, 71, 27, 54, 43, 97, 34, 94, 33, 54, 26, 15, 52, 20, 71, 88, 42, 50, 6, 66, 88, 36, 99, 27, 82, 7, 72]
# k = 18
# print(timeRequiredToBuy(tickets, k))
