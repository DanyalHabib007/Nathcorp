from flask import Flask, render_template, request
from main import TripCrew

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        origin = request.form['origin']
        cities = request.form['destination']
        date_range = f"{request.form['start_date']} to {request.form['end_date']}"
        interests = request.form['hobbies']

        # Here you can call the TripCrew class with the gathered data
        trip_crew = TripCrew(origin, cities, date_range, interests)
        result = trip_crew.run()

        return render_template('result.html', result=result)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
