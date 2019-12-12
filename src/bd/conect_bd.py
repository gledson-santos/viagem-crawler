import mysql.connector
from src.graylog import *


class ConectBd(object):

  def __init__(self):
    self.conect = mysql.connector.connect(
      host="localhost",
      port="3306",
      database='db_gol',
      user="root",
      passwd="root"
    )
    self.mycursor = self.conect.cursor(dictionary=True)

  def executa(self, sql):
    try:
      self.mycursor.execute(sql)
      return self.conect.commit()
    except Exception as exception:
      logger.exception(exception)
      print(exception)

  def busca(self, sql):
    try:
      self.mycursor.execute(sql)
      return self.mycursor.fetchall()
    except Exception as exception:
      insere_log(exception)
      print(exception)
