#queue-ds that follow FIFO
from collections import deque
q=deque()
q.append(10)
q.append(20)
q.popleft()
print(q)