import tkinter as tk
from tkinter import filedialog, ttk, Text, Scrollbar
from PIL import Image, ImageTk
import pytesseract

# Uncomment and specify the Tesseract path if necessary (for Windows users):
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if file_path:
        # Open the selected image
        image = Image.open(file_path)
        image.thumbnail((400, 400))  # Resize image to fit in the window
        img_display = ImageTk.PhotoImage(image)

        # Display the image in the window
        image_label.config(image=img_display)
        image_label.image = img_display

        # Extract text from the image using pytesseract
        extracted_text = pytesseract.image_to_string(image)

        # Display the extracted text in the text widget
        text_box.delete(1.0, tk.END)  # Clear previous text
        text_box.insert(tk.END, extracted_text)

# Create the main window
root = tk.Tk()
root.title("Text Extraction from Image")
root.geometry("700x600")

# Use ttk for better styling
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc")

# Create a frame for better layout management
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Create a label to display the uploaded image
image_label = ttk.Label(frame)
image_label.pack(pady=20)

# Create a button to upload the image
upload_button = ttk.Button(frame, text="Upload Image", command=upload_image)
upload_button.pack()

# Create a scrollable text box for displaying extracted text
scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, height=10)
text_box.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

scrollbar.config(command=text_box.yview)

# Start the Tkinter event loop
root.mainloop()
