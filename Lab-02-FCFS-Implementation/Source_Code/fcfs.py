p_id = ["p0", "p1", "p2", "p3", "p4"]
at = [3, 5, 2, 1, 6]
bt = [1, 3, 2, 2, 3]

for i in range(len(at) - 1):
    for j in range(len(at) - 1 - i):
        if at[j] > at[j + 1]:
            temp = at[j]
            at[j] = at[j + 1]
            at[j + 1] = temp

            temp = bt[j]
            bt[j] = bt[j + 1]
            bt[j + 1] = temp

            temp = p_id[j]
            p_id[j] = p_id[j + 1]
            p_id[j + 1] = temp
ct = []
tat = []
wt = []
time = 0
sum_tat = 0
sum_wt = 0

for i in range(len(p_id)):
    if time < at[i]:
        t = at[i]

        ct.append(t + bt[i])
        t = ct[i]

        tat.append(ct[i] - at[i])
        wt.append(tat[i] - bt[i])

        sum_tat += tat[i]
        sum_wt += wt[i]
print("p_id\AT\BT\CT\TAT\WT")

for i in range(len(p_id)):
    print(p_id[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", wt[i])

print("Avrg TAT =", sum_tat / len(p_id))
print("Avrg WT =", sum_wt / len(p_id))

print("Execution Seq:")

for i in range(len(p_id)):
    print(p_id[i], end=" ")
