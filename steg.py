import tkinter as tk
from tkinter import filedialog, messagebox, font
from PIL import Image

class SteganographyApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Steganography")
        master.geometry("700x500")
        master.configure(bg="#ecf0f1")

        # Font and Style settings
        self.default_font = font.Font(family="Helvetica", size=11)
        self.bold_font = font.Font(family="Helvetica", size=11, weight="bold")
        self.button_bg = "#3498db"
        self.button_fg = "white"
        self.entry_bg = "#ffffff"
        self.entry_fg = "#2c3e50"
        self.label_fg = "#2c3e50"

        # Main Frames for Navigation
        self.main_frame = tk.Frame(master, bg="#ecf0f1")
        self.main_frame.pack(fill="both", expand=True)

        self.create_main_page()
        self.encode_frame = None
        self.decode_frame = None

    def create_main_page(self):
        # Buttons to navigate to Encode and Decode pages
        encode_button = tk.Button(self.main_frame, text="Encode", command=self.show_encode_page, bg=self.button_bg, fg=self.button_fg, font=self.default_font, relief="flat", bd=0, width=15)
        encode_button.pack(pady=20)

        decode_button = tk.Button(self.main_frame, text="Decode", command=self.show_decode_page, bg=self.button_bg, fg=self.button_fg, font=self.default_font, relief="flat", bd=0, width=15)
        decode_button.pack(pady=20)

    def show_encode_page(self):
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create and show encode frame
        if not self.encode_frame:
            self.encode_frame = tk.Frame(self.master, bg="#ecf0f1", padx=20, pady=20)
            self.create_encoding_frame()
        self.encode_frame.pack(fill="both", expand=True)

        back_button = tk.Button(self.encode_frame, text="Back to Main", command=self.show_main_page, bg=self.button_bg, fg=self.button_fg, font=self.default_font, relief="flat", bd=0, width=15)
        back_button.grid(row=3, column=1, pady=20)

    def show_decode_page(self):
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create and show decode frame
        if not self.decode_frame:
            self.decode_frame = tk.Frame(self.master, bg="#ecf0f1", padx=20, pady=20)
            self.create_decoding_frame()
        self.decode_frame.pack(fill="both", expand=True)

        back_button = tk.Button(self.decode_frame, text="Back to Main", command=self.show_main_page, bg=self.button_bg, fg=self.button_fg, font=self.default_font, relief="flat", bd=0, width=15)
        back_button.grid(row=2, column=1, pady=10)

    def create_encoding_frame(self):
        # Image Selection
        tk.Label(self.encode_frame, text="Select Image:", bg="#ecf0f1", fg=self.label_fg, font=self.bold_font).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.encode_image_path = tk.StringVar()
        encode_entry = tk.Entry(self.encode_frame, textvariable=self.encode_image_path, width=40, bg=self.entry_bg, fg=self.entry_fg, font=self.default_font, relief="flat")
        encode_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        browse_encode_button = tk.Button(self.encode_frame, text="Browse", command=self.browse_encode_image, bg=self.button_bg, fg=self.button_fg, font=self.default_font, relief="flat", bd=0)
        browse_encode_button.grid(row=0, column=2, padx=5, pady=5)

        # Message Input
        tk.Label(self.encode_frame, text="Enter Secret Message:", bg="#ecf0f1", fg=self.label_fg, font=self.bold_font).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.secret_message = tk.Text(self.encode_frame, height=8, width=50, bg=self.entry_bg, fg=self.entry_fg, font=self.default_font, relief="flat", bd=0)
        self.secret_message.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        # Encoding Button
        encode_button = tk.Button(self.encode_frame, text="Encode and Save", command=self.encode, bg=self.button_bg, fg=self.button_fg, font=self.default_font, relief="flat", bd=0)
        encode_button.grid(row=2, column=1, pady=10)

        # Configure column weights for resizing
        self.encode_frame.columnconfigure(1, weight=1)

    def create_decoding_frame(self):
        # Image Selection
        tk.Label(self.decode_frame, text="Select Image:", bg="#ecf0f1", fg=self.label_fg, font=self.bold_font).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.decode_image_path = tk.StringVar()
        decode_entry = tk.Entry(self.decode_frame, textvariable=self.decode_image_path, width=40, bg=self.entry_bg, fg=self.entry_fg, font=self.default_font, relief="flat")
        decode_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        browse_decode_button = tk.Button(self.decode_frame, text="Browse", command=self.browse_decode_image, bg=self.button_bg, fg=self.button_fg, font=self.default_font, relief="flat", bd=0)
        browse_decode_button.grid(row=0, column=2, padx=5, pady=5)

        # Decoding Button
        decode_button = tk.Button(self.decode_frame, text="Decode", command=self.decode, bg=self.button_bg, fg=self.button_fg, font=self.default_font, relief="flat", bd=0)
        decode_button.grid(row=1, column=1, pady=10)

        # Configure column weights for resizing
        self.decode_frame.columnconfigure(1, weight=1)

    def show_main_page(self):
        # Clear existing frames
        if self.encode_frame:
            self.encode_frame.pack_forget()
        if self.decode_frame:
            self.decode_frame.pack_forget()

        # Recreate main page
        for widget in self.master.winfo_children():
            widget.destroy()

        self.__init__(self.master)

    def browse_encode_image(self):
        self.encode_image_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]))

    def browse_decode_image(self):
        self.decode_image_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]))

    def encode(self):
        image_path = self.encode_image_path.get()
        message = self.secret_message.get("1.0", tk.END).strip()

        if not image_path or not message:
            messagebox.showerror("Error", "Please select an image and enter a message.")
            return

        try:
            img = Image.open(image_path)
            encoded_img = self.encode_message(img, message)

            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                encoded_img.save(save_path)
                messagebox.showinfo("Success", f"Image encoded and saved to {save_path}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decode(self):
        image_path = self.decode_image_path.get()

        if not image_path:
            messagebox.showerror("Error", "Please select an image to decode.")
            return

        try:
            img = Image.open(image_path)
            decoded_message = self.decode_message(img)
            messagebox.showinfo("Decoded Message", decoded_message)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def encode_message(self, img, message):
        data = message + "$t3g0"
        binary = ''.join(format(ord(i), '08b') for i in data)
        length = len(binary)

        if length > img.size[0] * img.size[1] * 3:
            raise ValueError("Error: Need a larger image to hide data")

        new_img = img.copy()
        data_index = 0

        for x in range(new_img.size[0]):
            for y in range(new_img.size[1]):
                pixels = list(new_img.getpixel((x, y)))
                for i in range(3):
                    if data_index < length:
                        pixels[i] = (pixels[i] & ~1) | int(binary[data_index])
                        data_index += 1

                new_img.putpixel((x, y), tuple(pixels))

                if data_index >= length:
                    break
            if data_index >= length:
                break

        return new_img

    def decode_message(self, img):
        binary_data = ""
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                pixels = list(img.getpixel((x, y)))
                for i in range(3):
                    binary_data += str(pixels[i] & 1)

                if len(binary_data) > 24:
                    delimiter_index = binary_data.find('0010010001110100001100110110011100110000')
                    if delimiter_index != -1:
                        binary_data = binary_data[:delimiter_index]
                        break
            if delimiter_index != -1:
                break

        all_bytes = [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]
        decoded_data = "".join(chr(int(byte, 2)) for byte in all_bytes)
        return decoded_data

root = tk.Tk()
app = SteganographyApp(root)
root.mainloop()
