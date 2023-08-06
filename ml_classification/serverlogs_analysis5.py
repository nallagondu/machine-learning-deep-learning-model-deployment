import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read the server logs from the text file
with open("server_logs.txt", "r") as file:
    server_logs = file.readlines()

# Create a list to store the log messages and their corresponding labels (log_level)
log_messages = []
log_labels = []

# Regular expression to extract log level and log message from each log entry
log_pattern = re.compile(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] \[(\w+)\] (.+)")

# Process each log entry and extract log level and message
for log_entry in server_logs:
    match = log_pattern.match(log_entry)
    if match:
        timestamp, log_level, server_id, log_message = match.groups()
        log_messages.append(log_message)
        log_labels.append(log_level)

# Convert log messages into a numerical representation using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(log_messages)

# Create a DataFrame to store the log data
log_data = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# Convert log levels into numerical labels
log_data['log_level'] = pd.Categorical(log_labels).codes

# Split the data into features (log messages) and labels (log levels)
X = log_data.drop(columns='log_level')
y = log_data['log_level']

# Train a simple Naive Bayes classifier for log level classification
classifier = MultinomialNB()
classifier.fit(X, y)

# Predict the log level for new log messages (RCA)
new_log_messages = [
    "Server is running out of memory",
    "High CPU utilization detected",
    "Disk space full"
]

# Convert the new log messages into a numerical representation
X_new = vectorizer.transform(new_log_messages)

# Predict the log level for the new log messages
predicted_log_levels = classifier.predict(X_new)

# Convert numerical labels back to log level names
predicted_log_level_names = pd.Categorical.from_codes(predicted_log_levels, categories=log_data['log_level'].cat.categories)

# Print the RCA for each new log message
for i, log_message in enumerate(new_log_messages):
    print(f"Log Message: {log_message} | RCA: {predicted_log_level_names[i]}")
