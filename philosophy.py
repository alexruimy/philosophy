from PhilosophyFinder import PhilosophyFinder
import sys

args = ' '.join(sys.argv[1:])

if args == '':
  search = input('Enter search term, or leave blank for random\n-->: ')

elif args == 'random':
  search = ''

else:
  search = args

w = PhilosophyFinder()
w.find(search)
