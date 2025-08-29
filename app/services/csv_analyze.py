import pandas as pd

form = pd.read_csv("form.csv")
def nomes() -> list[str]:
    return form['Nome Completo'].to_list()

def campi() -> list[str]:
    return form["Campus (cidade) e turno:"].unique().tolist()

def aptos():
    aptos_por_campus = {}
    
    for campus in campi():
        aptos_por_campus[campus] = form[(form["Campus (cidade) e turno:"] == campus)][["Carimbo de data/hora", "Nome Completo", "Apto"]].to_records().tolist()

    return aptos_por_campus

def aptos_por_campus(campus: str) -> list[str]:
    form_filtrado = form[(form["Campus (cidade) e turno:"] == campus)][["Carimbo de data/hora", "Nome Completo", "Apto"]]

    form_filtrado["Carimbo de data/hora"] = pd.to_datetime(
        form_filtrado["Carimbo de data/hora"], 
        format="%m/%d/%Y %H:%M:%S"
    )

    form_filtrado["Carimbo de data/hora"] = form_filtrado["Carimbo de data/hora"].dt.strftime("%d/%m/%Y %H:%M:%S")

    return form_filtrado.to_records().tolist()


print(aptos_por_campus("Campus Campina Grande - Turno da Tarde"))