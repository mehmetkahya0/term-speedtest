# Terminal Speedtest App

This is a terminal-based speed test application that logs the download and upload speed of your internet connection. The app uses the `speedtest-cli` library to measure the speeds and logs the results in a CSV file.

## Prerequisites

- Python 3.x
- `speedtest-cli` library
- `colorama` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mehmetkahya0/terminal-speedtest.git
    cd terminal-speedtest
    ```

2. Install the required libraries:
    ```sh
    pip install speedtest-cli colorama
    ```

## Usage

Run the application with the following command:
```sh
python main.py [--interval INTERVAL] [--log-file LOG_FILE]
```
