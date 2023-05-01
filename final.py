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

def figure2():
    cases_df = get_cases()
    twenty = []
    twentyone = []
    twentytwo = []
    twentythree = []
    for date in cases_df['Date']:
        seperate = date.split()
        year = seperate[2]
        cases = cases_df.loc[cases_df['Date'] == date, 'Weekly Cases'].iloc[0]
        #print(cases)
        if year == '2020':
            twenty.append(cases)
        elif year == '2021':
            twentyone.append(cases)
        elif year == '2022':
            twentytwo.append(cases)
        elif year == '2023':
            twentythree.append(cases)
    
    fig, ax = matplotlib.pyplot.subplots(figsize=(12,7))
    ax.boxplot([twenty, twentyone, twentytwo, twentythree])
    ax.set_xticklabels(['2020', '2021', '2022', '2023'])
    matplotlib.pyplot.ylabel("Number of Cases (In Millions)", fontsize = 12)
    matplotlib.pyplot.xlabel("Years", fontsize = 12)
    matplotlib.pyplot.title("Weekly COVID-19 Cases by Year", fontsize = 18)
    matplotlib.pyplot.show()

def figure3(): 
    cases_df = get_cases()
    cases_df['Date'] = pd.to_datetime(cases_df['Date'], format='%b %d %Y')
    mask = (cases_df['Date'] >= pd.Timestamp('2020-03-01')) & (cases_df['Date'] <= pd.Timestamp('2021-03-01'))
    filtered_cases_df = cases_df.loc[mask]
    dates_list = filtered_cases_df['Date'].tolist()
    cases_list = filtered_cases_df['Weekly Cases'].tolist()

    df = pd.DataFrame({'date': dates_list, 'cases': cases_list})
    df['date'] = pd.to_datetime(df['date'], format='%b %d %Y')
    dates = df['date'].values
    cases = df['cases'].values
    slope, intercept = np.polyfit(matplotlib.dates.date2num(dates), cases, 1)
    line = slope * matplotlib.dates.date2num(dates) + intercept
    fig, ax = matplotlib.pyplot.subplots(figsize=(12,7))
    ax.set_ylim([(cases.min()), (cases.max()) + 100000])
    ax.scatter(dates, cases)
    ax.plot(dates, matplotlib.dates.num2date(line), color='red')
    matplotlib.pyplot.ylabel("Weekly Cases(In Hundred Thousandths)", fontsize = 12)
    matplotlib.pyplot.xlabel("Months", fontsize = 12)
    matplotlib.pyplot.title("Weekly COVID-19 Cases From Mar 2020 to Mar 2021", fontsize = 18)
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%b %Y'))
    matplotlib.pyplot.show()


figure1()
figure2()
figure3()