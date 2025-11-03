import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import os

SAVE_LOCATION = "static/images"
FIGURE_NAME = 'plot.png'

def plot_graph(result: int, gender:str, race_ethnicity:str, parental_level_of_education:str, lunch:str, test_preparation_course:str, reading_score:int, writing_score:int):
    df = pd.read_csv("notebook/data/stud.csv")

    two_colors = ["#206A6A", "#D96C3D"]
    three_colors = ['#206A6A', '#F7DC6F', "#D96C3D"]
    labels = ['Dataset Average','Dataset Average', 'Predicted']
    gender_total = df[df['gender'] == gender]['math_score'].count()
    gender_avg = (df[df['gender'] == gender]['math_score'].sum())/gender_total

    race_ethnicity_total = df[df['race_ethnicity'] == race_ethnicity]['math_score'].count()
    race_ethnicity_avg = (df[df['race_ethnicity'] == race_ethnicity]['math_score'].sum())/race_ethnicity_total

    parental_level_of_education_total = df[df['parental_level_of_education'] == parental_level_of_education]['math_score'].count()
    parental_level_of_education_avg = (df[df['parental_level_of_education'] == parental_level_of_education]['math_score'].sum())/parental_level_of_education_total

    lunch_total = df[df['lunch'] == lunch]['math_score'].count()
    lunch_avg = (df[df['lunch'] == lunch]['math_score'].sum())/lunch_total

    test_preparation_course_total = df[df['test_preparation_course'] == test_preparation_course]['math_score'].count()
    test_preparation_course_avg = (df[df['test_preparation_course'] == test_preparation_course]['math_score'].sum())/test_preparation_course_total
    
    reading_score_total = df[df['reading_score'] == reading_score]['math_score'].count()
    if reading_score_total==0:
        reading_score_total=1
    reading_score_avg = (df[df['reading_score'] == reading_score]['math_score'].sum())/reading_score_total
    
    writing_score_total = df[df['writing_score'] == writing_score]['math_score'].count()
    if writing_score_total==0:
        writing_score_total=1
    writing_score_avg = (df[df['writing_score'] == writing_score]['math_score'].sum())/writing_score_total

    plt.style.use('fivethirtyeight')
    fig, axs = plt.subplots(nrows=3, ncols=2)
    bars = axs[0,0].bar(['gender_avg', 'result'],[gender_avg, result], color=two_colors)
    axs[0,0].set_title('Gender', fontsize=12)
    axs[0,0].bar_label(bars, fmt='%d', padding=2, fontsize=8)
    
    bars = axs[0,1].bar(['race_ethnicity_avg', 'result'],[race_ethnicity_avg, result], color=two_colors)
    axs[0,1].set_title('Race/Ethnicity', fontsize=12)
    axs[0,1].bar_label(bars, fmt='%d', padding=2, fontsize=8)
    
    bars = axs[1,0].bar(['parental_level_of_education_avg', 'result'],[parental_level_of_education_avg, result], color=two_colors)
    axs[1,0].set_title('Parental Level of Education', fontsize=12)
    axs[1,0].bar_label(bars, fmt='%d', padding=2, fontsize=8)
    
    bars = axs[1,1].bar(['lunch_avg', 'result'],[lunch_avg, result], color=two_colors)
    axs[1,1].set_title('Lunch', fontsize=12)
    axs[1,1].bar_label(bars, fmt='%d', padding=2, fontsize=8)
    
    bars = axs[2,0].bar(['test_preparation_course_avg', 'result'],[test_preparation_course_avg, result], color=two_colors)
    axs[2,0].set_title('Test Preparation Course', fontsize=12)
    axs[2,0].bar_label(bars, fmt='%d', padding=2, fontsize=8)
    
    bars = axs[2,1].bar(['reading_score_avg', 'writing_score_avg', 'result'], [reading_score_avg, writing_score_avg, result], color=three_colors)
    axs[2,1].set_title('Reading-Writing Score', fontsize=12)
    axs[2,1].bar_label(bars, fmt='%d', padding=2, fontsize=8)
    
    axs = axs.flatten()
    for ax in axs:
        ax.set_xticklabels([])
        ax.tick_params(axis='y', which='major', labelsize=8)
        ax.yaxis.set_major_locator(plt.MaxNLocator(4))

    fig.legend(bars, labels, loc='upper left', fontsize=10, frameon=False)
    plt.subplots_adjust(wspace=0.05, hspace=0.1)

    plt.tight_layout(rect=[0, 0, 1, 0.90])
    
    figure_location = os.path.join(SAVE_LOCATION,FIGURE_NAME)
    plt.savefig(figure_location)
    plt.close()
    
    return FIGURE_NAME
