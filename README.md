# Flashy French Vocabulary Trainer

## Overview
The **Flashy French Vocabulary Trainer** is a Python application built using the Tkinter library. It is designed to help you learn and practice French vocabulary words. The program presents you with French words, and you have to guess their English translations. You can mark your answers as correct or incorrect and continue learning until you have mastered all the words.

## Features
- Presents French words along with their English translations.
- Allows you to mark whether your answer is correct or incorrect.
- Automatically saves your progress and loads it when you start the program again.
- Provides a "Reset" button to start over and learn the words again.

## Requirements
- Python 3.x
- Tkinter library
- pandas library

## Getting Started
1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries if you don't have them already:
   ```
   pip install -r requirements.txt
   ```
3. Clone or download this repository to your local machine.

## Usage
1. Open your terminal (command prompt) and navigate to the directory where the script is located.
2. Run the following command to start the Flashy French Vocabulary Trainer:
   ```
   python flashy-vocabulary-trainer.py
   ```
3. The application window will appear with a French word and its translation in English.
4. If you know the correct translation, click the **"Correct"** button.
5. If you don't know or want to skip the word, click the **"Wrong"** button.
6. The application will save your progress automatically, so you can close it and come back later to continue learning.
7. If you have learned all the words, the application will display a message informing you of your accomplishment. You can reset the learning process by clicking the **"Reset"** button.

## Data
The application uses two CSV files to store data:
- **french_words.csv**: This file contains the French words and their English translations initially.
- **words_to_learn.csv**: This file is used to keep track of the words you are currently learning. As you mark words as correct, they will be removed from this file.

If you want to add more words to learn or start over with new words, you can modify the **french_words.csv** file.

## Customization
You can customize the appearance of the application by replacing the image files located in the **images** directory. Make sure the new image files have the same names as the original ones.

## Acknowledgments
This project is inspired by the need to practice any language vocabulary effectively. It is a simple and fun way to learn new words and improve language skills.

## Disclaimer
This program uses a random selection of words from the provided data files. While the application is designed to be helpful for learning, it may not cover all possible translations or contexts of the words. It is intended for educational purposes and should not be used as a comprehensive language learning tool.

## About the Developer
This project was created as part of a learning experience.

Happy learning! 🇫🇷📚