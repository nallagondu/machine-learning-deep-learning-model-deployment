import numpy as np
import pandas as pd
import mlflow
import mlflow.sklearn

mlflow.sklearn.autolog()

# mlflow set experiment
mlflow.tracking.set_tracking_uri("http://127.0.0.1:5000/")
mlflow.set_experiment(experiment_name="futurexskill mlflow demo 4")

with mlflow.start_run(run_name="new-run1-11") as run5:
    training_data = pd.read_csv('storepurchasedata.csv')
    print("loaded training data")
    
    print("Checking for NaN values in training data:")
    print(training_data.isnull().sum())  # Print the count of NaN values in each column
    training_data.describe()

    X = training_data.iloc[:, :-1].values
    y = training_data.iloc[:, -1].values

    # Handle missing and invalid values
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy='mean')
    X = imputer.fit_transform(X)

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.60, random_state=0)

    from sklearn.neighbors import KNeighborsClassifier
    classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)

    # Model training
    print("Training the classifier...")
    try:
        classifier.fit(X_train, y_train)
        print("Model trained successfully")
    except ValueError as e:
        print("Error during modeltrainig :", e)
        
    y_pred = classifier.predict(X_test)
    y_prob = classifier.predict_proba(X_test)[:, 1]

    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

    from sklearn.metrics import accuracy_score
    model_accuracy = accuracy_score(y_test, y_pred)
    print(model_accuracy)

    mlflow.set_tag("Classifier", "knn")
    mlflow.log_metric("accuracy", model_accuracy)
    
    # Log the confusion matrix (optional)
    #mlflow.log_confusion_matrix(y_test, y_pred)

    # Log the model
    #mlflow.sklearn.log_model(classifier, "model")
