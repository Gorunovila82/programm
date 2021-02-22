from pypresence import Presence
from time import time
 
RPC = Presence("732122172855943179")
print(RPC)
btns = [
    {
        "label": "Site",
        "url": "https://gorunov.online"
    }
]
 
print(RPC.connect())
print(RPC.update(
    state="Сладкий арбуз!",
    details="Просто арбуз!",
    start=time(),
    buttons=btns,
    large_image="watermelon",
    small_image="small",
    large_text="арбузик :3",
    small_text="!Куда лезеш!"
))
 
input() # Чтобы программа резко не закрывалась.