import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///Farma_lineSQLITE.db')
connection = engine.connect()

class Farmaco:

    def __init__(self, codice: str, nome: str, prezzo: str, ricetta: str, preparato_galenico: str, scheda_tecnica=None):
        self.codice = codice
        self.nome = nome
        self.prezzo = prezzo
        self.ricetta = ricetta
        self.preparato_galenico = preparato_galenico
        # self.scheda_tecnica = scheda_tecnica opzionale

    def associazioneDB(self) -> None:
            farmaco= pd.DataFrame (
                    columns=['nome', 'ricetta', 'preparato_galenico', 'prezzo', 'codice'],
                    data= [self.nome,self.ricetta,self.preparato_galenico,self.prezzo, self.codice]
            )
            farmaco.to_sql('FarmaciMagazzino', connection, if_exists='append')
            return None

#non si puo fare tutto in init