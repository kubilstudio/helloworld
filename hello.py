import time
import os

# สี ANSI
CYAN = "\033[96m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()

print(CYAN + "=" * 70 + RESET)
print(YELLOW + "                 🚢  HELLO WORLD  🚢" + RESET)
print(CYAN + "=" * 70 + RESET)

time.sleep(0.5)

ship = r"""
                         |    |    |
                        )_)  )_)  )_)
                       )___))___))___)\
                      )____)____)_____)\\
                    _____|____|____|____\\__
                  \                         /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       ~~~~        ~~~~~       ~~~~~       ~~~~
    ~~~~~~~~    ~~~~~~~~    ~~~~~~~~    ~~~~~~~~
"""

print(BLUE + ship + RESET)

time.sleep(0.5)

print(GREEN + "=" * 70 + RESET)
print("              🌊  WELCOME ABOARD!  🌊")
print("              ⚓ Captain is ready!")
print(GREEN + "=" * 70 + RESET)

# คลื่นน้ำ animation
print()

for i in range(3):
    print("🌊" * (10+i*5))
    time.sleep(0.3)

print()
print(YELLOW + "🚢 Journey started..." + RESET)