import requests
from bs4 import BeautifulSoup
import os

# Function to check if a word is dangerous
def is_dangerous(word):
    dangerous_words = ["bomb", "kill", "murder", "terror", "terrorist", "terrorists", "terrorism"]
    return word.lower() in dangerous_words

# Function to parse HTML and count dangerous words
def count_dangerous_words(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    words = text.split()
    dangerous_word_count = sum(1 for word in words if is_dangerous(word))
    return dangerous_word_count

# Function to save content to file
def save_content(content, filepath):
    try:
        with open(filepath, 'wb') as file:
            file.write(content)
        print("Content saved successfully to", filepath)
    except Exception as e:
        print("Error saving content:", e)

# Main function
def main():
    url = input("Enter a valid URL to download: ")
    try:
        response = requests.get(url)
        response.raise_for_status()
        if 'text/html' in response.headers.get('content-type', ''):
            dangerous_word_count = count_dangerous_words(response.content)
            print("Number of dangerous words found:", dangerous_word_count)
        else:
            print("Content is not HTML, skipping dangerous word check.")
        
        filepath = input("Enter the path where to save the contents: ")
        save_content(response.content, filepath)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
