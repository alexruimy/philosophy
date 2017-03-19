from PhilosophyFinder import PhilosophyFinder
import collections
import time

path_lengths = []
errors = []
log = []
repeat = 20
distribution = collections.Counter()

while len(path_lengths) < repeat:

  try :
    i = PhilosophyFinder()
    i.quiet = True
    result = i.find()

    while not i.complete:
      print('sleeping')
      time.sleep(2)

    if type(result) == int:
      path_lengths.append(result)

  except:
    pass

for i in path_lengths:
  distribution[i]+= 1

for k, v in distribution.most_common():
  print('%d clicks: %d' % (k, v))
