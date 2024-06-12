import streamlit as st 
import streamlit_authenticator as stauth
import os
import pickle 
from pathlib import Path
import joblib

names = ['Felix Kwemoi',"Don felo"]
passwords = ["#CoyG12","123"]
username = ["DonFelo10",'lofe']


# Hash the passwords
hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent/"hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
    




    
    
            

