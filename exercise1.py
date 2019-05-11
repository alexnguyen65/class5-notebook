import argparse, sys, time, random, os

parser = argparse.ArgumentParser(description="Process some integers")
parser.add_argument("myinteger")
args = parser.parse_args()
print(args.myinteger)

print(sys.argv[1])

print(time.localtime())
print(random.randrange(10))
print(os.getlogin())

