import pandas as pd
SHEET_ID = '10GKGOmX7Y8xb6RK-2SxlbXMfwfxeix6q'
SHEET_NAME = 'attendance'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'

def getData():
    df = pd.read_csv(url)
    for i in df.columns:
        if i=='Student Name':
            name = df[i]
        else:
            status = df[i]
    return name, status