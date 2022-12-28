import base64
import tkinter as tk

def on_button_click():
    # Get the hex string from the text entry
    hex_string = entry.get()

    # Decode the hex string to a bytes object
    bytes_obj = bytes.fromhex(hex_string)

    # Encode the bytes object to a base64 string
    base64_string = base64.b64encode(bytes_obj).decode()

    # Update the label with the result
    result_label.config(text=base64_string)

# Create the main window
root = tk.Tk()
root.title("Hex to Base64 Converter")

# Create a label and a text entry for the hex string
label = tk.Label(root, text="Enter a hex string:")
entry = tk.Entry(root)

# Create a button to trigger the conversion
button = tk.Button(root, text="Convert", command=on_button_click)

# Create a label to display the result
result_label = tk.Label(root, text="")

# Add the widgets to the window
label.pack()
entry.pack()
button.pack()
result_label.pack()

# Run the main loop
root.mainloop()
