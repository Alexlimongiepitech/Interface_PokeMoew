import pyautogui
import pygetwindow as gw


CURSOR_POS = []


def find_discord_chat():
    activate_discord()
    discord_chat_locate = pyautogui.locateOnScreen(
        "resource/img/discord_chat.png", confidence=0.7
    )
    if discord_chat_locate != None:
        # print(discord_chat_locate)
        # pyautogui.moveTo(discord_chat_locate.left - 59, discord_chat_locate.top + 18)
        return [discord_chat_locate.left - 59, discord_chat_locate.top + 18]
    return [0, 0]


def cursor_on_discord_chat(pos):
    pyautogui.click(pos[0], pos[1])


def send_on_discord_chat(pos, message):
    cursor_on_discord_chat(pos)
    pyautogui.write(message)
    pyautogui.press("enter")
    back_old_windows()


def back_old_windows():
    try:
        pyautogui.moveTo(CURSOR_POS[0], CURSOR_POS[1])
        old_windows = gw.getWindowsWithTitle("MainWindow")[0]
        old_windows.activate()
    except (gw.PyGetWindowException, IndexError):
        pass


def activate_discord():
    global CURSOR_POS
    CURSOR_POS = pyautogui.position()
    discord_windows = gw.getWindowsWithTitle("Discord")[0]
    discord_windows.activate()
    back_old_windows()


if __name__ == "__main__":
    print(gw.getAllTitles())
