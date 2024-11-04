import streamlit as st
import numpy as np
import datetime
import pickle
import gdown
import time
gdown.download(f"https://drive.google.com/uc?id={st.secrets['LABELS']['id']}", f'labels.pkl', quiet=False)


# Load and print the list
with open('labels.pkl', 'rb') as file:
    labels = pickle.load(file)

print(labels[P_emaildomain])