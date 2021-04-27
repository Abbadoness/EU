class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def push(self, item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items)-1]
  def size(self):
    return len(self.items)

contro1 = []
contro2 = []

n = int(input())
C = list(map(int,input().strip().split()))[:]
C1 = C[n:]
w = []
sobras = []
listadep = []
for i in range(n):
  w.append(Stack())
  listadep.append([])

for i in range(len(C)):
  for j in range(n):
    if w[j].isEmpty():
      w[j].push(C[i])
      contro1.append(C[i])
      break

i = 0
j = 0
contador = 0
maior = 0
while contador <= (len(C)-n)*n:
  if n <= i:
    i=0
  if C1[0] <= w[i].peek():
    w[i].push(C1[0])
    contro2.append(C1[0])
    C1.pop(0)
    if len(C1) == 0:
      contador = (len(C)-n)*n
  else:
    for t in range(n):
      if C1[0] > w[t].peek():
        maior += 1
    if maior >= n:
      sobras.append(C1[0])
      C1.pop(0)
      if len(C1) == 0:
        contador = (len(C)-n)*n
    maior = 0
  i+=1
  contador+=1


for i in range(n):
  listadepilhas.append([])

for i in range(n):
  for j in range(w[i].size()):
    listadepilhas[i].append(w[i].pop())

for i in range(n):
  listadepilhas[i].sort()
  listadepilhas[i].reverse()

for i in range(n):
  for j in range(len(listadepilhas[i])):
    listadep[i] += listadepilhas[j]