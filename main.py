#coding=utf-8

import sys

def start():
  if (len(sys.argv) >= 2):
    module = sys.argv[1]
    if (module == 'nice'):
      import nice as plat
    elif (module == 'du'):
      import du as plat

    plat.run()
  else:
    print("plz input python main.py nice or python mian.py du")

if __name__=='__main__':
    start()