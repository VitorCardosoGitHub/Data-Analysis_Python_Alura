import pandas as pd

#Import data archive
#Use data .read_[Type]("Link")
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

#Create a dictionary for you df
columns_dictionary_ptbr = {
    "work_year": "ano_trabalho",
    "experience_level": "nivel_experiencia",
    "employment_type": "tipo_contrato",
    "job_title": "cargo",
    "salary": "salario",
    "salary_currency": "moeda_salario",
    "salary_in_usd": "salario_em_usd",
    "employee_residence": "residencia_funcionario",
    "remote_ratio": "percentual_remoto",
    "company_location": "localizacao_empresa",
    "company_size": "tamanho_empresa"
}

df = df.rename(columns=columns_dictionary_ptbr)
df.columns