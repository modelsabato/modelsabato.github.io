import numpy as np
import pandas as pd

filename = 'datos.csv'
num_datos = np.random.random(size=(500,3))
col_names = ['Col A', 'Col B', 'Col C']

with open(filename, 'w') as f:
    f.write(col_names[0]+','+col_names[1]+','+col_names[2]+'\n')
    for j in range(num_datos.shape[0]):
        f.write(str(num_datos[j,0])+','+str(num_datos[j,1])+','+str(num_datos[j,2])+'\n')

filename_v2 = 'datos_pd.csv'

df = pd.DataFrame(data=num_datos,columns=col_names)
df.to_csv(filename_v2,index=False)

