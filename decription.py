# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 00:41:21 2018

@author: ManasiAdmin
"""
import pandas as pd
def save_doc(lines, filename):
	data = '\n'.join(lines)
	file = open(filename, 'w')
	file.write(data)
	file.close()
Description_df = pd.read_csv(r"Online_Retail_final_final.csv")
Description_df
df1=Description_df['Description']
final = []
df1.shape
for i in range(df1.shape[0]):
    final.append(df1[i])
final
out_filename = 'description_string.txt'
save_doc(final, out_filename)
