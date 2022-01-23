import pyautogui
import time
import keyboard
import mouse
import sys

pyautogui.PAUSE = 0.4

item_positions = ["1700,420", "1760,420", "1820,420", "1880,420",
                  "1700,480", "1760,480", "1820,480", "1880,480",
                  "1700,540", "1760,540", "1820,540", "1880,540",
                  "1700,600", "1760,600", "1820,600", "1880,600"]

inventory_positions = ["1700,370", "1750,370", "1800,370", "1850,370"]

GET_ALL = 970,695
CLOSE = 1080,695
OK_DIALOG = 965,593
QUANTITY_INPUT = 940,525
TITANIUM_MARTIAL_GLOVES_LOCATION = 160,410
EXTRACTION_ICON = 1698,637
EXTRACTION_ACCEPT = 965,621

                  
def main():
  alt_tab()
  iterations = get_iterations()
  first_buy = get_first_buy()
  for i in range(iterations):
    if first_buy:
      buy_titanium()
    else:
      first_buy = True
    toggle_extraction()
    for inv_pos in range(1,4):
        for item_pos in item_positions:
          click_inv(inv_pos)
          search_item(item_pos)
          accept_extraction()
    close_extraction()


def get_iterations():
  iterations = None
  try:
    iterations = int(sys.argv[1])
  except:
    iterations = 1
  return iterations

def get_first_buy():
  first_buy = None
  try:
    first_buy = False if lower(sys.argv[2]) == "false" else True
  except:
    first_buy = True
  return first_buy

def close_extraction():
  click(GET_ALL)
  click(CLOSE)
  toggle_extraction()
  
def alt_tab():
  pyautogui.hotkey('alt', 'tab')

def toggle_extraction():
  click(EXTRACTION_ICON)


def accept_extraction():
  click(EXTRACTION_ACCEPT)
  click(OK_DIALOG)


def search_item(item_pos):
  [x, y] = item_pos.split(",")
  click(int(x), int(y))

def click_inv(number):
  [x, y] = inventory_positions[number].split(",")
  click(int(x), int(y))

def click(x, y = 0):
  if type(x) == tuple:
    (x, y) = x
  pyautogui.click(x,y)

def buy_titanium(quantity = 48):
  pyautogui.moveTo(TITANIUM_MARTIAL_GLOVES_LOCATION)
  keyboard.press("alt")
  time.sleep(0.25)
  mouse.click("left")
  keyboard.release("alt")
  pyautogui.press("backspace")
  click_inv(1)
  click(QUANTITY_INPUT)
  for key in str(quantity):
    pyautogui.press(key)
  click(OK_DIALOG)


main()
