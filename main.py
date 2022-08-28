import time, sys

try:
    import bext
except ImportError:
    print("you need bext module")
    sys.exit()

print('Press Ctrl-C to stop.')
time.sleep(3)

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end=' ')
        bext.fg("red")
        print("##", end=" ")
        bext.fg("yellow")
        print('##', end=' ')
        bext.fg("green")
        print('##', end=' ')
        bext.fg("blue")
        print('##', end=' ')
        bext.fg("cyan")
        print('##', end=' ')
        bext.fg("purple")
        print("##", end=" ")

        if indentIncreasing:
            indent += 1
            if indent == 60:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

        time.sleep(0.2)
except KeyboardInterrupt:
    sys.exit()

