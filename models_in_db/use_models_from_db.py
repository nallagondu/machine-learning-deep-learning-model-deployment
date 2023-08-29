# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:02:01 2023

@author: nallag
"""
import psycopg2
import pickle

connection = psycopg2.connect(user='postgres',
                              password='mypassword',
                              host='localhost',
                              database='postgres')

cursor = connection.cursor()

select_query = "select * from modelstore.futurex_model_catalog"
models =cursor.execute(select_query)
models = cursor.fetchall()
models

classifier_from_db = pickle.loads(models[1][2])
scaler_from_db = pickle.loads(models[1][2])

new_pred = classifier_from_db.predict(scaler_from_db.transform(np.array([[30,20000]])))

new_pred_proba = classifier_from_db.predict_proba(scaler_from_db.transform(np.array([[40,80000]])))[:,1]
print(new_pred)
print(new_pred_proba)