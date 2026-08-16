p_id = ["p1", "p2", "p3", "p4", "p5"]
at = [3, 2, 5, 1, 6]
bt = [3, 5, 4, 3, 2]

fcfs_id = p_id.copy()
fcfs_at = at.copy()
fcfs_bt = bt.copy()

for i in range(len(fcfs_at)-1):
    for j in range(len(fcfs_at)-1-i):
        if fcfs_at[j] > fcfs_at[j+1]:
            fcfs_at[j], fcfs_at[j+1] = fcfs_at[j+1], fcfs_at[j]
            fcfs_bt[j], fcfs_bt[j+1] = fcfs_bt[j+1], fcfs_bt[j]
            fcfs_id[j], fcfs_id[j+1] = fcfs_id[j+1], fcfs_id[j]

fcfs_ct = []
fcfs_tat = []
fcfs_wt = []

current_time = 0
sum_tat = 0
sum_wt = 0

for i in range(len(fcfs_id)):

    if current_time < fcfs_at[i]:
        current_time = fcfs_at[i]

    current_time = current_time + fcfs_bt[i]

    fcfs_ct.append(current_time)
    fcfs_tat.append(fcfs_ct[i] - fcfs_at[i])
    fcfs_wt.append(fcfs_tat[i] - fcfs_bt[i])

    sum_tat = sum_tat + fcfs_tat[i]
    sum_wt = sum_wt + fcfs_wt[i]

fcfs_avg_tat = sum_tat / len(fcfs_id)
fcfs_avg_wt = sum_wt / len(fcfs_id)

sjf_id = p_id.copy()
sjf_at = at.copy()
sjf_bt = bt.copy()

sjf_ct = [0, 0, 0, 0, 0]
sjf_tat = [0, 0, 0, 0, 0]
sjf_wt = [0, 0, 0, 0, 0]
done = [0, 0, 0, 0, 0]
time = 0
completed = 0
sjf_seq = []

while completed < len(sjf_id):

    smallest = -1

    for i in range(len(sjf_id)):
        if sjf_at[i] <= time and done[i] == 0:

            if smallest == -1 or sjf_bt[i] < sjf_bt[smallest]:
                smallest = i

    if smallest != -1:

        sjf_seq.append(sjf_id[smallest])
        time = time + sjf_bt[smallest]
        sjf_ct[smallest] = time
        sjf_tat[smallest] = sjf_ct[smallest] - sjf_at[smallest]
        sjf_wt[smallest] = sjf_tat[smallest] - sjf_bt[smallest]
        done[smallest] = 1
        completed = completed + 1

    else:
        time = time + 1


sjf_avg_tat = sum(sjf_tat) / len(sjf_id)
sjf_avg_wt = sum(sjf_wt) / len(sjf_id)

print("\nFor FCFS:")
print("Execution Seq:", end=" ")
for i in range(len(fcfs_id)):
    print(fcfs_id[i], end=" ")

print("\n")
print(f"{'p_id':<8}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")

for i in range(len(fcfs_id)):
    print(
        f"{fcfs_id[i]:<8}{fcfs_at[i]:<6}{fcfs_bt[i]:<6}"
        f"{fcfs_ct[i]:<6}{fcfs_tat[i]:<6}{fcfs_wt[i]:<6}"
    )

print("\nAverage TAT =", fcfs_avg_tat)
print("Average WT  =", fcfs_avg_wt)

print("\nFor SJF")
print("Execution Seq:", end=" ")
for process in sjf_seq:
    print(process, end=" ")

print("\n")
print(f"{'p_id':<8}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")

for i in range(len(sjf_id)):
    print(
        f"{sjf_id[i]:<8}{sjf_at[i]:<6}{sjf_bt[i]:<6}"
        f"{sjf_ct[i]:<6}{sjf_tat[i]:<6}{sjf_wt[i]:<6}"
    )

print("\nAverage TAT =", sjf_avg_tat)
print("Average WT  =", sjf_avg_wt)
print("\nCOMPARISON")
print(f"{'Algorithm':<12}{'Avg TAT':<12}{'Avg WT':<12}")
print(f"{'FCFS':<12}{fcfs_avg_tat:<12.1f}{fcfs_avg_wt:<12.1f}")
print(f"{'SJF':<12}{sjf_avg_tat:<12.1f}{sjf_avg_wt:<12.1f}")
