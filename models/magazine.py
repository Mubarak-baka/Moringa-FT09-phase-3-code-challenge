class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) <= 0:
            raise ValueError("Category must be longer than 0 characters.")
        self._category = value

    @staticmethod
    def create(name, category):
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        magazines = cursor.fetchall()
        conn.close()

        # Convert rows to dictionaries
        magazines_list = []
        for magazine in magazines:
            magazine_dict = {
                "id": magazine["id"],
                "name": magazine["name"],
                "category": magazine["category"]
            }
            magazines_list.append(magazine_dict)
        return magazines_list

    @staticmethod
    def find_by_id(magazine_id):
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
        magazine = cursor.fetchone()
        conn.close()
        if magazine:
            return Magazine(id=magazine['id'], name=magazine['name'], category=magazine['category'])
        return None

    def update(self, name=None, category=None):
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE magazines SET name = ? WHERE id = ?", (name, self._id))
        if category:
            cursor.execute("UPDATE magazines SET category = ? WHERE id = ?", (category, self._id))
        conn.commit()
        conn.close()

    def delete(self):
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM magazines WHERE id = ?", (self._id,))
        conn.commit()
        conn.close()
        print(f"Magazine with ID {self._id} deleted successfully!")

    def __repr__(self):
        return f"<Magazine {self.name}>"
