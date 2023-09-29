# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def hasCycle(head):
    '''
    :param head: дана ссылка на "вершину" односвязный список
    :return: вернуть True если список цикличен или False, если нет. Под цикличностью понимается наличие у "крайнего"
    элемента списка ссылки на какой-либо другой элемент связного списка. То есть в условном списке [1, 2, 3, 4]
    последний элемент может никуда не ссылаться self.next будет равен None или ссылаться на любой другой элемент
    изначального списка. Например ссылка с четвертого может идти на второй.
    Задачи на односвязные списки, дереья и подобные структуры для меня пока сложно, но эту задачу решил руководствуясь
    друмя указателями. Первый - медленный указатель (за иттерацию проходит на следующий элемент). Второй - быстрый.
    За одну иттерацию перемещается на два элемента. Если представить себе трассу вокруг стадиона, то второй элемент
    в один прекрастный момент догонит первый на втором круге. На этой логике и реализовано решение.
    '''

    slow, fast = head, head

    while fast:
        fast = fast.next
        if fast is None:
            return False
        fast = fast.next
        if fast is None:
            return False
        slow = slow.next
        if fast.val == slow.val and fast.next == slow.next:
            return True
    return False