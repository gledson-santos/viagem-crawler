import schedule
import time
from src.pesquisa_voo import pesquisa_voo


schedule.every(0.1).minutes.do(pesquisa_voo)

while True:
    schedule.run_pending()
    time.sleep(1)
