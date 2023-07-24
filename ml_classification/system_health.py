import csv
import subprocess
import psutil
import socket
import datetime
import glob

def get_logs_info():
    log_files = glob.glob('/var/log/*.log')  # Path to log files directory, modify as per your system

    logs_info = []

    for file in log_files:
        with open(file, 'r') as log_file:
            logs = log_file.readlines()

        for log in logs:
            if 'error' in log.lower() or 'alert' in log.lower() or 'warning' in log.lower():
                logs_info.append({'Log File': file, 'Log Message': log.strip()})

    return logs_info

def get_system_info():
    # Server information
    hostname = socket.gethostname()
    memory = psutil.virtual_memory().total
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())

    # Disk information
    disk_usage = psutil.disk_usage('/')
    mount_points = [partition.mountpoint for partition in psutil.disk_partitions()]

    # Network information
    network_status = 'Connected' if subprocess.call("ping -c 1 google.com", shell=True) == 0 else 'Disconnected'

    # Port and firewall information
    open_ports = [22, 80, 443]  # Example ports to check
    open_ports_status = []
    firewall_status = 'Active' if subprocess.call("ufw status | grep 'Status: active'", shell=True) == 0 else 'Inactive'

    for port in open_ports:
        port_status = 'Open' if subprocess.call("nc -z -v -w5 {hostname} {port}".format(hostname=hostname, port=port), shell=True) == 0 else 'Closed'
        open_ports_status.append({'Port': port, 'Status': port_status})

    # Kernel and mode information
    kernel_version = subprocess.check_output("uname -r", shell=True).decode().strip()
    mode = subprocess.check_output("uname -m", shell=True).decode().strip()

    return {
        'Hostname': hostname,
        'Memory': memory,
        'Uptime': uptime,
        'Disk Usage': disk_usage,
        'Mount Points': mount_points,
        'Network Status': network_status,
        'Open Ports': open_ports_status,
        'Firewall Status': firewall_status,
        'Kernel Version': kernel_version,
        'Mode': mode
    }

def write_to_csv(data):
    fieldnames = data[0].keys()

    with open('server_monitoring.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    logs_info = get_logs_info()
    server_info = get_system_info()

    combined_info = [server_info.update(log) for log in logs_info]

    write_to_csv([server_info])
