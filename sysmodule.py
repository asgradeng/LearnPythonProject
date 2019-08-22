import sys

sys.stderr.write('this is stderr test\n')
sys.stderr.flush()
sys.stdout.write('\nthis is stdout text\n')

print(sys.argv)
if len(sys.argv) >1:
    print(sys.argv[1])
    print(float(sys.argv[2])+5)

