import random
import time

log_files = ['/var/log/syslog', '/var/log/messages', '/var/log/kern.log', '/var/log/dmesg', '/var/log/auth.log',
             '/var/log/apache2/access.log', '/var/log/nginx/access.log', '/var/log/mysql/error.log',
             '/var/log/postgresql/postgresql-<version>-main.log', '/var/log/mail.log', '/var/log/secure']

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_random_timestamp():
    return time.strftime('%b %d %H:%M:%S', time.localtime(random.randint(0, int(time.time()))))

def generate_random_log_entry():
    log_file = random.choice(log_files)
    timestamp = generate_random_timestamp()
    log_level = random.choice(['INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    message = f"Sample log entry for {log_file}: Random event occurred with level {log_level}"
    return f"{timestamp} server1 {log_level}: {message}"

num_logs = 1000

with open("sample_logs.txt", "w") as file:
    for _ in range(num_logs):
        log_entry = generate_random_log_entry()
        file.write(log_entry + "\n")

