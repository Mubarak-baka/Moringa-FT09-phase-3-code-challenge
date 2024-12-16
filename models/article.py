class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        # Initialize an Article instance with its attributes
        self._id = id  # Unique identifier for the article
        self._title = title  # Title of the article
        self.content = content  # Content of the article
        self._author_id = author_id  # ID of the author who wrote the article
        self._magazine_id = magazine_id  # ID of the magazine where the article is published

    @property
    def id(self):
        # Property to get the article's ID
        return self._id

    @property
    def title(self):
        # Property to get the article's title
        return self._title

    @property
    def author(self):
        # Property to fetch the author details from the database using the author's ID
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (self._author_id,))
        author = cursor.fetchone()  # Fetch the author record
        conn.close()  # Close the database connection
        return author  # Return the author details

    @property
    def magazine(self):
        # Property to fetch the magazine details from the database using the magazine's ID
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (self._magazine_id,))
        magazine = cursor.fetchone()  # Fetch the magazine record
        conn.close()  # Close the database connection
        return magazine  # Return the magazine details

    @staticmethod
    def create(title, content, author_id, magazine_id):
        # Static method to create a new article in the database
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
            (title, content, author_id, magazine_id)  # Insert article details
        )
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

    @staticmethod
    def get_all():
        # Static method to retrieve all articles from the database
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        articles = cursor.fetchall()  # Fetch all articles
        conn.close()  # Close the database connection

        # Convert rows to dictionaries for easier access
        articles_list = []
        for article in articles:
            article_dict = {
                "id": article["id"],
                "title": article["title"],
                "content": article["content"],
                "author_id": article["author_id"],
                "magazine_id": article["magazine_id"]
            }
            articles_list.append(article_dict)  # Append each article as a dictionary

        return articles_list  # Return the list of articles

    @staticmethod
    def find_by_id(article_id):
        # Static method to find an article by its ID
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
        article = cursor.fetchone()  # Fetch the article record
        conn.close()  # Close the database connection
        if article:
            # If the article exists, return an Article instance
            return Article(id=article['id'], title=article['title'], content=article['content'], 
                           author_id=article['author_id'], magazine_id=article['magazine_id'])
        return None  # Return None if the article does not exist

    def update(self, title=None, content=None):
        # Method to update the article's title and/or content
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        if title:
            cursor.execute("UPDATE articles SET title = ? WHERE id = ?", (title, self._id))  # Update title
        if content:
            cursor.execute("UPDATE articles SET content = ? WHERE id = ?", (content, self._id))  # Update content
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

    def delete(self):
        # Method to delete the article from the database
        from database.connection import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles WHERE id = ?", (self._id,))  # Delete # the article using its ID
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

    def __repr__(self):
        # String representation of the Article instance
        return f"<Article {self.title}>"  # Return the title of the article for easy identification