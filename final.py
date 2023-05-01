'''
Varun Neti 
Apr 24 2023
ISTA 131 Final Project 
Kapua Loane
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot
import matplotlib.dates
import datetime as dt 

def get_cases():
    cases_df = pd.read_csv("data_table_united_states.csv",skiprows = 2, header = 0)
    #cases_df['Date'] = pd.to_datetime(cases_df['Date'])
    del cases_df["Geography"]
    del cases_df["New Historic Cases"]
    return cases_df
    #print(cases_df)

def figure1():
    cases_df = get_cases()
    cases_df['Date'] = pd.to_datetime(cases_df['Date'])
    fig, ax = matplotlib.pyplot.subplots(figsize=(12,7))
    ax.plot(cases_df['Date'], cases_df['Weekly Cases'], color='red', linewidth = 4)
    ax.set_ylim(0, (cases_df['Weekly Cases'].max() + 500000))
    matplotlib.pyplot.xlabel("Dates", fontsize = 12)
    matplotlib.pyplot.ylabel("Number of Cases (In Millions)", fontsize = 12)
    matplotlib.pyplot.title("Number of COVID-19 Cases Since Jan 29, 2020", fontsize = 18)
    matplotlib.pyplot.show()



figure1()