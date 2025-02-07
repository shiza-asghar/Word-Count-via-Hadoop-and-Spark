import sys
for line in sys.stdin:
    words = line.strip().lower().split()
    for word in words:
        print(f"{word}\t1")
