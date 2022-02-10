import logging

from PySide6.QtSql import QSqlDatabase, QSqlQuery

table_name = "Conversions"
QML_IMPORT_NAME = "ChatModel"
QML_IMPORT_MAJOR_VERSION = 1


def createTable():
    if table_name in QSqlDatabase.database().tables():
        return
    query = QSqlQuery()
    if not query.exec_(
            """
      CREATE TABLE IF NOT EXISTS 'Conversations' (
          'author' TEXT NOT NULL,
          'recipient' TEXT NOT NULL,
          'timestamp' TEXT NOT NULL,
          'message' TEXT NOT NULL,
      FOREIGN KEY('author') REFERENCES Contacts ( name ),
      FOREIGN KEY('recipient') REFERENCES Contacts ( name )
      )
      """
    ):
        logging.error("Failed to query database")
    query.exec_(
        """
                INSERT INTO Conversations VALUES(
                    'machine', 'Me', '2019-01-07T14:36:06', 'Hello!'
                )
                """
    )
