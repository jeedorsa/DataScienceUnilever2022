#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[6]:


df = pd.read_csv('./mortgages (1).csv')
df.head(100)


# El conjunto de datos que se te da aquí es el conjunto de datos hipotecario usado anteriormente en este curso. Tu meta es reproducir un gráfico. El plot negro es la hipoteca de 30 años al 5% y la línea azul es al 3%. Lo que está graficado es el interés acumulado pagado en el transcurso del préstamo. Nota que no es un gráfico hermoso. No dice qué línea corresponde a qué hipoteca y el gráfico en sí no es visualmente el más atractivo. Estos son los tipos de problemas que se cubren a lo largo del curso. 

# In[14]:


df.info()
df.isnull().sum()


# In[20]:


plt.style.use('seaborn')
plt.plot( df['Month'], df['Interest Paid'])


# In[ ]:


# suma acumulativa 
#https://es.acervolima.com/python-pandas-series-cumsum-para-encontrar-la-suma-acumulativa-de-una-serie/


# In[57]:


años = df["Mortgage Name"] == "30 Year"
tasa3 =  df["Interest Rate"] == float('0.03')
tasa3 =  df["Interest Rate"] == 0.03
tasa5 =  df["Interest Rate"] == float('0.05')
#de las dos formas me trae el valor correcto 
df_30year3 = df.loc[tasa3 & años  , :]
df_30year5 = df.loc[tasa5 & años  , :]
df_30year3
df_30year5
#tasa3


# In[58]:


#f['Interest Paid']
#f['Interest Paid']
#eries.cumsum(skipna = False) 
#f[Ac3%] = df['Interest Paid'].cumsum(skipna = False) 
df_30year3['Ac3%']= df_30year3['Interest Paid'].cumsum(skipna = False) 
#f['InterestPaid5%] = df[]
df_30year3


# In[59]:


#f['Interest Paid']
#f['Interest Paid']
#eries.cumsum(skipna = False) 
#f[Ac3%] = df['Interest Paid'].cumsum(skipna = False) 
df_30year5['Ac3%']= df_30year5['Interest Paid'].cumsum(skipna = False) 
#f['InterestPaid5%] = df[]
df_30year5


# In[74]:


fig, ax = plt.subplots()
plt.plot( df_30year3['Month'], df_30year3['Ac3%'], label = 'Credito Hipotecario 3%')
plt.plot( df_30year5['Month'], df_30year5['Ac3%'], label = 'Credito Hipotecario 5%')
#plt.plot(  df_30year['Ac3%'],df_30year['Month'])
#axes.set_xlim(left=1892,right=2020)
#axes.set_ylim(bottom=0,top=1800)
#axes.set_xlabel('Year', fontsize = 16)
plt.ylabel('Monto Acumulado')
plt.ylabel('Meses')
plt.title('Diferencia de creditos hipotecarios')
ax.legend(loc = 'lower right' )
#https://aprendeconalf.es/docencia/python/manual/matplotlib/
plt.show()


# In[65]:





# In[ ]:




