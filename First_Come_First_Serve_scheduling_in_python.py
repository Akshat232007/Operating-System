fcfs_processes = [
    [1, 0, 5],
    [2, 1, 3],
    [3, 2, 8],
    [4, 3, 6]
]

sjf_processes = [
    [1, 0, 7, False],
    [2, 2, 4, False],
    [3, 4, 1, False],
    [4, 5, 4, False]
]


def print_cli_gantt(gantt_data):
    chart_line = "|"
    time_line = f"{gantt_data[0][1]}"

    for label, _, et in gantt_data:
        cell = f" {label} "
        chart_line += f"{cell}|"
        time_line += f"{et:>{len(cell)+1}}"

    print("\nCLI GANTT CHART:")
    print(chart_line)
    print(time_line)


def run_fcfs():
    print("=" * 60)
    print("        EXECUTION STEPS: FCFS SCHEDULING")
    print("=" * 60)

    current_time = 0
    results = []
    gantt = []

    for proc in fcfs_processes:
        pid, at, bt = proc[0], proc[1], proc[2]

        if current_time < at:
            print(f"Time {current_time} to {at}: CPU is IDLE")
            current_time = at

        st = current_time
        ct = st + bt
        tat = ct - at
        wt = tat - bt

        print(f"Time {st} to {ct}: Process P{pid} is EXECUTING (Burst: {bt}ms)")
        print(f"  --> P{pid} Completed at {ct}ms | TAT: {tat}ms | WT: {wt}ms")

        current_time = ct
        results.append([pid, at, bt, ct, tat, wt])
        gantt.append((f"P{pid}", st, ct))

    print("\nFCFS SUMMARY TABLE:")
    print("Process | Arrival | Burst | Complete | Turnaround | Waiting")
    print("-" * 55)
    total_tat, total_wt = 0, 0
    for r in results:
        print(f"  P{r[0]}    |    {r[1]}    |   {r[2]}   |    {r[3]:<5} |     {r[4]:<5}  |   {r[5]}")
        total_tat += r[4]
        total_wt += r[5]

    n = len(results)
    print("-" * 55)
    print(f"Average Waiting Time    = {total_wt / n:.2f} ms")
    print(f"Average Turnaround Time = {total_tat / n:.2f} ms")

    print_cli_gantt(gantt)
    print("\n")


def run_sjf():
    print("=" * 60)
    print("  EXECUTION STEPS: NON-PREEMPTIVE SJF SCHEDULING")
    print("=" * 60)

    n = len(sjf_processes)
    completed = 0
    current_time = 0
    results = []
    gantt = []
    procs = [p[:] for p in sjf_processes]

    while completed < n:
        available = [p for p in procs if p[1] <= current_time and not p[3]]

        if not available:
            print(f"Time {current_time}: CPU is IDLE waiting for processes to arrive")
            current_time += 1
            continue

        shortest = min(available, key=lambda x: x[2])
        pid, at, bt = shortest[0], shortest[1], shortest[2]

        st = current_time
        ct = st + bt
        tat = ct - at
        wt = tat - bt

        print(f"Time {st} to {ct}: Process P{pid} selected (Shortest Burst: {bt}ms)")
        print(f"  --> P{pid} Completed at {ct}ms | TAT: {tat}ms | WT: {wt}ms")

        shortest[3] = True
        completed += 1
        current_time = ct

        results.append([pid, at, bt, ct, tat, wt])
        gantt.append((f"P{pid}", st, ct))

    results.sort(key=lambda x: x[0])

    print("\nSJF SUMMARY TABLE:")
    print("Process | Arrival | Burst | Complete | Turnaround | Waiting")
    print("-" * 55)
    total_tat, total_wt = 0, 0
    for r in results:
        print(f"  P{r[0]}    |    {r[1]}    |   {r[2]}   |    {r[3]:<5} |     {r[4]:<5}  |   {r[5]}")
        total_tat += r[4]
        total_wt += r[5]

    print("-" * 55)
    print(f"Average Waiting Time    = {total_wt / n:.2f} ms")
    print(f"Average Turnaround Time = {total_tat / n:.2f} ms")

    print_cli_gantt(gantt)
    print("\n")


# Execute both algorithms on CLI
run_fcfs()
run_sjf()
