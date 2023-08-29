import tensorflow as tf
import numpy as np

# Generate synthetic log data (example)
num_samples = 1000
num_features = 10
normal_data = np.random.normal(0, 1, size=(num_samples, num_features))

# Create a TensorFlow model (autoencoder for anomaly detection)
input_layer = tf.keras.layers.Input(shape=(num_features,))
encoder_layer = tf.keras.layers.Dense(5, activation='relu')(input_layer)
decoder_layer = tf.keras.layers.Dense(num_features, activation='linear')(encoder_layer)
autoencoder = tf.keras.models.Model(input_layer, decoder_layer)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Train the model on normal log data
autoencoder.fit(normal_data, normal_data, epochs=50, batch_size=32, shuffle=True, validation_split=0.2)

# Generate anomaly data (example)
anomaly_data = np.random.normal(10, 3, size=(50, num_features))

# Predict on anomaly data
predictions = autoencoder.predict(anomaly_data)
losses = np.mean(np.square(anomaly_data - predictions), axis=1)

# Set a threshold for anomaly detection
threshold = 1.5

# Identify anomalies
anomalies = np.where(losses > threshold)[0]

# Print the index of anomalous data points
print("Anomalous data points:", anomalies)
