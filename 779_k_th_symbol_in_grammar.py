def kthGrammar(n: int, k: int) -> int:
    if n == 1:
        return 0
    if k % 2 == 0:
        return 1 if kthGrammar(n - 1, k // 2) == 0 else 0
    else:
        return 0 if kthGrammar(n - 1, (k + 1) // 2) == 0 else 1


n = 5
k = 3
print(kthGrammar(n, k))
