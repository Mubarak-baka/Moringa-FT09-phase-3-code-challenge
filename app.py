from database.setup import create_tables
from models.article import Article
from models.author import Author
from models.magazine import Magazine
import os 


def main():
    # Initialize the database and create tables
    create_tables()

    print("\nWelcome to the Magazine Manager!")
    print("1. Add Author")
    print("2. Add Magazine")
    print("3. Add Article")
    print("4. View Authors")
    print("5. View Magazines")
    print("6. View Articles")
    print("7. Update Article")
    print("8. Update Magazine")
    print("9. Update Author")
    print("10. Delete Article")
    print("11. Delete Magazine")
    print("12. Delete Author")
    print("13. Back")
    print("14. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                  # Add Author
                name = input("Enter author's name: ")
                Author.create(name)
                print(f"{name} added successfully!")

            elif choice == 2:
                os.system('clear')   # Add Magazine
                name = input("Enter magazine name: ")
                category = input("Enter magazine category: ")
                Magazine.create(name, category)
                print(f"{name} and {category} added successfully!")

            elif choice == 3:
                os.system('clear')   # Add Article
                title = input("Enter article title: ")
                content = input("Enter article content: ")
                author_id = int(input("Enter author ID: "))
                magazine_id = int(input("Enter magazine ID: "))
                Article.create(title, content, author_id, magazine_id)
                print(f" {title, content, author_id, magazine_id}, added successfully!")

            elif choice == 4:
                os.system('clear')   # View Authors
                print("\nAuthors:")
                authors = Author.get_all()
                for author in authors:
                    print(f"ID: {author.id}, Name: {author.name}")

            elif choice == 5:
                os.system('clear')   # View Magazines
                print("\nMagazines:")
                magazines = Magazine.get_all()
                for magazine in magazines:
                    print(f"ID: {magazine['id']}, Name: {magazine['name']}, Category: {magazine['category']}")

            elif choice == 6:
                os.system('clear')   # View Articles
                print("\nArticles:")
                articles = Article.get_all()
                for article in articles:
                    print(f"ID: {article['id']}, Title: {article['title']}, Content: {article['content']}")

            elif choice == 7:
                os.system('clear')   # Update Article
                article_id = int(input("Enter the ID of the article to update: "))
                new_title = input("Enter new title (leave blank to keep unchanged): ")
                new_content = input("Enter new content (leave blank to keep unchanged): ")
                article = Article.find_by_id(article_id)
                if article:
                    article.update(title=new_title if new_title else None,
                                   content=new_content if new_content else None)
                    print(f"Article updated successfully!")
                else:
                    print("Article not found!")

            elif choice == 8:
                os.system('clear')   # Update Magazine
                magazine_id = int(input("Enter the ID of the magazine to update: "))
                magazine = Magazine.find_by_id(magazine_id)
                if magazine:
                    new_name = input("Enter new name (leave blank to keep unchanged): ")
                    new_category = input("Enter new category (leave blank to keep unchanged): ")
                    magazine.update(name=new_name if new_name else None, category=new_category if new_category else None)
                    print(f"Magazine updated successfully!")
                else:
                    print("Magazine not found!")

            elif choice == 9:
                os.system('clear')   # Update Author
                author_id = int(input("Enter the ID of the author to update: "))
                author = Author.find_by_id(author_id)
                if author:
                    new_name = input("Enter new name (leave blank to keep unchanged): ")
                    author.update(name=new_name if new_name else None)
                    print(f"Author updated successfully!")
                else:
                    print("Author not found!")

            elif choice == 10:
                os.system('clear')   # Delete Article
                article_id = int(input("Enter the ID of the article to delete: "))
                article = Article.find_by_id(article_id)
                if article:
                    article.delete()
                    print(f"Article with ID {article_id} deleted successfully!")
                else:
                    print("Article not found!")

            elif choice == 11: 
                os.system('clear')  # Delete Article
                magazine_id = int(input("Enter the ID of the magazine to delete: "))
                magazine= Magazine.find_by_id(magazine_id)
                if magazine:
                    magazine.delete()
                    print(f"Magazine with ID {magazine_id} deleted successfully!")
                else:
                    print("Magazine not found!")
            elif choice == 12:
                os.system('clear')   # Delete Article
                author_id = int(input("Enter the ID of the aurthor to delete: "))
                author= Author.find_by_id(author_id)
                if author:
                    author.delete()
                    print(f"Author with ID {author_id} deleted successfully!")
                else:
                    print("Author not found!")
            elif choice == 13:
                main()
            

            elif choice == 14:
                os.system('clear')   # Exit
                print("Goodbye!")
                break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
