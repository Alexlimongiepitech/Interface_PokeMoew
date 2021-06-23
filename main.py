import pyautogui
import pygetwindow


CURSOR_POS = []


def find_discord_chat():
    activate_discord()
    discord_chat_locate = pyautogui.locateOnScreen(r"discord_chat.png", confidence=0.7)
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
        old_windows = pygetwindow.getWindowsWithTitle("Interface_PokeMoew")[0]
        old_windows.activate()
    except (pygetwindow.PyGetWindowException, IndexError):
        pass


def activate_discord():
    global CURSOR_POS
    CURSOR_POS = pyautogui.position()
    discord_windows = pygetwindow.getWindowsWithTitle("Discord")[0]
    discord_windows.activate()
    back_old_windows()


def good_id_arena(region_str, arena_int):
    if region_str == "Kanto":
        if arena_int == 1:
            return 1
        if arena_int == 2:
            return 2
        if arena_int == 3:
            return 3
        if arena_int == 4:
            return 4
        if arena_int == 5:
            return 5
        if arena_int == 6:
            return 6
        if arena_int == 7:
            return 7
        if arena_int == 8:
            return 8
    if region_str == "Johto":
        if arena_int == 1:
            return 14
        if arena_int == 2:
            return 15
        if arena_int == 3:
            return 16
        if arena_int == 4:
            return 17
        if arena_int == 5:
            return 18
        if arena_int == 6:
            return 19
        if arena_int == 7:
            return 20
        if arena_int == 8:
            return 21
    if region_str == "Hoenn":
        if arena_int == 1:
            return 27
        if arena_int == 2:
            return 28
        if arena_int == 3:
            return 29
        if arena_int == 4:
            return 30
        if arena_int == 5:
            return 31
        if arena_int == 6:
            return 32
        if arena_int == 7:
            return 33
        if arena_int == 8:
            return 34
    if region_str == "Sinnoh":
        if arena_int == 1:
            return 40
        if arena_int == 2:
            return 40
        if arena_int == 3:
            return 42
        if arena_int == 4:
            return 43
        if arena_int == 5:
            return 44
        if arena_int == 6:
            return 45
        if arena_int == 7:
            return 46
        if arena_int == 8:
            return 47
    if region_str == "Unova":
        if arena_int == 1:
            return 53
        if arena_int == 2:
            return 54
        if arena_int == 3:
            return 55
        if arena_int == 4:
            return 56
        if arena_int == 5:
            return 57
        if arena_int == 6:
            return 58
        if arena_int == 7:
            return 59
        if arena_int == 8:
            return 60
    if region_str == "Kalos":
        if arena_int == 1:
            return 66
        if arena_int == 2:
            return 67
        if arena_int == 3:
            return 68
        if arena_int == 4:
            return 69
        if arena_int == 5:
            return 70
        if arena_int == 6:
            return 71
        if arena_int == 7:
            return 72
        if arena_int == 8:
            return 73
    return 0


def good_id_elite_four(region_str, elite_four_int):
    if region_str == "Kanto":
        if elite_four_int == 1:
            return 9
        if elite_four_int == 2:
            return 10
        if elite_four_int == 3:
            return 11
        if elite_four_int == 4:
            return 12
    if region_str == "Johto":
        if elite_four_int == 1:
            return 22
        if elite_four_int == 2:
            return 23
        if elite_four_int == 3:
            return 24
        if elite_four_int == 4:
            return 25
    if region_str == "Hoenn":
        if elite_four_int == 1:
            return 35
        if elite_four_int == 2:
            return 36
        if elite_four_int == 3:
            return 37
        if elite_four_int == 4:
            return 38
    if region_str == "Sinnoh":
        if elite_four_int == 1:
            return 48
        if elite_four_int == 2:
            return 49
        if elite_four_int == 3:
            return 50
        if elite_four_int == 4:
            return 51
    if region_str == "Unova":
        if elite_four_int == 1:
            return 61
        if elite_four_int == 2:
            return 62
        if elite_four_int == 3:
            return 63
        if elite_four_int == 4:
            return 64
    if region_str == "Kalos":
        if elite_four_int == 1:
            return 74
        if elite_four_int == 2:
            return 75
        if elite_four_int == 3:
            return 76
        if elite_four_int == 4:
            return 77
    return 0


if __name__ == "__main__":
    print(gw.getAllTitles())
