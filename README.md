# wav-duration-summarizer
This script recursively scans a folder structure to count `.wav` audio files and sum their total duration. It outputs the results in both seconds and a formatted time (hours, minutes, and seconds), saving the details to a CSV file.

## Features

- Counts the number of `.wav` files in a specified folder and all its subfolders.
- Calculates the total duration of all `.wav` files, including a breakdown by file.
- Outputs the total duration in both seconds and formatted time (hh:mm:ss).
- Handles hidden "phantom files" created by macOS.
- Logs individual file durations to a CSV file for easy reference.

## Prerequisites

- Python 3.x
- `mutagen` library for audio file metadata reading

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/wav-duration-summarizer.git
