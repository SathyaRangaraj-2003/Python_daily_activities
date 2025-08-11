#pandas

'''

#series

#from dictionary to series

import pandas as pd
data = pd.Series({'A' : 10 , 'B' : 20 , 'C' : 30})
print(data)


#list to series

import pandas as pd
data = pd.Series([10,20,30,40])
print(data)


#boolean indexing in series:

import pandas as pd
data = pd.Series([10,20,30,40])
print(data > 20 )


# filtering based on boolean condition

import pandas as pd
data = pd.Series([10,20,30,40])
print(data[data > 20] )

'''