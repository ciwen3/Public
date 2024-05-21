import tkinter as tk
from tkinter import filedialog
import os

# Import the steganography functions from the script
from steganography import file_to_bits, encode, decode

# Create the main window
window = tk.Tk()
window.title("Steganography Tool")

# Create a frame for the input and output paths
paths_frame = tk.Frame(window)
paths_frame.pack(fill="x")

# Create labels and text fields for the input and output paths
input_label = tk.Label(paths_frame, text="Input:")
input_label.pack(side="left")
input_field = tk.Entry(paths_frame)
input_field.pack(side="left", fill="x", expand=True)

output_label = tk.Label(paths_frame, text="Output:")
output_label.pack(side="left")
output_field = tk.Entry(paths_frame)
output_field.pack(side="left", fill="x", expand=True)

# Create a frame for the buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack(fill="x")

# Create a button to open a file dialog for the input path
def select_input():
    # Open the file dialog
    input_path = filedialog.askopenfilename()

    # Update the input field with the selected path
    input_field.delete(0, tk.END)
    input_field.insert(0, input_path)

input_button = tk.Button(buttons_frame, text="Select Input", command=select_input)
input_button.pack(side="left")

# Create a button to open a file dialog for the output path
def select_output():
    # Open the file dialog
    output_path = filedialog.asksaveasfilename()

    # Update the output field with the selected path
    output_field.delete(0, tk.END)
    output_field.insert(0, output_path)

output_button = tk.Button(buttons_frame, text="Select Output", command=select_output)
output_button.pack(side="left")

# Create a frame for the mode selection
mode_frame = tk.Frame(window)
mode_frame.pack(fill="x")

# Create radio buttons to select the mode (encode or decode)
mode = tk.StringVar()
mode.set("encode")

encode_button = tk.Radiobutton(mode_frame, text="Encode", variable=mode, value="encode")
encode_button.pack(side="left")

decode_button = tk.Radiobutton
(mode_frame, text="Decode", variable=mode, value="decode")
decode_button.pack(side="left")

# Create a frame for the run button
run_frame = tk.Frame(window)
run_frame.pack(fill="x")

# Create a button to run the program
def run():
    # Get the paths and mode from the GUI
    input_path = input_field.get()
    output_path = output_field.get()
    mode = mode.get()

    # Check if the input and output paths are valid
    if not os.path.exists(input_path):
        print("Error: Invalid input path")
        return
    if not os.path.exists(output_path):
        print("Error: Invalid output path")
        return

    if mode == "encode":
        # Convert the input file to a bit string
        bits = file_to_bits(input_path)

        # Encode the bit string in the input image and save the result
        encode(bits, input_path, output_path)
    elif mode == "decode":
        # Decode the input image and save the result
        decoded_file = decode(input_path)
        with open(output_path, "wb") as f:
            f.write(decoded_file)

run_button = tk.Button(run_frame, text="Run", command=run)
run_button.pack(side="right")

# Run the main loop
window.mainloop()
