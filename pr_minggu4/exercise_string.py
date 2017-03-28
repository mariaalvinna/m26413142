print('A. donuts')
def donuts(count):
  don = "Number of donuts: "
  if count < 10:
    don = don + str(count)
  elif count >= 10:
    don = don + "many"
  return don

print('B. both_ends')
def both_ends(a):
  if len(a) < 2:
    return ''
  temp = a[0:2]
  hasil = a[-2:]
  return temp + hasil

print('C. fix_start')
def fix_start(a):
  awal = a[0]
  akhir = a[1:]
  tukar = akhir.replace(awal, '*')
  return awal + tukar 
