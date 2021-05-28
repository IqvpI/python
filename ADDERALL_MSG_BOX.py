import ctypes  # An included library with Python install.
Title_Text = 'ADDERALL LOG ENTRY'
MBOX_text = 'PLEASE ENTER DOSE'
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
