from PhilosophyFinder import PhilosophyFinder
import sys

args = ' '.join(sys.argv[1:])

if args == 'random':
  search = ''

elif args == '':
  search = input('Enter search term, or leave blank for random\n-->: ')

w = PhilosophyFinder()
w.find(search)
