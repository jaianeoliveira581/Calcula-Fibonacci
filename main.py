def calcula_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcula_fibonacci(n - 1) + calcula_fibonacci(n - 2)
    
    #programa principal
n = int(input('informe o numero de sequencias fibonacci:'))

for x in range(n):
    print(calcula_fibonacci(n))