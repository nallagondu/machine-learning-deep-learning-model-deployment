import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
message = "This is a sample log message."
tokens = word_tokenize(message.lower())
# Step 1: Load and preprocess the server logs data
url = 'https://raw.githubusercontent.com/nallagondu/machine-learning-deep-learning-model-deployment/main/ml_classification/server_logs.csv'
data = pd.read_csv(url)

# Assuming the target column for server performance is named 'performance'
X = data['log_message']
y = data['log_level']

# Step 2: Extract features using TF-IDF vectorization
vectorizer = TfidfVectorizer(min_df=2, stop_words='english', lowercase=True)
X = vectorizer.fit_transform(X)

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train a RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the model on the testing data
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Step 6: Use the trained model to predict server performance for new log messages
# Assuming 'new_log_messages' is a list of new log messages
new_log_messages = [
    "CPU usage is spiking",
    "Memory consumption is high",
    "Disk read/write errors detected",
    "Network latency is increasing"
]

# Preprocess the new log messages
preprocessed_new_log_messages = []
for message in new_log_messages:
    tokens = word_tokenize(message.lower())
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    preprocessed_message = " ".join(filtered_tokens)
    preprocessed_new_log_messages.append(preprocessed_message)

# Convert the preprocessed new log messages into numerical representations using the same vectorizer
X_new = vectorizer.transform(preprocessed_new_log_messages)

# Use the trained model to predict server performance for the new log messages
predictions = model.predict(X_new)

print("Predicted server performance for new log messages:")
for i, message in enumerate(new_log_messages):
    print(f"Log message: {message} - Predicted Performance: {predictions[i]}")


