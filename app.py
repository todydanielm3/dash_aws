# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#df = pd.read_excel("../dados_igesdf/07.06.2022.xlsx")
#df = pd.read_excel("../dados_igesdf/base_2020_2022.xlsx")

df = pd.read_excel("07.06.2022.xlsx")


#CRIANDO O GRAFICO COM BASE NA PLANILHA
fig = px.bar(df, x="EMPRESA", y="TOTAL", color="TIPO", text_auto=True)
#fig = px.bar(df, x="EMPRESA", y="TOTAL", color="TIPO", barmode="group")
#fig = px.pie(df,values='TOTAL', names='EMPRESA', title='Junho 2022')

app.layout = html.Div(children=[
    html.H1(children='Titulo: Base de extração de dados Boletim IGESDF '),
    html.H2(children='Data Inicial: 07/06/2022'),
    html.H2(children='Data Final: 07/06/2022'),
    html.Div(children='''
       Mês de Março'''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=666, debug=True)

