#use only one if in entire program



#sets
invited = {"Alice" , "Bob" , "Charlie"}
arrived = {"Alice" , "Charlie" , "Diana" }

not_invited = arrived - invited

if not_invited:
	print("Unexpected guests arrived :",*not_invited)
