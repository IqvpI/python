import ctypes  # An included library with Python install.
Title_Text = 'COOL!'
MBOX_text = 'Yes?'
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox(Title_Text, MBOX_text, 1)