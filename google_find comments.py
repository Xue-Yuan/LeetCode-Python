import sys


def find_comments():
    state = 'outside'
    with open('minTrianglePath.cpp') as infile:
        file = infile.read()
        idx = 0
        while idx < len(file):
            cur = file[idx]
            idx += 1
            if state == 'outside':
                if cur == '/':
                    nxt = file[idx]
                    if nxt == '*':
                        state = 'multi'
                        idx += 1
                    elif nxt == '/':
                        state = 'single'
                        idx += 1
                elif cur == '"':
                    state = 'quote'
            elif state == 'quote':
                if cur == '"':
                    state = 'outside'
            elif state == 'multi':
                if cur == '*':
                    nxt = file[idx]
                    if nxt == '/':
                        state = 'outside'
                        sys.stdout.write('\n')
                        idx += 1
                else:
                    sys.stdout.write(cur)
            elif state == 'single':
                if cur == '\n':
                    state = 'outside'
                    sys.stdout.write('\n')
                else:
                    sys.stdout.write(cur)

find_comments()
