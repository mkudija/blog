import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

def data_sleep(path):
    # read data
    sleep = pd.read_csv(path,
                        parse_dates=[1])
    sleep['DateTime'] = sleep['Time']
    sleep['Date'] = sleep['DateTime'].dt.date
    sleep['Time'] = sleep['DateTime'].dt.time

    # get bottom
    sleep['bottom'] = (sleep['Date']-min(sleep['Date'])).astype(str)
    sleep['bottom'] = (sleep['bottom'].str.split(' ').str.get(0)).astype(int)

    # get minutes
    sleep['minutes'] = sleep['Time'].astype(str).str.split(':').apply(lambda x: int(x[0]) * 60 + int(x[1]))

    return sleep


def data_nurse(path):
    # read data
    nurse = pd.read_csv(path,
                        parse_dates=[1])
    nurse['DateTime'] = nurse['Time']
    nurse['Date'] = nurse['DateTime'].dt.date
    nurse['Time'] = nurse['DateTime'].dt.time

    # get duration
    nurse['Total Duration'] = nurse['Left duration'] + nurse['Right duration']

    # get bottom
    nurse['bottom'] = (nurse['Date']-min(nurse['Date'])).astype(str)
    nurse['bottom'] = (nurse['bottom'].str.split(' ').str.get(0)).astype(int)

    # get minutes
    nurse['minutes'] = nurse['Time'].astype(str).str.split(':').apply(lambda x: int(x[0]) * 60 + int(x[1]))

    return nurse


def data_diaper(path):
    # read data
    diaper = pd.read_csv(path,
                        parse_dates=[1])
    diaper['DateTime'] = diaper['Time']
    diaper['Date'] = diaper['DateTime'].dt.date
    diaper['Time'] = diaper['DateTime'].dt.time
    
    # get bottom
    diaper['bottom'] = (diaper['Date']-min(diaper['Date'])).astype(str)
    diaper['bottom'] = (diaper['bottom'].str.split(' ').str.get(0)).astype(int)

    # get minutes
    diaper['minutes'] = diaper['Time'].astype(str).str.split(':').apply(lambda x: int(x[0]) * 60 + int(x[1]))

    return diaper


def data_story(path):
    # read data
    story = pd.read_csv(path,
                        parse_dates=[1])
    story = story[story['Other activity']=='Story Time']
    story['DateTime'] = story['Time']
    story['Date'] = story['DateTime'].dt.date
    story['Time'] = story['DateTime'].dt.time
    
    # get bottom
    story['bottom'] = (story['Date']-min(story['Date'])).astype(str)
    story['bottom'] = (story['bottom'].str.split(' ').str.get(0)).astype(int)

    # get minutes
    story['minutes'] = story['Time'].astype(str).str.split(':').apply(lambda x: int(x[0]) * 60 + int(x[1]))

    return story


def plot_sleep_radial(sleep):
    ax = plt.subplot(111, projection='polar')
    ax.set_facecolor('#F8B55A') # awake time background

    # turn axes off
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    # sleep time
    for row in range(sleep.shape[0]):
        duration = sleep.loc[sleep.index[row],'Duration(minutes)']
        minutes  = sleep.loc[sleep.index[row],'minutes']
        bottom   = sleep.loc[sleep.index[row],'bottom']
        width = duration / 60 / 24 * 2 * np.pi
        center = ( -(minutes+duration/2) / 60 / 24 * 2 * np.pi) - np.pi/2
        bars = ax.bar(center, 1, width=width, bottom=bottom, color='#225282')

    # hour marks
    x = np.linspace(0,np.pi*2,num=25)
    hr = ['6 pm','5 pm','4 pm','3 pm','2 pm','1 pm','12 pm',
          '11 am','10 am','9 am','8 am','7 am','6 am',
          '5 am','4 am','3 am','2 am','1 am','12 am',
          '11 pm','10 pm','9 pm','8 pm','7 pm','']
    for i in range(len(x)):
        plt.plot([0,x[i]],[0,bottom+1],'k:',lw=.5,alpha=.5)
        plt.text(x[i],bottom+2.5,hr[i],ha='center',va='center', color='grey', 
            fontsize=8, family='monospace')

    # annotation
    ax.annotate('Data collected with Baby Tracker app (v3.09)', xy=(0, 0),  
        xycoords='figure fraction', xytext=(0.0, -0.1), textcoords='axes fraction',
        horizontalalignment='left', verticalalignment='center', fontsize=6, color='grey')

    # legend
    legend_elements = [Line2D([0], [0], color='#F8B55A', lw=6, label='Awake'),
                       Line2D([0], [0], color='#225282', lw=6, label='Sleeping')]                       
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(.85, .06), fontsize=6)


    plt.title('Baby\'s Sleep Schedule', va='bottom')
    plt.ylim(ymax=bottom+1)
    plt.savefig('plot_sleep_radial.png', bbox_inches='tight', dpi=300)


