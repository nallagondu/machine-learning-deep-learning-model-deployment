import torch
import torch.nn as nn
from torch.nn import functional as F
import pandas as pd
import numpy as np

dataset = pd.read_csv('C:\Users\nallag\source\ML\ml_classification\storepurchasedata.csv')

dataset.describe()