import win32gui
import win32api
import win32con
import time


def click_button(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, 0)



def send_textbox_text(hwnd, text):
    win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, None, text)









def find_window(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        print("Janela não encontrada.")
    else:
        return hwnd

def get_child_windows(hwnd):
    child_windows = []

    def enum_child_windows(hwnd, param):
        child_windows.append(hwnd)
        return True

    win32gui.EnumChildWindows(hwnd, enum_child_windows, None)

    return child_windows

def get_window_text(hwnd):
    #text_length = win32gui.GetWindowTextLength(hwnd) + 1
    #buffer = ' ' * text_length
    nome = win32gui.GetWindowText(hwnd)
    return nome

def get_window_class(hwnd):
    return win32gui.GetClassName(hwnd)

def map_window_components(hwnd):
    child_windows = get_child_windows(hwnd)

    for child in child_windows:
        class_name = get_window_class(child)
        text = get_window_text(child)

        print("Componente:")
        print("Classe:", class_name)
        print("Texto:", text)
        print("Identificador:", child)
        print("-" * 50)
# Encontrar a janela principal
main_window_title = "Salvar Esquema como"
main_window = find_window(main_window_title)

if main_window:

    #click_button(263698)
    time.sleep(2)
    send_textbox_text(723032, "Texto que você quer digitar")
    map_window_components(main_window)
else:
    print("Janela não encontrada.")
