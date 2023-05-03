from flask import Flask, request, render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline



application= Flask(__name__)

app=application

@app.route('/') # this is route to home page home page is bydeafuls a get request
def home_page():
    return render_template('index.html')


@app.route('/predict', methods= ['GET', 'POST'])

def predict_datapoint():    #this function is called in webpage of form.html to take the input from page
    if request.method=='GET':
        return render_template ('form.html')

    else: #after putting the submit button in html wepage of form.html the belowe data point have to be created from prdiction pipeline code

        data=CustomData(
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('results.html',final_result=results)



if __name__=='__main__':
    app.run(host= '0.0.0.0', debug =True)

