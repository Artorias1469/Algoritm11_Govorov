#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_bottom_up(a):
    n = len(a)
    D = [1] * n

    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and D[i] < D[j] + 1:
                D[i] = D[j] + 1

    return max(D)


def using_prev(prev, m_index):
    result = []
    while m_index is not None:
        result.insert(0, m_index)
        m_index = prev[m_index]
    return result


def without_prev(d, ans, m_index):
    result = []
    while d[m_index] != 1:
        result.insert(0, ans[m_index])
        m_index -= 1
    result.insert(0, ans[m_index])
    return result


def list_bottom_up_2(a):
    n = len(a)
    D = [1] * n
    prev = [None] * n
    m_index = 0

    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and D[i] < D[j] + 1:
                D[i] = D[j] + 1
                prev[i] = j
                if D[i] > D[m_index]:
                    m_index = i

    result_using_prev = using_prev(prev, m_index)
    result_without_prev = without_prev(D, a, m_index)

    return D[m_index], result_using_prev, result_without_prev


if __name__ == '__main__':
    a = [10, 22, 9, 33, 21, 50, 41, 60, 80]

    length_bottom_up = list_bottom_up(a)
    print(f"Длина наибольшей возрастающей подпоследовательности (снизу вверх): {length_bottom_up}")

    length_bottom_up_2, lis_using_prev, lis_without_prev = list_bottom_up_2(a)
    print(f"Длина НВП (снизу вверх_2): {length_bottom_up_2}")
    print(f"НВП с помощью prev: {lis_using_prev}")
    print(f"НВП без prev: {lis_without_prev}")
