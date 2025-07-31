#activity_07:

def tag(text , wrapper):
	return f"<{wrapper}>{text}</{wrapper}>"
print(tag("hi" , "p"))