print('A. match_ends')
def match_ends(words):
  a = 0
  for i in words:
        if len(i) >= 2 and i[0]==i[-1]:
                a = a+1
  return a

print('B. front_x')
def front_x(words):
  x = []
  xx = []
  for word in words:
      if word.startswith('x') or word.startswith('X'):
        x.append(word)
      else:
        xx.append(word)
  return sorted(x) + sorted(xx)
