#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:19:26 2024

@author: Mario Rollo (Umeå University)
"""

import os
from mutagen.wave import WAVE
import csv

# Function to get the duration of a wav file using mutagen (metadata)
def get_wav_metadata_duration(file_path):
    try:
        audio = WAVE(file_path)
        duration = audio.info.length
        return duration
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0.0

# Function to convert seconds into hours, minutes, and seconds
def seconds_to_hms(total_seconds):
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = total_seconds % 60
    return hours, minutes, seconds

# Main function to traverse folders, count files, and log durations
def process_audio_files(main_folder, output_csv):
    if not os.path.exists(main_folder):
        print(f"Main folder '{main_folder}' does not exist.")
        return

    total_files = 0
    total_duration = 0.0

    # Open CSV for detailed logging of each file's duration
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['File Path', 'Duration (seconds)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for root, dirs, files in os.walk(main_folder):
            wav_files = [f for f in files if f.lower().endswith('.wav') and not f.startswith('._')]

            for wav_file in wav_files:
                file_path = os.path.join(root, wav_file)
                duration = get_wav_metadata_duration(file_path)
                total_duration += duration
                total_files += 1

                # Log each file and its duration
                writer.writerow({'File Path': file_path, 'Duration (seconds)': f"{duration:.6f}"})
                print(f"File: {wav_file}, Duration: {duration:.6f} seconds")

    # Convert total duration from seconds to hours, minutes, and seconds
    hours, minutes, seconds = seconds_to_hms(total_duration)

    print(f"\nProcess completed. Found {total_files} audio files with a total duration of {total_duration:.6f} seconds.")
    print(f"Total duration: {hours} hours, {minutes} minutes, and {seconds:.2f} seconds.")
    print(f"Detailed durations saved to {output_csv}")

# Specify the main folder and output CSV file
main_folder = 'path/to/main/folder'  # Replace with your main folder path
output_csv = 'detailed_file_durations_mutagen.csv'

# Call the function to process audio files and save the results
process_audio_files(main_folder, output_csv)
