import schedule
import time
from src.pesquisa_voo import pesquisa_voo


schedule.every(45).minutes.do(pesquisa_voo)

while True:
    schedule.run_pending()
    time.sleep(1)
