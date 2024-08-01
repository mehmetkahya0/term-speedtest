# Terminal Speedtest app. Logs the download and upload speed of the user's internet connection. 
# The app uses the speedtest-cli library to get the download and upload speed.

import speedtest
import time
import datetime
import csv
import os
import argparse
from colorama import Fore, Style

class SpeedTest:
    def __init__(self, log_file):
        self.st = speedtest.Speedtest()
        self.download_speed = 0
        self.upload_speed = 0
        self.log_file = log_file

    def get_speed(self):
        self.st.get_best_server()
        self.download_speed = self.st.download() / 1024 / 1024
        self.upload_speed = self.st.upload() / 1024 / 1024

    def log_speed(self):
        with open(self.log_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.datetime.now(), self.download_speed, self.upload_speed])

    def print_speed(self):
        print(f"{Fore.GREEN}Download Speed: {self.download_speed:.2f} Mbps")
        print(f"Upload Speed: {self.upload_speed:.2f} Mbps{Style.RESET_ALL}")
        
    def run(self):
        self.get_speed()
        self.log_speed()
        self.print_speed()
        
def main():
    parser = argparse.ArgumentParser(description="Terminal Speedtest app")
    parser.add_argument('--interval', type=int, default=10, help='Interval between speed tests in seconds')
    parser.add_argument('--log-file', type=str, default='log/speedtest_log.csv', help='Path to the log file')
    args = parser.parse_args()

    speed_test = SpeedTest(args.log_file)
    while True:
        speed_test.run()
        time.sleep(args.interval)
    
if __name__ == "__main__":
    main()