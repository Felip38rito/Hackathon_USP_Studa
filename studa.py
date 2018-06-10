import numpy as np
import pandas as pd


from sklearn.cluster import KMeans
import sklearn as sk

from sklearn.metrics import silhouette_score


### Cria colunas que nao estao na base de teste

def add_missing_dummy_columns(new_data, train_columns):
    missing_cols = set( train_columns ) - set( new_data.columns )
    for c in missing_cols:
        new_data[c] = 0
        
### Verifica se existe colunas na teste que nao pertencem a treino
### Caso existam ele retira
def fix_columns (new_data, train_columns):  
    add_missing_dummy_columns(new_data, train_columns)

    
    assert(set(train_columns) - set(new_data.columns) == set())

    extra_cols = set(new_data.columns) - set(train_columns)
    if extra_cols:
        print ("colunas extras na base teste", extra_cols)

    new_data = new_data[ train_columns ]
    return new_data


def Agrupamento(BASE_TREINO,BASE_CONSULTA, CURSO = 'MATEMATICA'):

    BASE_TREINO = BASE_TREINO.loc[(BASE_TREINO['CURSO'] == CURSO) ] 
    # BASE_TREINO = BASE_TREINO.drop(['CURSO','NOME','FACULDADE'],axis=1 )
    # BASE_CONSULTA = BASE_CONSULTA.drop(['CURSO','NOME','FACULDADE'],axis=1 )                  
    
    BASE_TREINO = BASE_TREINO.copy()
    names_to_dummies = ['LINGUA','FORMACAO']
    BASE_TREINO = pd.get_dummies(BASE_TREINO, columns=names_to_dummies)
    colunas =['SEMESTRE', 'IDADE', 'INTERCAMBIO', 'INICIACAO CIENTIFICA',
       'EXPERIENCIA _PROFISSIONAL_MESES', 'LINGUA_PT', 'LINGUA_PT_ENG',
       'LINGUA_PT_ENG_ES', 'FORMACAO_DOUTORADO', 'FORMACAO_GRADUACAO',
       'FORMACAO_MESTRANDO']
    
    
    
    BASE_CONSULTA2 = fix_columns (BASE_CONSULTA, colunas)
    
    BASE_TREINO = BASE_TREINO[['SEMESTRE', 'IDADE', 'INTERCAMBIO', 'INICIACAO CIENTIFICA',
       'EXPERIENCIA _PROFISSIONAL_MESES', 'LINGUA_PT', 'LINGUA_PT_ENG',
       'LINGUA_PT_ENG_ES', 'FORMACAO_DOUTORADO', 'FORMACAO_GRADUACAO',
       'FORMACAO_MESTRANDO']]
    

    km = KMeans(init='k-means++',  n_clusters=3, max_iter=15,random_state = 2345) 
    Y = km.fit_predict(BASE_TREINO)
    cluster_final =km.predict(BASE_CONSULTA2 )

    return cluster_final[0]




    