#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci(n, calculation_method=0):
    def fibonacci_td(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fibonacci_td(n - 1) + fibonacci_td(n - 2)
        return memo[n]

    def fibonacci_bu(n):
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def fibonacci_bu_improved(n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    if calculation_method == 0:
        return fibonacci_td(n)
    elif calculation_method == 1:
        return fibonacci_bu(n)
    elif calculation_method == 2:
        return fibonacci_bu_improved(n)
    else:
        raise ValueError("Invalid calculation method")

if __name__ == "__main__":
    N = 10

    for method in range(3):
        result = fibonacci(N, method)
        print(f"Fibonacci({N}) using method {method}: {result}")
