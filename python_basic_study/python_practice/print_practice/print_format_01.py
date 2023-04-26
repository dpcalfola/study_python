print("%d" % 100)
print("%d" % 200, 300)

# print('%d %d' % 10)
# TypeError: not enough arguments for format string

print("%d / %d = %.2f" % (100, 200, 0.5))
print("%d / %d = %2.5f" % (100, 200, 0.5))

print()

print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))

print("{2:d} {1:d} {0:d}".format(123, 456, 789))