def plot_all_radial(sleep, nurse, diaper, story):
    ax = plt.subplot(111, projection='polar')
    ax.set_facecolor('#F8B55A') # awake time background

    # turn axes off
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    # sleep time
    for row in range(sleep.shape[0]):
        duration = sleep.loc[sleep.index[row],'Duration(minutes)']
        minutes  = sleep.loc[sleep.index[row],'minutes']
        bottom   = sleep.loc[sleep.index[row],'bottom']
        width = duration / 60 / 24 * 2 * np.pi
        center = ( -(minutes+duration/2) / 60 / 24 * 2 * np.pi) - np.pi/2
        bars = ax.bar(center, 1, width=width, bottom=bottom, color='#225282')

    # nurse time
    for row in range(nurse.shape[0]):
        duration = nurse.loc[nurse.index[row],'Total Duration']
        minutes  = nurse.loc[nurse.index[row],'minutes']
        bottom   = nurse.loc[nurse.index[row],'bottom']
        width = duration / 60 / 24 * 2 * np.pi
        center = ( -(minutes+duration/2) / 60 / 24 * 2 * np.pi) - np.pi/2
        bars = ax.bar(center, 1, width=width, bottom=bottom, color='#f85a9d')

    # dirty diapers
    for row in range(diaper.shape[0]):
        bottom   = diaper.loc[diaper.index[row],'bottom']
        minutes  = diaper.loc[diaper.index[row],'minutes']
        center = ( -minutes / 60 / 24 * 2 * np.pi) - np.pi/2
        plt.plot(center, bottom+.5, marker='o', markersize=3, color="#825222", 
            markeredgecolor='white', markeredgewidth=.2)

    # story time
    for row in range(story.shape[0]):
        bottom   = story.loc[story.index[row],'bottom']
        minutes  = story.loc[story.index[row],'minutes']
        center = ( -minutes / 60 / 24 * 2 * np.pi) - np.pi/2
        plt.plot(center, bottom+.5, marker='o', markersize=3, color="#5aecf8", 
            markeredgecolor='white', markeredgewidth=.2)

    # hour marks
    x = np.linspace(0,np.pi*2,num=25)
    hr = ['6 pm','5 pm','4 pm','3 pm','2 pm','1 pm','12 pm',
          '11 am','10 am','9 am','8 am','7 am','6 am',
          '5 am','4 am','3 am','2 am','1 am','12 am',
          '11 pm','10 pm','9 pm','8 pm','7 pm','']
    for i in range(len(x)):
        plt.plot([0,x[i]],[0,bottom+1],'k:',lw=.5,alpha=.5)
        plt.text(x[i],bottom+2.5,hr[i],ha='center',va='center', color='grey', 
            fontsize=8, family='monospace')

    # annotation
    ax.annotate('Data collected with Baby Tracker app (v3.09)', xy=(0, 0),
        xycoords='figure fraction', xytext=(0.0, -0.1), textcoords='axes fraction',
        horizontalalignment='left', verticalalignment='center', fontsize=6, color='grey')

    # legend
    legend_elements = [Line2D([0], [0], color='#F8B55A', lw=6, label='Awake'),
                       Line2D([0], [0], color='#225282', lw=6, label='Sleeping'),
                       Line2D([0], [0], color='#f85a9d', lw=6, label='Nursing'),
                       Line2D([0], [0], marker='o', color='#825222', label='Diaper',
                              markeredgecolor='w', markersize=7),
                       Line2D([0], [0], marker='o', color='#5aecf8', label='Story Time',
                              markeredgecolor='w', markersize=7)]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(.85, .06), fontsize=6)

    plt.title('Baby\'s Schedule', va='bottom')
    plt.ylim(ymax=bottom+1)
    plt.savefig('plot_all_radial.png', bbox_inches='tight', dpi=300)


