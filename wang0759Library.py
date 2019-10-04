
def xLine():
    y = 50
    x = 0
    while (x <= 127):
        lcd.set_pixel(x, y, 1)
        x = x + 1
    lcd.show()


def yLine():
    x = 80
    y = 0
    while (y <= 63):
        lcd.set_pixel(x, y, 1)
        y = y + 1
    lcd.show()


def stair():
    w = 48
    h = 0
    while (h <= 36):
        lcd.set_pixel(h, w, 1)
        h = h + 1
    lcd.show()
    h = 36
    w = 24
    while (w <= 48):
        lcd.set_pixel(h, w, 1)
        w = w + 1
    lcd.show()

    w = 24
    h = 36
    while (h <= 95):
        lcd.set_pixel(h, w, 1)
        h = h + 1
    lcd.show()

    h = 95
    w = 0
    while (w <= 24):
        lcd.set_pixel(h, w, 1)
        w = w + 1
    lcd.show()


def randPixel():
    i = 0
    while i < 10:
        i += 1
        x = random.randint(0, 127)
        y = random.randint(0, 63)
        lcd.set_pixel(x, y, 1)
        lcd.show()
        time.sleep(2)
    lcd.clear()
    lcd.show()


def clearBacklight():
    backlight.set_all(255, 100, 100)
    backlight.show()
    time.sleep(2)
    lcd.clear()
    backlight.set_all(200, 200, 200)
    backlight.show()

