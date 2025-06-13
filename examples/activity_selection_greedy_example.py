"""
Activity Selection Problem – Greedy Algorithm Example
"""

def select_activities(starts, finishes):
    n = len(starts)
    selected = [0]           # always pick the first activity
    last_finish = finishes[0]
    for i in range(1, n):
        if starts[i] >= last_finish:
            selected.append(i)
            last_finish = finishes[i]
    return selected

if __name__ == "__main__":
    start_times  = [1, 3, 0, 5, 8, 5]
    finish_times = [2, 4, 6, 7, 9, 9]
    chosen = select_activities(start_times, finish_times)
    print("Selected activity indices:", chosen)
