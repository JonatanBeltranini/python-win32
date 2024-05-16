import win32gui
import win32con
import win32api

def find_window_by_title(title):
    hwnd = win32gui.FindWindow(None, title)
    if hwnd == 0:
        print("Janela não encontrada.")
        return None
    else:
        return hwnd

def find_button_by_text(hwnd, button_text):
    button_hwnd = None

    def callback(hwnd, lParam):
        nonlocal button_hwnd
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            text = win32gui.GetWindowText(hwnd)
            if text == button_text:
                button_hwnd = hwnd
                return False
        return True

    win32gui.EnumChildWindows(hwnd, callback, None)
    return button_hwnd

def click_button(hwnd):
    win32api.PostMessage(hwnd, win32con.BM_CLICK, 0, 0)

# Encontrar a janela principal
main_window_title = "Som"
main_window = find_window_by_title(main_window_title)

if main_window:
    # Encontrar o botão pelo texto
    button_text = "OK"
    button_hwnd = find_button_by_text(main_window, button_text)

    if button_hwnd:
        # Clicar no botão
        click_button(button_hwnd)
    else:
        print("Botão não encontrado.")
else:
    print("Janela não encontrada.")
