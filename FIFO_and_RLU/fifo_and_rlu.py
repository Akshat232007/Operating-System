def fifo(pages, frames):
    memory = []
    hits = 0
    misses = 0

    for page in pages:
        if page in memory:
            hits += 1
        else:
            misses += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        print("Page:", page, "Memory:", memory)

    print("Hits:", hits)
    print("Misses:", misses)
    print("Hit Ratio:", hits / len(pages))
    print("Miss Ratio:", misses / len(pages))


def lru(pages, frames):
    memory = []
    hits = 0
    misses = 0

    for page in pages:
        if page in memory:
            hits += 1
            memory.remove(page)
            memory.append(page)
        else:
            misses += 1

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        print("Page:", page, "Memory:", memory)

    print("Hits:", hits)
    print("Misses:", misses)
    print("Hit Ratio:", hits / len(pages))
    print("Miss Ratio:", misses / len(pages))


pages = [1, 2, 3, 1, 4, 5, 2, 1, 2, 3]
frames = 3

print("FIFO Page Replacement")
fifo(pages, frames)

print("\nLRU Page Replacement")
lru(pages, frames)
