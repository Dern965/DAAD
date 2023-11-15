import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

st.write("""
# Practica 4
## Visualización de datos
""")

df = pd.read_csv('C:\Users\dern9\Desktop\DAAD\Practica 4\SuperStore_Sales_Dataset.csv')
