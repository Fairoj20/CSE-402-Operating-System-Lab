p_id = ["p1", "p2", "p3", "p4", "p5"]
at = [4, 2, 1, 0, 3]
bt = [2, 2, 3, 6, 1]

n = len(p_id)

quantum = 2

remaining = bt.copy()

ct = [0]*n
tat = [0]*n
wt = [0]*n

time = 0
completed = 0

execution_seq = []

while completed < n:
    shortest = -1

    while completed < n:

        shortest = -1

        for i in range(n):

            if at[i] <= time and remaining[i] > 0:

                if shortest == -1 or remaining[i] < remaining[shortest]:
                    shortest = i

        if shortest == -1:

            time = time + 1

        else:

            execution_seq.append(p_id[shortest])

            if remaining[shortest] > quantum:

                time = time + quantum
                remaining[shortest] = remaining[shortest] - quantum

            else:

                time = time + remaining[shortest]
                remaining[shortest] = 0

            if remaining[shortest] == 0:
                ct[shortest] = time
                completed = completed + 1

sum_tat = 0
sum_wt = 0

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

    sum_tat = sum_tat + tat[i]
    sum_wt = sum_wt + wt[i]


avg_tat = sum_tat / n
avg_wt = sum_wt / n

print("\nPREEMPTIVE SJF:")

print("Time Quantum =", quantum)

print("Execution Sequence:", end=" ")

for process in execution_seq:
    print(process, end=" ")

print("\n")

print(f"{'PID':<8}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")

for i in range(n):

    print(
        f"{p_id[i]:<8}{at[i]:<6}{bt[i]:<6}"
        f"{ct[i]:<6}{tat[i]:<6}{wt[i]:<6}"
    )

print("\nAverage TAT =", avg_tat)
print("Average WT  =", avg_wt
