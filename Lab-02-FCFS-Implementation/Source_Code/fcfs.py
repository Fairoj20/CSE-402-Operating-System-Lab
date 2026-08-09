p_id = ["p0", "p1", "p2", "p3", "p4"]
at = [3, 5, 2, 1, 6]
bt = [1, 3, 2, 2, 3]

for i in range(len(at) - 1):
    for j in range(len(at) - 1 - i):
        if at[j] > at[j + 1]:
           at[j], at[j + 1] = at[j + 1], at[j]
      bt[j], bt[j + 1] = bt[j + 1], bt[j]
      p_id[j], p_id[j + 1] = p_id[j + 1], p_id[j]
ct = []
tat = []
wt = []
current_time = 0
sum_tat = 0
sum_wt = 0

for i in range(len(p_id)):
   if current_time < at[i]:
    current_time = at[i]

  current_time += bt[i]
  ct.append(current_time)


  tat.append(ct[i] - at[i])
  wt.append(tat[i] - bt[i])

  sum_tat += tat[i]
  sum_wt += wt[i]
print(f"{'p_id':<8}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")
for i in range(len(p_id)):
  print(
      f"{p_id[i]:<8}{at[i]:<6}{bt[i]:<6}{ct[i]:<6}{tat[i]:<6}{wt[i]:<6}"
  )
print("\nAvrg TAT =", sum_tat / len(p_id))
print("Avrg WT =", sum_wt / len(p_id))

print("\nExecution Seq:")

for i in range(len(p_id)):
    print(p_id[i], end=" ")
