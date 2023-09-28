from liquidcrystal import LiquidCrystal
from pywiring import i2c

ioi = i2c.PCF8574IO(1, 0x27)
lcd = LiquidCrystal(ioi, en=8, rw=5, rs=7, data=[9, 10, 11, 12], bl=15, cols=16, rows=2)