import pandas as pd
import numpy as np
import os, json, requests
os.chdir(os.path.dirname(os.path.realpath(__file__)));
print os.getcwd();
frame = pd.read_csv("Cars93.csv");