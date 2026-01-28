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

###### Class 2 ######

# Clean and prepare the data

# Check for missing (null) values across the entire DataFrame
df.isnull()

# Count the total number of missing values per column
df.isnull().sum()

# Display all unique values in the 'ano' column
df["ano"].unique()

# Show all rows that contain at least one missing value
df[df.isnull().any(axis=1)]

# Creating a new DataFrame (test example 1)
import numpy as np  # Used for numerical operations (in this case, to represent missing values with np.nan)

df_salarios = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],  # column names and values
    'salario': [4000, np.nan, 5000, np.nan, 100000]       # np.nan represents missing values
})

# Creates a new column where missing salary values are replaced
# with the mean salary, rounded to two decimal places
df_salarios['salario_media'] = df_salarios['salario'].fillna(
    df_salarios['salario'].mean().round(2)
)

df_salarios

# Creates a new column where missing salary values are replaced
# with the median salary, rounded to two decimal places
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(
    df_salarios['salario'].median().round(2)
)

df_salarios

# Creating a new DataFrame (test example 2)
df_temperaturas = pd.DataFrame({
    'dia': ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta'],  # days of the week
    'temperatura': [30, np.nan, np.nan, 28, 27]              # missing temperature values
})

# ffill (forward fill): fills missing values using the last previously available value
df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()
df_temperaturas

# bfill (backward fill): fills missing values using the next available value
df_temperaturas['preenchido_bfill'] = df_temperaturas['temperatura'].bfill()
df_temperaturas

# Creating a new DataFrame (test example 3)
df_cidades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],  # column names and values
    'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Belém']  # missing cities values
})

# Fill missing city values with a default label
df_cidades['cidade preenchida'] = df_cidades['cidade'].fillna('Não Informado')

#Exiting examples and backing to main df!!!!!

# Remove all rows containing at least one missing value
df_limpo = df.dropna()

# Verify that no missing values remain
df_limpo.isnull().sum()

# Convert the 'ano' column to integer type
df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype('int64'))



