p_id = ["p1", "p2", "p3", "p4", "p5", "p6"]
at = [0, 1, 2, 3, 4, 4]
bt = [7, 4, 15, 11, 20, 9]

n = len(p_id)


fcfs_id = p_id.copy()
fcfs_at = at.copy()
fcfs_bt = bt.copy()


for i in range(n - 1):
    for j in range(n - 1 - i):

        if fcfs_at[j] > fcfs_at[j + 1]:

            fcfs_at[j], fcfs_at[j + 1] = fcfs_at[j + 1], fcfs_at[j]
            fcfs_bt[j], fcfs_bt[j + 1] = fcfs_bt[j + 1], fcfs_bt[j]
            fcfs_id[j], fcfs_id[j + 1] = fcfs_id[j + 1], fcfs_id[j]


fcfs_ct = []
fcfs_tat = []
fcfs_wt = []

time = 0
sum_tat = 0
sum_wt = 0

for i in range(n):

    if time < fcfs_at[i]:
        time = fcfs_at[i]

    time = time + fcfs_bt[i]

    fcfs_ct.append(time)
    fcfs_tat.append(fcfs_ct[i] - fcfs_at[i])
    fcfs_wt.append(fcfs_tat[i] - fcfs_bt[i])

    sum_tat = sum_tat + fcfs_tat[i]
    sum_wt = sum_wt + fcfs_wt[i]


fcfs_avg_tat = sum_tat / n
fcfs_avg_wt = sum_wt / n



sjf_ct = [0] * n
sjf_tat = [0] * n
sjf_wt = [0] * n

done = [0] * n

time = 0
completed = 0

sjf_seq = []


while completed < n:

    smallest = -1

    for i in range(n):

        if at[i] <= time and done[i] == 0:

            if smallest == -1 or bt[i] < bt[smallest]:
                smallest = i

    if smallest != -1:

        sjf_seq.append(p_id[smallest])

        time = time + bt[smallest]

        sjf_ct[smallest] = time
        sjf_tat[smallest] = sjf_ct[smallest] - at[smallest]
        sjf_wt[smallest] = sjf_tat[smallest] - bt[smallest]

        done[smallest] = 1
        completed = completed + 1

    else:
        time = time + 1


sjf_avg_tat = sum(sjf_tat) / n
sjf_avg_wt = sum(sjf_wt) / n



quantum = 5

rr_id = p_id.copy()
rr_at = at.copy()
rr_bt = bt.copy()


for i in range(n - 1):
    for j in range(n - 1 - i):

        if rr_at[j] > rr_at[j + 1]:

            rr_at[j], rr_at[j + 1] = rr_at[j + 1], rr_at[j]
            rr_bt[j], rr_bt[j + 1] = rr_bt[j + 1], rr_bt[j]
            rr_id[j], rr_id[j + 1] = rr_id[j + 1], rr_id[j]


remaining = rr_bt.copy()

rr_ct = [0] * n
rr_tat = [0] * n
rr_wt = [0] * n

queue = []
added = [0] * n

time = 0
completed = 0

rr_seq = []


while completed < n:


    for i in range(n):

        if rr_at[i] <= time and added[i] == 0:

            queue.append(i)
            added[i] = 1


    if len(queue) == 0:

        time = time + 1

    else:

        current = queue.pop(0)

        rr_seq.append(rr_id[current])


        if remaining[current] > quantum:

            time = time + quantum
            remaining[current] = remaining[current] - quantum

        else:

            time = time + remaining[current]
            remaining[current] = 0
        for i in range(n):

            if rr_at[i] <= time and added[i] == 0:

                queue.append(i)
                added[i] = 1


        if remaining[current] > 0:

            queue.append(current)


        else:

            rr_ct[current] = time

            rr_tat[current] = rr_ct[current] - rr_at[current]

            rr_wt[current] = rr_tat[current] - rr_bt[current]

            completed = completed + 1


rr_avg_tat = sum(rr_tat) / n
rr_avg_wt = sum(rr_wt) / n



print("\nFCFS:")

print("Execution Sequence:", end=" ")

for i in range(n):
    print(fcfs_id[i], end=" ")

print("\n")
print(f"{'PID':<8}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")

for i in range(n):

    print(
        f"{fcfs_id[i]:<8}{fcfs_at[i]:<6}{fcfs_bt[i]:<6}"
        f"{fcfs_ct[i]:<6}{fcfs_tat[i]:<6}{fcfs_wt[i]:<6}"
    )

print("\nAverage TAT =", fcfs_avg_tat)
print("Average WT  =", fcfs_avg_wt)


print("\nSJF:")

print("Execution Sequence:", end=" ")

for process in sjf_seq:
    print(process, end=" ")

print("\n")
print(f"{'PID':<8}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")

for i in range(n):

    print(
        f"{p_id[i]:<8}{at[i]:<6}{bt[i]:<6}"
        f"{sjf_ct[i]:<6}{sjf_tat[i]:<6}{sjf_wt[i]:<6}"
    )

print("\nAverage TAT =", sjf_avg_tat)
print("Average WT  =", sjf_avg_wt)


print("\nROUND ROBIN:")

print("Time Quantum =", quantum)

print("Execution Sequence:", end=" ")

for process in rr_seq:
    print(process, end=" ")

print("\n")
print(f"{'PID':<8}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")

for i in range(n):

    print(
        f"{rr_id[i]:<8}{rr_at[i]:<6}{rr_bt[i]:<6}"
        f"{rr_ct[i]:<6}{rr_tat[i]:<6}{rr_wt[i]:<6}"
    )

print("\nAverage TAT =", rr_avg_tat)
print("Average WT  =", rr_avg_wt)


print("\nCOMPARISON:")

print(f"{'Algorithm':<15}{'Avg TAT':<12}{'Avg WT':<12}")

print(f"{'FCFS':<15}{fcfs_avg_tat:<12.1f}{fcfs_avg_wt:<12.1f}")
print(f"{'SJF':<15}{sjf_avg_tat:<12.1f}{sjf_avg_wt:<12.1f}")
print(f"{'Round Robin':<15}{rr_avg_tat:<12.1f}{rr_avg_wt:<12.1f}")
