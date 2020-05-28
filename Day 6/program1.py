def delete(A, n):

    B = A[::-1]
    a = [[0 for x in range(n + 1)] for y in range((n + 1))]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                a[i][j] = a[i - 1][j - 1] + 1

            else:
                a[i][j] = max(a[i - 1][j], a[i][j - 1])

    return n - a[n][n]

s = str(input("Enter a string: "))
n = len(s)
print("Deletions required : ", delete(s, n))
