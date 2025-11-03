import pickle
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData, PredictPipeline
from src.plot import plot_graph
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('predict.html')
    else:
        gender=request.form.get('gender')
        race_ethnicity=request.form.get('ethnicity')
        parental_level_of_education=request.form.get('parental_level_of_education')
        lunch=request.form.get('lunch')
        test_preparation_course=request.form.get('test_preparation_course')
        reading_score=float(request.form.get('reading_score'))
        writing_score=float(request.form.get('writing_score'))
        data = CustomData(gender=gender,
                          race_ethnicity=race_ethnicity,
                          parental_level_of_education=parental_level_of_education,
                          lunch=lunch,
                          test_preparation_course=test_preparation_course,
                          reading_score=reading_score,
                          writing_score=writing_score)
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        img_loc = plot_graph(results[0], gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score)
        return render_template('predict.html', results = results[0], img_loc=img_loc)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)