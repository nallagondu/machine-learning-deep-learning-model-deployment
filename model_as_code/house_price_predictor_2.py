import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--distance",help ="distance to city center")
args = parser.parse_args()

class HousePricePredictor:
    
    def __init__(self):
        print("Prediction started")
        self.distance_to_city_center = float(args.distance)
    
    def predict_price(self):
        price = 610710.0319872361 - 72635.89282856 * self.distance_to_city_center
        print("House price is >>> "+str(price))
        with open("model_output.txt", "w") as f:
            f.write(str(price))
        
if __name__ == "__main__":
    model_instance = HousePricePredictor()
    model_instance.predict_price(2)