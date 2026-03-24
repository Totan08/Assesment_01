import tkinter as tk
from PIL import Image, ImageTk

# -------------------- Create Window --------------------
root = tk.Tk()
root.title("PNG Background Window Template")
root.geometry("600x600")
root.configure(bg="black")
root.resizable(True, True)

# -------------------- Load PNG --------------------
image_path = "Background Test.png"  # Replace with your PNG file
try:
    original_image = Image.open(image_path)
except Exception as e:
    print(f"Error loading image: {e}")
    root.destroy()
    exit()

# -------------------- Canvas --------------------
canvas = tk.Canvas(root, width=600, height=800, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Keep references
background_image = None
image_id = None

def resize_image(event):
    global background_image, image_id
    if event.width < 1 or event.height < 1:
        return
    # Resize using updated Pillow 10+ method
    resized = original_image.resize(
        (event.width, event.height), resample=Image.Resampling.LANCZOS
    )
    background_image = ImageTk.PhotoImage(resized)
    if image_id is None:
        image_id = canvas.create_image(0, 0, anchor="nw", image=background_image)
    else:
        canvas.itemconfig(image_id, image=background_image)

root.bind("<Configure>", resize_image)

# -------------------- Run --------------------
root.mainloop()