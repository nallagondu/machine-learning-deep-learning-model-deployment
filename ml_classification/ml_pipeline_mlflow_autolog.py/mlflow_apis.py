# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:58:47 2023

@author: nallag
"""

import mlflow 

mlflow.tracking.set_tracking_uri("http://127.0.0.1:5000")

print(mlflow.tracking.get_tracking_uri())

experiment = mlflow.get_experiment("633010643391764265")
print("Name: {}".format(experiment.name))