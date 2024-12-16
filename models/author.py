class Author:
    def __init__(self, id, name):
        # Initialize an Author instance with its attributes
        self._id = id  # Unique identifier for the author
        self._name = name  # Name of the author

    @property
    def id(self):
        # Property to get the author's ID
        return self._id

    @property
    def name(self):
        # Property to get the author's name
        return self._name

    @name.setter
    def name(self, value):
        # Prevent changing the author's name after initialization
        raise AttributeError("Name cannot be changed after initialization.")

    @staticmethod
    def create(name):
        # Static method to create a new author in the database
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))  # Insert author name
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

    @staticmethod
    def get_all():
        # Static method to retrieve all authors from the database
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()  # Fetch all authors
        conn.close()  # Close the database connection

        # Convert each row into an Author object
        author_objects = [Author(row["id"], row["name"]) for row in authors]
        return author_objects  # Return the list of Author objects

    @staticmethod
    def find_by_id(author_id):
        # Static method to find an author by their ID
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        author = cursor.fetchone()  # Fetch the author record
        conn.close()  # Close the database connection
        if author:
            # If the author exists, return an Author instance
            return Author(id=author['id'], name=author['name'])
        return None  # Return None if the author does not exist

    def update(self, name=None):
        # Method to update the author's name (not allowed, but included for completeness)
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (name, self._id))  # Update name
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

    def delete(self):
        # Method to delete the author from the database
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors WHERE id = ?", (self._id,))  # Delete the author using their ID
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection
        print(f"Author with ID {self._id} deleted successfully!")  # Confirmation message

    def __repr__(self):
        # String representation of the Author instance
        return f"<Author {self.name}>"  # Return the name of the author for easy identification