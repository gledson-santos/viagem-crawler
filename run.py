import os
from multiprocessing import Pool


processos = ('export PYTHONPATH="${PYTHONPATH}:$PWD/src"', 'src/telegram/boot.py', 'src/consulta_scraping.py')


def roda_processo(processo):
    os.system('python {}'.format(processo))


if __name__ == '__main__':
    pool = Pool(processes=2)
    pool.map(roda_processo, processos)
