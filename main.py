### PYTHON IMPLEMENTATION ON FLASH 
## FLASK APPLICATION 
# WHAT IS FLASK?
# Web Application Development Framework 
# Web application is an application which you call over any network or any internet connection.
# So that it can be called from any where in the world and Flask will help us to create # the web application development framework.

#ROUTE

# So we will have different route.Route will help that control will go where.
# With the help of route we can use different functionalites into one single python program.
# Route help or enables the pyton application to do multiple jobs based on the routes provided.
# This is provided along with the URL.

# In this project we will be using three different routes.
# Blank: homepage
# Predict: for prediction 
# Train: while training 


from flask import Flask, request, render_template
from flask import Response
import os
from flask_cors import CORS, cross_origin
from prediction_Validation_Insertion import pred_validation
from trainingModel import trainModel
from training_Validation_Insertion import train_validation
import flask_monitoringdashboard as dashboard
from predictFromModel import prediction

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
#dashboard.bind(app)
CORS(app)


@app.route("/", methods = ['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRouteClient():
    try:
        if request.json is not None:
            path = request.json['filepath']

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path = pred.predictionFromModel()
            return Response("Prediction File created at %s!!!" % path)
        elif request.form is not None:
            path = request.form['filepath']

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path = pred.predictionFromModel()
            return Response("Prediction File created at %s!!!" % path)

    except ValueError:
        return Response("Error Occurred! %s" %ValueError)
    except KeyError:
        return Response("Error Occurred! %s" %KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" %e)




@app.route("/train", methods = ['POST'])
@cross_origin()
def trainRouteClient():

    try:
        if request.json['filepath'] is not None:
            # VALIDATION
            # Data transformation
            # Column name and file name validation etc.
            # Then inserting the data into the database and from there we export the data to csv file.
            # We will be creating class for valiation and training 
            path = request.json['filepath']
            train_valObj = train_validation(path) #object initialization ( created an object of train validation class)

            train_valObj.train_validation()#calling the training_validation function

            # MODEL TRAINING 
            trainModelObj = trainModel() #object initialization # trainModel is a class
            trainModelObj.trainingModel() #training the model for the files in the table # trainingModel is a method from the class trainModel



    except ValueError:

        return Response("Error Occurred! %s" % ValueError)

    except KeyError:

        return Response("Error Occurred! %s" % KeyError)

    except Exception as e:

        return Response("Error Occurred! %s" % e)
    return Response("Training successfull!!")

port = int(os.getenv("PORT",5001))
if __name__ == "__main__":
    app.run(port=port,debug=True)