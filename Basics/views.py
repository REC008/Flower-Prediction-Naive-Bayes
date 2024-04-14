from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def Home(request):
    if request.method == "POST":
        data = request.POST
        sl = float(data.get('sl'))
        sw = float(data.get('sw'))
        pl = float(data.get('pl'))
        pw = float(data.get('pw'))

        path = "C:\\Users\\rohit\\Desktop\\Intern K Proj\\MLprog\\Flower_Prediction\\Basics\\Iris.csv"
        data = pd.read_csv(path)

        # Drop columns for inputs and outputs
        inputs = data.drop(['Id', 'Species'], axis=1)
        outputs = data.drop(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'], axis=1)

        # Split the data into training and testing sets
        x_train, x_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.2)

        # Create and train the KNeighborsClassifier model
        model = KNeighborsClassifier(n_neighbors=13)
        model.fit(x_train, y_train)

        # Predict the result for the input values
        result = model.predict([[sl, sw, pl, pw]])

        # Check if result is not empty
        if len(result) > 0:
            return render(request, "Home.html", context={'result': result.tolist()})

    return render(request, 'Home.html')
