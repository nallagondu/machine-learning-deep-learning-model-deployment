import random
import pandas as pd
from faker import Faker

# Create a Faker object to generate random data
fake = Faker()

# Create lists to store the generated logs
timestamps = []
log_levels = []
server_ids = []
log_messages = []

# Generate 100 random server logs
for _ in range(100):
    timestamps.append(fake.date_time_this_year())
    log_levels.append(random.choice(["INFO", "WARNING", "ERROR"]))
    server_ids.append(fake.hostname())
    log_messages.append(fake.catch_phrase())

# Create a DataFrame to store the logs
log_data = pd.DataFrame({
    'timestamp': timestamps,
    'log_level': log_levels,
    'server_id': server_ids,
    'log_message': log_messages
})

# Save the DataFrame to a CSV file
log_data.to_csv("server_logs.csv", index=False)
