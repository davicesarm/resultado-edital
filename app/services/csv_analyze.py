import pandas as pd

form = pd.read_csv("form.csv")
def nomes() -> list[str]:
    return form['Nome Completo'].to_list()

def aptos():
    return form[["Nome Completo", "Apto"]].to_records()

print(aptos())