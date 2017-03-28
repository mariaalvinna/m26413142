
colors = ['red', 'blue', 'green']
print colors[0]
print colors[2]
print len(colors)

squares = [1, 4, 6, 8, 10, 15, 20, 27]
sum = 0
for num in squares:
  sum += num
print ('Total: {}'.format(sum))

list = ['larry', 'curly', 'moe']
if 'curly' in list:
  print 'yay'

for i in range(20):
  print i

i = 0
a = [1, 2, 3, 4, 5]
while i < len(a):
  print ('Hasil: {}'.format(a[i]))
  i = i + 3

list = [1, 5, 10]
list.append(15)
list.insert(2, 'lili')
list.extend(['lulu', 'cindy'])
list.pop(2)
print list

list = ['a', 'd', 'f', 'h']
print list[1:-1]
list[0:2] = 'z'
print list
