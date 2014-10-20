import pandas as pd
import numpy as np
import os, json, requests
os.chdir(os.path.dirname(os.path.realpath(__file__)));
print os.getcwd();
frame = pd.read_csv("Cars93.csv");
mapping = {'rotary':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8'};
frame.Cylinders = frame['Cylinders'].map(mapping);
mapping = {'non-USA':'0','USA':'1'}
frame['Origin'] = frame['Origin'].map(mapping);
mapping = {'Yes':'0','No':'1'}
frame['Man.trans.avail'] = frame['Man.trans.avail'].map(mapping);

print frame.describe()