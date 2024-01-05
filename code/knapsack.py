#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def knapsack_with_reps(W, weights, values):
    n = len(weights)
    cell = [0] * (W + 1)

    for w in range(1, W + 1):
        for i in range(n):
            if weights[i] <= w:
                cell[w] = max(cell[w], cell[w - weights[i]] + values[i])

    return cell[W]

def knapsack_without_reps(W, weights, values):
    n = len(weights)
    cell = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                cell[i][w] = max(cell[i - 1][w], cell[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                cell[i][w] = cell[i - 1][w]

    w, i = W, n
    selected_items = [0] * n
    while i > 0 and w > 0:
        if cell[i][w] != cell[i - 1][w]:
            selected_items[i - 1] = 1
            w -= weights[i - 1]
        i -= 1

    return cell[n][W], selected_items

def knapsack_bu(W, weights, values):
    without_reps_result = knapsack_without_reps(W, weights, values)
    with_reps_result = knapsack_with_reps(W, weights, values)

    return with_reps_result, without_reps_result

if __name__ == "__main__":
    W = 10
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]

    # Knapsack with repetitions
    result_with_reps = knapsack_with_reps(W, weights, values)
    print("Результат рюкзака с повторами:", result_with_reps)

    # Knapsack without repetitions
    result_without_reps, selected_items = knapsack_without_reps(W, weights, values)
    print("Результат рюкзака без повторов:", result_without_reps)
    print("Выбранные предметы:", selected_items)

    # Combined result
    combined_result = knapsack_bu(W, weights, values)
    print("Общий результат (с повторами, без повторов):", combined_result)
