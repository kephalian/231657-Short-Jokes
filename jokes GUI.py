
import pandas as pd
import numpy as np
import PySimpleGUI as sg
sg.theme("purple1")
def retrieve_jokes(file_path, num_samples=2):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Generate random IDs within the range
    random_ids = np.random.randint(1, 231657, size=num_samples)

    # Retrieve 'Joke' column values for the random IDs
    selected_jokes = df.loc[df['ID'].isin(random_ids), 'Joke']

    return selected_jokes.tolist()

# Define the GUI layout
layout = [
    [sg.Button('Get Jokes')],
    [sg.Multiline(size=(28, 10), key='-OUTPUT-', disabled=True)]
]

# Create the window
window = sg.Window('Joke Generator', layout)

# Event loop
while True:
    event, values = window.read()

    # Handle window closed event
    if event == sg.WINDOW_CLOSED:
        break

    # Handle 'Get Jokes' button press
    if event == 'Get Jokes':
        jokes = retrieve_jokes('shortjokes.csv')
        window['-OUTPUT-'].update('\n****\n'.join(jokes))

# Close the window
window.close()
#```bash
#pip install PySimpleGUI
#```

#This script creates a simple window with a button. When the 'Get Jokes' button is pressed, it retrieves two random jokes using your `retrieve_jokes` function and updates the multiline Textbox with the jokes.