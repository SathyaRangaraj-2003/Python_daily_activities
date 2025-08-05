#activity_14:

log_lines = (f"Line {i}" if i != 99999 else "ERROR: Something failed" for i in range(10**6))

print(next(log_lines))


for i, line in enumerate(log_lines, start=1):
    if i == 100000:
        print(f"line:{i} -> {line.lower()}")
        break


# actual o/p : line:100000 -> error:Something failed