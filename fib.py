#Recursive fibonacci with memoization 
def fib(n):
    key = str(n)
    
    if key in memo:
        return memo[key]     

    if n <=2:
        return 1
    
    memo[str(n-1)] = fib(n-1)
    memo[str(n-2)] = fib(n-2)

    return (memo[str(n-1)]+memo[str(n-2)])



memo={}
print(fib(499))

