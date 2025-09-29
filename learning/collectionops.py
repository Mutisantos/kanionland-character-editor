from collections import Counter, deque


def count_occurrences(collection):
    return Counter(collection)


entries = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
occurrence_count = count_occurrences(entries)
print(occurrence_count)


# Using deque for efficient appends and pops from both ends
def manage_deque():
    d = deque(maxlen=5)  # Limit size to 5
    for i in range(10, 200, 13):
        d.append(i)
        print(f'Deque after appending {i}: {d}')
    d.appendleft(9999)
    print(f'Deque after appending 99 to the left: {d}')
    d.pop()
    print(f'Deque after popping from the right: {d}')
    d.popleft()
    print(f'Deque after popping from the left: {d}')


manage_deque()
