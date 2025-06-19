import mysql.connector
import os

#Set up a known good state every test run
def reset_test_db():
    connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
    )
    cursor = connection.cursor()

    with open("../../sql/budget_tool_db_test.sql", "r") as f:
        sql_commands = f.read().split(';')
        for cmd in sql_commands:
            if cmd.strip():
                cursor.execute(cmd)

    connection.commit()
    cursor.close()
    connection.close()