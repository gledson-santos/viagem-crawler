import schedule
import time
from src.pesquisa_voo import pesquisa_voo


schedule.every(35).minutes.do(pesquisa_voo)

while True:
    schedule.run_pending()
    time.sleep(1)
    schedule.next_run()
