s = 'hello'
print s[1]
print len(s)
print s + ' world'

pi = 3.14
##kalau tidak ad str tidak bisa jalan
text = 'the value of pi is ' + str(pi)
print text

text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'boni', 'bani', 'bene')
print('Hasil: {}'.format(text))

speed = ''
mood = ''
raw_input("Speed: ")
raw_input("Mood: ")
if speed >= 80:
  print 'License and registration please'
  if mood == 'terrible' or speed >= 100:
    print 'You have the right to remain silent.'
  elif mood == 'bad' or speed >= 90:
    print "i'm going to have to write you a ticket."
    write_ticket()
  else:
    print "Let's try to keep it under 80 ok?"


