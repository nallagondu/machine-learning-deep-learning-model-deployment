import house_price_predictor

model_object = house_price_predictor.HousePricePredictor()

model_object.predict_price(5)


import os
command = 'python house_price_predictor_2.py --distance 1'
os.system(command)

