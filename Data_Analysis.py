import pandas as pd

#Import data archive
#Use data .read_[Type]("Link")
#Data base downloaded from Kaggle
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df.head() #Read entire table
#df.head(10) #Read only the 10 first columns

df.info() #Bring important info. about your df

df.describe() #Shows you statistics about your df (Max, min, mean, average)

df.shape #If you run it, shows you the size of the archive (lines x columns)
line, column = df.shape[0], df.shape[1] #Vetor 0 save the information of lines, and vector 1 save the number of columns.
print("Number of Lines: ", line) #saving numbers into variable and print
print("Number of Columns: ", column) #saving numbers into variable and print

df.columns #Shows you the name of all columns in your DF

#Create a dictionary for your df columns
dictionary_columns_ptbr = {
    "work_year": "ano",
    "experience_level": "senioridade",
    "employment_type": "contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda",
    "salary_in_usd": "usd",
    "employee_residence": "residencia",
    "remote_ratio": "remoto",
    "company_location": "empresa",
    "company_size": "tamanho_empresa"
}

df = df.rename(columns=columns_dictionary_ptbr)
df.columns

df["senioridade"].value_counts() #Show you the resume of counts of itens in your column
df["contrato"].value_counts() #Show you the resume of counts of itens in your column
df["remoto"].value_counts() #Show you the resume of counts of itens in your column
df["tamanho_empresa"].value_counts() #Show you the resume of counts of itens in your column

#Create a dictionary for the data into the columns (Senioridade)
dictionary_senioridade_column_ptbr = {
    "SE": "Senior",
    "MI": "Pleno",
    "EN": "Junior",
    "EX": "Executivo"
}

df["senioridade"] = df["senioridade"].replace(dictionary_senioridade_column_ptbr)
df["senioridade"].value_counts()

#Create a dictionary for the data into the columns (Contrato)
dictionary_contrato_column_ptbr = {
    "FT": "Tempo Integral",
    "CT": "Tempo Parcial",
    "PT": "Freela",
    "FL": "Contrato"
}

df["contrato"] = df["contrato"].replace(dictionary_contrato_column_ptbr)
df["contrato"].value_counts()

#Create a dictionary for the data into the columns (tamanho_empresa)
dictionary_tamanho_empresa_column_ptbr = {
    "S": "Pequena",
    "M": "Media",
    "L": "Grande"
}

df["tamanho_empresa"] = df["tamanho_empresa"].replace(dictionary_tamanho_empresa_column_ptbr)
df["tamanho_empresa"].value_counts()

#Create a dictionary for the data into the columns (remoto)
dictionary_remoto_column_ptbr = {
    0: "Presencial",
    50: "Remoto",
    100: "Hibrido"
}

df["remoto"] = df["remoto"].replace(dictionary_remoto_column_ptbr)
df["remoto"].value_counts()

df.head()

df.describe(include="object")
#Count: How many itens this column have in the total
#Unique: How many unique values this category have (Executivo, pleno, senior, junior)
#Top: Which information shows with more frequecy
#Freq: Cal. of the frequency (How many times the top value repeat)

