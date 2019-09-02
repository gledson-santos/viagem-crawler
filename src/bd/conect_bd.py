import mysql.connector


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
    except Exception as e:
      print(e)

  def busca(self, sql):
    try:
      self.mycursor.execute(sql)
      return self.mycursor.fetchall()

    except Exception as exception:
      print(exception)
