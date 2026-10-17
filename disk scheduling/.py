#FCFS Disk Scheduling — Unordered Request Sequence

req_seq = [0,14,30,41,50,62,79,100,114,62]
head = 50
total_movement = 0
print("FCFS Disk Scheduling")
 
print("\nSequence:")
print(head, end=" -> ")
 
for i in range(len(req_seq)):
 
    movement = abs(req_seq[i] - head)
    total_movement = total_movement + movement
    head = req_seq[i]
    print(head, end=" -> ")
 
print("\n\nTotal Head Movement =", total_movement)
 
#FCFS Disk Scheduling — Ordered Request Sequence
req_seq = [0,14,30,41,50,62,62,79,100,114]
head = 50
total_movement = 0
print("FCFS Disk Scheduling")
 
print("\nSequence:")
print(head, end=" -> ")
 
for i in range(len(req_seq)):
 
    movement = abs(req_seq[i] - head)
    total_movement = total_movement + movement
    head = req_seq[i]
    print(head, end=" -> ")
 
print("\n\nTotal Head Movement =", total_movement)
 
#SSTF Disk Scheduling
req_seq = [3,4,10,25,30,60]
head = 41
total_movement = 0
visited = [0] * len(req_seq)
sequence = []
 
while len(req_seq) > 0:
    shortest = 0
    for i in range(1,len(req_seq)):
        if abs(req_seq[i] - head) < abs(req_seq[shortest] - head):
            shortest = i
    movement = abs(req_seq[shortest] - head)
    total_movement = total_movement + movement
    head = req_seq[shortest]
 
    sequence.append(head)
    req_seq.pop(shortest)
 
print("SSTF Disk Scheduling")
print("\nSequence:")
print(41, end=" -> ")
for i in range(len(sequence)):
    print(sequence[i], end=" -> ")
 
 
print("\n\nTotal Head Movement =", total_movement)
 
