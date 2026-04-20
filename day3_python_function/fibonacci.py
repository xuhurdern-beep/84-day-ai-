def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [1]
    elif n>=2:
        fib_list=[1,1]
        for i in range(2,n):
            next_fib=fib_list[i-1]+fib_list[i-2]
            fib_list.append(next_fib)
        return fib_list

if __name__ == "__main__":
    n = 10
    print(f"前 {n} 个斐波那契数列：{fibonacci(n)}")
    