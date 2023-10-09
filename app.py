from flask import Flask, request, render_template
import pandas as pd
import pickle
import plotly.graph_objects as go

app = Flask(__name__)

model = pickle.load(open('arima_model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_values = request.form['months']
        input_values = [int(value.strip()) for value in input_values.split(',')]
    except ValueError:
        return render_template('index.html', prediction_text='Invalid input. Please enter valid numbers separated by commas.')

    all_predictions = []
    for value in input_values:
        predictions = model.get_forecast(steps=value).predicted_mean
        predictions.index = predictions.index.strftime('%Y-%m-%d')
        all_predictions.append(predictions)
    
    # Create a Plotly line chart for the predictions
    fig = go.Figure()
    for i, predictions in enumerate(all_predictions):
        fig.add_trace(go.Scatter(x=predictions.index, y=predictions, mode='lines+markers', name=f'Input {input_values[i]}'))

    fig.update_layout(title='Monthly Predictions for Scanned Receipts', xaxis_title='Month', yaxis_title='Predicted Values')

    # Convert the Plotly chart to HTML and pass it to the template
    plotly_chart = fig.to_html(full_html=False)
    return render_template('index.html', prediction_text=f'Monthly predictions for Number of months: {input_values}', plotly_chart=plotly_chart)

if __name__ == '__main__':
    app.run(debug=True)
