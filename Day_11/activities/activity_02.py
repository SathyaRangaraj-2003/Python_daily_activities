#guests setA = invited by email ,
# setB = invited by phone, 
# setC = blocked guest

# manage 3 guest lists invited by email,phone,blocked guests
# print set of peopple invited both email and phone but not blocked plus only blocked list and nowhere else

setA={'A','B','C'}
setB={'C','D','E'}
setC={'C','D','E','F'}


print(((setA & setB ) - setC ) | setC - (setA | setB) )
