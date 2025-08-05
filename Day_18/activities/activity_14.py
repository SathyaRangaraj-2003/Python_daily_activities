#activity_14:

log_lines = (f"Line {i}" if i != 99999 else "ERROR: Something failed" for i in range(10**6))


for line_number, line in enumerate(log_lines, start=1):
    if "ERROR" in line:
        print(f"LINE:{line_number} -> {line}")
        break


