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

2. Install the necessary dependencies:

pip install mutagen

### Usage

1. Edit the wav_duration_summary.py file and specify the main_folder path where your audio files are located and an output_csv file for the results.

Example:

```python
main_folder = '/path/to/your/audio/folder'
output_csv = 'wav_file_durations.csv'

2. Run the script:

```bash
python wav_duration_summary.py

3. The script will print the number of .wav files found and the total duration in both seconds and formatted time.

#### Example Output

```bash
Process completed. Found 340 audio files with a total duration of 906397.000000 seconds.
Total duration: 251 hours, 46 minutes, and 37.00 seconds.
Detailed durations saved to wav_file_durations.csv

#### CSV Output
The CSV file will contain two columns: the file path and the duration in seconds for each .wav file.

#### Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any improvements or bugs.
