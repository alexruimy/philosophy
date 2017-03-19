from PhilosophyFinder import PhilosophyFinder
import collections
import time
import sys

repeat = 20
quiet = False

args = sys.argv[1:]
path_lengths = []
errors = []
log = []

distribution = collections.Counter()

if 'quiet' in args:
  quiet = True
  args.remove('quiet')

try:
  repeat = int(args[0])
except:
  pass

print('Checking %d articles' % repeat)

while len(path_lengths) < repeat:

  try :
    i = PhilosophyFinder()
    i.quiet = quiet
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
