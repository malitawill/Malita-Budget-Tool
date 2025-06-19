from typing import Optional

from models.user_account_models import UserAccount
from data.db_connection import create_connection

# #Provides the CRUD Methods that access the database
class UserAccountRepository:
    def __init__(self):
        self.conn = create_connection()

    #Find by id
    def find_by_id(self, user_id: int) -> Optional[UserAccount]:
        try:
            cursor = self.conn.cursor(dictionary=True, buffered=True)
            cursor.execute("SELECT * FROM user_account WHERE user_account_id = %s", (user_id,))
            result = cursor.fetchone()
            cursor.close()
            if result:

                return UserAccount(**result)
            return None
        except Exception as e:
            print(f"Error in find_by_id: {e}")
            return None

    #def create_account(UserAccount user_account):

    #def update_account(UserAccount user_account):

    #def delete_account(int user_id):

