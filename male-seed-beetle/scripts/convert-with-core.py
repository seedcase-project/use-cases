import polars as pl
import re
from pathlib import Path

#Transform from tab sep to comma sep
with open('../data-raw/data.csv', 'r') as tsv:

    with open('../data-raw/data1.csv', 'w') as csv:

        for line in tsv:

            content = re.sub("\t", ",", line) 

            csv.write(content)

Path('../data-raw/data.csv').unlink()

Path('../data-raw/data1.csv').rename('../data-raw/data.csv')

#Find the columns with type string, then check for pure numerical 
# values as that may indicate that there is a conversion error

df = pl.read_csv('../data-raw/data.csv')

for col, dtype in zip(df.columns, df.dtypes):
    if dtype == pl.Utf8:
        print(f"{col}: {dtype}")

        for value in df[col]:
            if value.isdigit():
                print(f"Numerical value found in column {col}: {value}")

#Update from scream to lowercase, as that will create snake_case in this file

df = pl.read_csv('../data-raw/data.csv')

column_names = {col: col.lower() for col in df.columns}

df = df.rename(column_names)

df.write_csv('../data-raw/data.csv')

# Update abbreviated values to full text
treatment_map = {"V":"Virgin", "M":"Mating"}

df = df.with_columns(
    treatment=pl.col("treatment").replace_strict(treatment_map)
)
df.write_csv('../data-raw/data.csv')

'''
"CYCLE":"FOCAL_CYCLE", 
"O2":"02_Consumed", 
"CO2":"C02_Produced", 
"RQ":"Respiratory_quotient", 
"BLOCK":"Experimental_Block", 
"ACTIVITY":"ACTIVITY", 
"STRAIN":"STRAIN", 
"MT_DNA_HAPLOTYPE":"Mitochodrial_DNA_Haplotype", 
"NC_GENOTYPE":"Nuclear_Lineage", 
"TREATMENT":"TREATMENT", 
"COEVOL":"Coadaptation", 
"W_V":"Virgin_Body_Weight", 
"W_M1":"Weight_after_Mating1", 
"W_M1R":"WaM1_after_Respirometry", 
"EJAC1":"Ejaculate_Weight_First_Mating", 
"EJAC2":"Ejaculate_Weight_Second_Mating", 
"COPULDUR_1":"Copulation_Duration_First_Mating", 
"COPULDUR_2":"Copulation_Duration_Second_Mating", 
"ID":"ID"
'''

