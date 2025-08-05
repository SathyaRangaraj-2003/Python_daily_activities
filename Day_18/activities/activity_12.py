#activity_12:

raw_guests = [" alice ", "", "Bob", "ALICE", " bob ", " Eve ", "eve", " ", "  ANAND"]

s = set()

for item in raw_guests:
	if item.strip():
		word = item.strip()
		res = word.capitalize()
		s.add(res)
d = {k:len(k) for k in s}
print(d)