def fcfs(requests, head):
    movement = 0

    for request in requests:
        movement += abs(head - request)
        head = request

    return movement


def sstf(requests, head):
    movement = 0
    requests = requests.copy()

    while requests:
        nearest = min(requests, key=lambda x: abs(head - x))

        movement += abs(head - nearest)
        head = nearest

        requests.remove(nearest)

    return movement


def cscan(requests, head, disk_size):
    movement = 0

    right = []
    left = []

    for request in requests:
        if request >= head:
            right.append(request)
        else:
            left.append(request)

    right.sort()
    left.sort()

    for request in right:
        movement += abs(head - request)
        head = request

    movement += abs(head - (disk_size - 1))
    head = disk_size - 1

    movement += disk_size - 1
    head = 0

    for request in left:
        movement += abs(head - request)
        head = request

    return movement


def clook(requests, head):
    movement = 0

    right = []
    left = []

    for request in requests:
        if request >= head:
            right.append(request)
        else:
            left.append(request)

    right.sort()
    left.sort()

    for request in right:
        movement += abs(head - request)
        head = request

    if left:
        movement += abs(head - left[0])
        head = left[0]

        for request in left:
            movement += abs(head - request)
            head = request

    return movement


def rss(requests, head):
    movement = 0

    for request in requests:
        movement += abs(head - request)
        head = request

    return movement


# Program starts here

requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
disk_size = 200

print("----- DISK SCHEDULING -----")
print("Disk Requests:", requests)
print("Initial Head:", head)
print()

print("FCFS   :", fcfs(requests, head))
print("SSTF   :", sstf(requests, head))
print("C-SCAN :", cscan(requests, head, disk_size))
print("C-LOOK :", clook(requests, head))
print("RSS    :", rss(requests, head))