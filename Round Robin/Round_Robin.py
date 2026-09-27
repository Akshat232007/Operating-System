processes = [
    ["P1", 0, 5],
    ["P2", 1, 3],
    ["P3", 2, 6]
]

quantum = 2

remaining = [p[2] for p in processes]
completion = [0, 0, 0]
queue = []
visited = [False, False, False]
gantt = []
time = 0

while True:
    for i in range(3):
        if processes[i][1] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True

    if len(queue) == 0:
        time += 1
        continue

    i = queue.pop(0)

    start = time
    run = min(quantum, remaining[i])
    time += run
    remaining[i] -= run
    gantt.append((processes[i][0], start, time))

    for j in range(3):
        if processes[j][1] <= time and not visited[j]:
            queue.append(j)
            visited[j] = True

    if remaining[i] > 0:
        queue.append(i)
    else:
        completion[i] = time

    if all(x == 0 for x in remaining):
        break

tat = []
wt = []

for i in range(3):
    tat.append(completion[i] - processes[i][1])
    wt.append(tat[i] - processes[i][2])

print("Round Robin")
print("Gantt Chart:")

for p, start, end in gantt:
    print("|", p, end=" ")

print("|")
print("Completion Time:", completion)
print("Turnaround Time:", tat)
print("Waiting Time:", wt)
print("Average Turnaround Time:", sum(tat) / 3)
print("Average Waiting Time:", sum(wt) / 3)