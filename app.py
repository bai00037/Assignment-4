import wikipedia
import random

# Lucas Bai
# 101300464

# Application idea taken from https://mindmajix.com/python-projects
# Project number 22 under the "For Intermediate Level" section

# This program's functionality is to keep displaying random Wikipedia articles until the user decides to read one.

def display_random_article():
    try:
        # Get a random article title
        random_title = wikipedia.random()
        print(f"Random Article Title: {random_title}")

        # Asking user if they are interested in the article
        user_input = input("Do you want to read this article? (yes/no):").strip().lower()

        if user_input == 'yes':
            # Display contents of article
            article_content = wikipedia.page(random_title).content
            print(f"\nContent of the article '{random_title}':\n")
            print(article_content)
        else:
            # Display another random article
            display_random_article()
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error: {e.options}")
        display_random_article()
    except wikipedia.exceptions.PageError:
        print("Page not found, redirecting to another article")
        display_random_article()

display_random_article()



