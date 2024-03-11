import tkinter as tk
from PIL import Image, ImageTk
from freetype import *

text = "JKUAT ROCKS!!"

def make_font(filename, size):
    face = Face(filename)
    face.set_char_size(size * 64)

    if not face.is_fixed_width:
        raise ValueError('Font is not monotype')

    width, height, ascender, descender = 0, 0, 0, 0

    for c in range(32, 128):
        face.load_char(chr(c), FT_LOAD_RENDER | FT_LOAD_FORCE_AUTOHINT)
        bitmap = face.glyph.bitmap
        width = max(width, bitmap.width)
        ascender = max(ascender, face.glyph.bitmap_top)
        descender = max(descender, bitmap.rows - face.glyph.bitmap_top)

    height = ascender + descender
    font_image = Image.new('L', (width * len(text), height), color=0)
    
    x_offset = 0
    for c in text:
        face.load_char(c, FT_LOAD_RENDER | FT_LOAD_FORCE_AUTOHINT)
        bitmap = face.glyph.bitmap
        font_image.paste(Image.frombytes('L', (bitmap.width, bitmap.rows), bytes(bitmap.buffer)),
                         (x_offset, ascender - face.glyph.bitmap_top))
        x_offset += width

    return ImageTk.PhotoImage(font_image)

class TextRendererApp:
    def __init__(self, master, font_image):
        self.master = master
        self.master.title("Freetype Text Renderer")

        self.label = tk.Label(master, image=font_image)
        self.label.pack()

def main():
    size = 120
    font_image = make_font("E:\Jkuat units\units 3.2\Computer Graphics\group_6_work_NO_1\DroidSansMono.ttf", size)

    root = tk.Tk()
    app = TextRendererApp(root, font_image)
    root.mainloop()

if __name__ == '__main__':
    main()
