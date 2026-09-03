p_id = ["p1", "p2", "p3", "p4", "p5"]
at = [0, 1, 2, 3, 5]
bt = [3, 4, 6, 4, 2]

priority = [3, 2, 4, 6, 10]

n = len(p_id)

np_ct = [0] * n
np_tat = [0] * n
np_wt = [0] * n
done = [0] * n

time = 0
completed = 0
np_exe_seq = []


while completed < n:
    highest = -1


    for i in range(n):
        if at[i] <= time and done[i] == 0:
            if highest == -1 or priority[i] < priority[highest]:
                highest = i


    if highest == -1:
        time = time + 1

    else:

        np_exe_seq.append(p_id[highest])
        time = time + bt[highest]
        np_ct[highest] = time
        np_tat[highest] = np_ct[highest] - at[highest]
        np_wt[highest] = np_tat[highest] - bt[highest]
        done[highest] = 1
        completed = completed + 1


np_avg_tat = sum(np_tat) / n
np_avg_wt = sum(np_wt) / n

remaining = bt.copy()

p_ct = [0] * n
p_tat = [0] * n
p_wt = [0] * n

time = 0
completed = 0
p_exe_seq = []

while completed < n:
    highest = -1

    for i in range(n):
        if at[i] <= time and remaining[i] > 0:
            if highest == -1 or priority[i] < priority[highest]:
                highest = i

    if highest == -1:
        time = time + 1

    else:

        p_exe_seq.append(p_id[highest])
        remaining[highest] = remaining[highest] - 1
        time = time + 1

        if remaining[highest] == 0:
            p_ct[highest] = time
            completed = completed + 1

for i in range(n):
    p_tat[i] = p_ct[i] - at[i]
    p_wt[i] = p_tat[i] - bt[i]

p_avg_tat = sum(p_tat) / n
p_avg_wt = sum(p_wt) / n

print("\nNON-PREEMPTIVE PRIORITY:")
print("Execution Sequence:", end=" ")

for process in np_exe_seq:
    print(process, end=" ")

print("\n")
print(f"{'PID':<8}{'AT':<6}{'BT':<6}{'Priority':<10}{'CT':<6}{'TAT':<6}{'WT':<6}")

for i in range(n):

    print(
        f"{p_id[i]:<8}{at[i]:<6}{bt[i]:<6}"
        f"{priority[i]:<10}{np_ct[i]:<6}"
        f"{np_tat[i]:<6}{np_wt[i]:<6}"
    )

print("\nAverage TAT =", np_avg_tat)
print("Average WT  =", np_avg_wt)

print("\nPREEMPTIVE PRIORITY:")
print("Execution Sequence:", end=" ")

for process in p_exe_seq:
    print(process, end=" ")

print("\n")
print(f"{'PID':<8}{'AT':<6}{'BT':<6}{'Priority':<10}{'CT':<6}{'TAT':<6}{'WT':<6}")

for i in range(n):

    print(
        f"{p_id[i]:<8}{at[i]:<6}{bt[i]:<6}"
        f"{priority[i]:<10}{p_ct[i]:<6}"
        f"{p_tat[i]:<6}{p_wt[i]:<6}"
    )

print("\nAverage TAT =", p_avg_tat)
print("Average WT  =", p_avg_wt)

print("\nComparison:")
print(f"{'Algorithm':<25}{'Avrg TAT':<15}{'Avrg WT':<15}")
print(f"{'NON-PREEMPTIVE PRIORITY:':<25}{np_avg_tat:<15.2f}{np_avg_wt:<15.2f}")
print(f"{'PREEMPTIVE PRIORITY:':<25}{p_avg_tat:<15.2f}{p_avg_wt:<15.2f}")
