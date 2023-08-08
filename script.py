import time
import pyautogui as pg

oldPosX = None
oldPosY = None
firstPos = {"x": None, "y": None}
disassembleFrame = {"x": None, "y": None}
disassembleButton = {"x": None, "y": None}
disassembledResultConfirmButton = {"x": None, "y": None}
buyCursorPos = {"x": None, "y": None}
buyConfirmPurchaseButton = {"x": None, "y": None}

print("=== Buy Cursor Position ===")
buyCursorPos["x"] = int(input("Coordinate X: "))
buyCursorPos["y"] = int(input("Coordinate Y: "))

print()

print("=== Buy Confirm Purchase Button Position ===")
buyConfirmPurchaseButton["x"] = int(input("Coordinate X: "))
buyConfirmPurchaseButton["y"] = int(input("Coordinate Y: "))

print()

print("=== First Item Position ===")
firstPos["x"] = int(input("Coordinate X: "))
oldPosX = firstPos["x"]
firstPos["y"] = int(input("Coordinate Y: "))
oldPosY = firstPos["y"]

print()

print("=== Disassemble Frame Position ===")
disassembleFrame["x"] = int(input("Coordinate X: "))
disassembleFrame["y"] = int(input("Coordinate Y: "))

print()

print("=== Disassemble Frame Button Begin Position ===")
disassembleButton["x"] = int(input("Coordinate X: "))
disassembleButton["y"] = int(input("Coordinate Y: "))

print()

print("=== Disassemble Frame Button Assembled Result Position ===")
disassembledResultConfirmButton["x"] = int(input("Coordinate X: "))
disassembledResultConfirmButton["y"] = int(input("Coordinate Y: "))

print()

print("Program will start in 10 second, ALT + TAB to your ROSE Online now!")
time.sleep(10)

buyCount = 0
while True:
    for i in range(0, 27):
        # if the buy count same as in array confirm the purchase
        if buyCount in [10, 20, 26]:
            pg.click(
                buyConfirmPurchaseButton["x"],
                buyConfirmPurchaseButton["y"],
                duration=0.5,
            )

        # buying item
        if buyCount != 26:
            pg.hold("shift")
            pg.moveTo(buyCursorPos["x"], buyCursorPos["y"])
            pg.doubleClick(buyCursorPos["x"], buyCursorPos["y"], duration=0.3)

        buyCount = buyCount + 1

    time.sleep(3)

    # dissasembling item that just bought
    for i in range(0, 26):
        # change direction inventory 1 step below
        if i in [6, 12, 18, 24]:
            firstPos["x"] = oldPosX
            firstPos["y"] = firstPos["y"] + 54  # hardcoded, do not change!

        # dragging item to dissasemble frame
        pg.moveTo(firstPos["x"], firstPos["y"])
        pg.dragTo(
            disassembleFrame["x"], disassembleFrame["y"], button="left", duration=0.6
        )

        # click the disassemble button
        pg.moveTo(disassembleButton["x"], disassembleButton["y"])
        pg.click(disassembleButton["x"], disassembleButton["y"], duration=0.7)

        # click the result of disassembled item
        pg.moveTo(
            disassembledResultConfirmButton["x"],
            disassembledResultConfirmButton["y"],
        )
        pg.click(
            disassembledResultConfirmButton["x"],
            disassembledResultConfirmButton["y"],
            duration=2,
        )

        firstPos["x"] = firstPos["x"] + 56  # hardcoded, do not change!

    # reset position
    firstPos["x"] = oldPosX
    firstPos["y"] = oldPosY
    buyCount = 0

    print("Program will start again in 1 second, ALT + TAB to your ROSE Online now!")
    time.sleep(1)
