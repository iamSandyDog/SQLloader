import pandas as pd
import plotly.express as px
from src.repository.BigKoopRepository import BigKoopRepository

class ReportCommand:
    def __init__(self, repository: BigKoopRepository):
        self.__repo = repository

    def run(self):
        print('Report')
        data = self.__repo.dataSelector()
        df = pd.DataFrame(data)

        df['delivery_date'] = pd.to_datetime(df['delivery_date'])
        df['year'] = df['delivery_date'].dt.strftime('%Y').sort_values()

        fig1 = px.treemap(df, path=['material_group', 'region', 'material_name', 'warehouse'], values='amount',
                          color='material_name', hover_data=['year'], title='Общее')

        fig1.show()

