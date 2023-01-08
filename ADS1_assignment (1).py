import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('WorldHappiness_Corruption_2015_2020.csv')

norway=data[data['Country']=='Norway']
uk=data[data['Country']=='United Kingdom']
usa=data[data['Country']=='United States']
germany=data[data['Country']=='Germany']


def line_plot(x,y):
    '''
    The line_plot function takes input as x axis labels and y axis labels and plots the line graphs.
    x: string
        labels on x axis
    y: string
        labels on y axis
    '''
    plt.plot(germany[x],germany[y],c='red',label='Germany')
    plt.plot(uk[x],uk[y],c='blue',label='United Kingdom')
    plt.plot(usa[x],usa[y],c='orange',label='USA')
    plt.plot(norway[x],norway[y],c='black',label='Norway')
    plt.title(y+' of countries')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.legend()
    plt.show()

line_plot('Year', 'happiness_score')


def violinplots(data,labels):
    '''
    The Funtion takes data and labels as input to generate the violinplot.
    data: N array of numbers
        data to plot on the graphs
    labels: Array
        data to plot on x axis
    '''
    plt.violinplot(data,labels)
    plt.title('Government Trust of the world in years')
    plt.xlabel('Years')
    plt.ylabel('Government Trust')
    plt.show()

years=[2015,2016,2017,2018,2019,2020]
govt_trust= [data['government_trust'][data['Year']==2015],data['government_trust'][data['Year']==2016],data['government_trust'][data['Year']==2017],data['government_trust'][data['Year']==2018],data['government_trust'][data['Year']==2019],data['government_trust'][data['Year']==2020]]
violinplots(govt_trust, years)

#pie chart
freedom=data['freedom'].groupby(data['continent']).mean()
plt.pie(freedom,labels=freedom.index,autopct='%1.1f%%',startangle=70)
plt.title('Freedom of speech in each continent')
plt.show()