def plot_sleep(sleep):
    fig = plt.gcf()
    fig.clf()
    ax = plt.subplot(111)#, projection='polar')
    ax.set_facecolor('#A3D070') # awake time

    # turn axes off
    # ax.axes.get_xaxis().set_visible(False)
    # ax.axes.get_yaxis().set_visible(False)

    # sleep time
    ## https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.bar.html
    ## bars = ax.bar(center, thickness, width, bottom, color)
    for row in range(sleep.shape[0]):
        date     = sleep.loc[sleep.index[row],'Date']
        duration = sleep.loc[sleep.index[row],'Duration(minutes)']
        minutes  = sleep.loc[sleep.index[row],'minutes']
        bottom   = sleep.loc[sleep.index[row],'bottom']
        # width = duration / 60 / 24 * 2 * np.pi
        # center = ( -(minutes+duration/2) / 60 / 24 * 2 * np.pi) - np.pi/2

        # bars = ax.bar(center, 1, width=width, bottom=bottom, color='grey')
        # bars = ax.bar(date,duration,bottom, color='grey')
        bars = ax.bar(x=date, height=duration, width=1, bottom=minutes, color='grey')
        # bar(x, height, *, align='center', **kwargs)

    # bars = ax.bar(0-np.pi/4/2, 1, width=np.pi/4, bottom=10, color='#574D96')
    # bars = ax.bar(0, 1, width=np.pi, bottom=11, color='grey')
    # bars = ax.bar(np.pi, 1, width=np.pi/3, bottom=4, color='grey')
    # bars = ax.bar(np.pi, 1, width=np.pi/3, bottom=6, color='grey')


    # dirty diapers
    # plt.plot(0.13, 10.5, marker='o', markersize=5, color="red")
    # plt.plot(1.13, 1.5, marker='o', markersize=5, color="red")
    # plt.plot(0.23, 4.5, marker='o', markersize=5, color="red")
    # plt.plot(-0.13, 7.5, marker='o', markersize=5, color="red")

    # hour marks
    # x = np.linspace(0,np.pi*2,num=25)
    # hr = ['',5,4,3,2,1,'',11,10,9,8,7,'',5,4,3,2,1,'',11,10,9,8,7,'',5,4,3,2,1,'']
    # for i in range(len(x)):
    #     plt.plot([0,x[i]],[0,bottom+1],'k:',lw=.5,alpha=.5)
    #     plt.text(x[i],bottom+3,hr[i],ha='center',va='center', color='grey')

    # labels
    # maxh = bottom+3
    # plt.text(-np.pi/2,maxh,'12:00 AM', ha='center', va='center')
    # plt.text(-np.pi,maxh,'6:00 AM', ha='right', va='center')
    # plt.text(np.pi/2,maxh,'12:00 PM', ha='center', va='center')
    # plt.text(0,maxh,'6:00 PM', ha='left', va='center')


    plt.xticks(rotation=70)

    # title
    plt.title('Sleep Schedule')

    plt.savefig('plot_sleep.png', bbox_inches='tight', dpi=300)

sleep = data_sleep('Baby1_sleep.csv')
nurse = data_nurse('Baby1_nursing.csv')
diaper = data_diaper('Baby1_diaper.csv')
story = data_story('Baby1_other_activity.csv')

# print(nurse.head())
plot_sleep_radial(sleep)
plot_all_radial(sleep, nurse, diaper, story)
# plot_sleep(sleep)