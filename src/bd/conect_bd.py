import mysql.connector


class ConectBd(object):

  def __init__(self):
    self.conect = mysql.connector.connect(
      host="database-1.ctnwzbi1oqcr.us-east-2.rds.amazonaws.com",
      port="3306",
      database='db_gol',
      user="admin",
      passwd="sentapua"
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
