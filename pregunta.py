"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    # Convertir textos en minuscula

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df=df.dropna()
    df.columns.values

    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['barrio'] = df['barrio'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.lower()

    # idea de negocio
    df['idea_negocio']=df['idea_negocio'].str.replace("-","_")
    df['idea_negocio']=df['idea_negocio'].str.replace("_"," ")
    df['idea_negocio']=df['idea_negocio'].str.strip()

    # Barrio
    df['barrio']=df['barrio'].str.replace("-","_")
    df['barrio']=df['barrio'].str.replace("_"," ")
    df['barrio']=df['barrio'].str.replace(".","")
    df['barrio']=df['barrio'].str.replace("bel¿n","belen")
    df['barrio']=df['barrio'].str.replace("antonio nari¿o","antonio nariño")
    df['barrio']=df['barrio'].str.strip()






    return df
