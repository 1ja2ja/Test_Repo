import pandas as pd

# Lese die HTML-Tabelle von einer Datei
with open('table.html', 'r') as f:
    table = f.read()

# Konvertiere die HTML-Tabelle in einen Pandas DataFrame
df = pd.read_html(table)[0]

# Schreibe den DataFrame in eine Excel-Datei
df.to_excel('table.xlsx', index=False)
