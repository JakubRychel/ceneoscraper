#import bibliotek
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#wyświetlenie zawartości katalogu opinions_json
input_directory = "/opinions_json"
print(*os.listdir(input_directory))

#wczytanie identyfikatora produktu, którego opinie będą analizowane
product_id = input("Podaj identyfikator produktu: ")

opinions = pd.read_json(input_directory+"/"+product_id+".json")
opinions = opinions.set_index("opinion_id")

average_score = opinions.stars.mean().round(2)
pros = 

print(average_score)

