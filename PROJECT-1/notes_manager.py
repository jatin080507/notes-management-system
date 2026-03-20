import csv
import os
from dotenv import load_dotenv
from datetime import datetime
note_management = []

def add_note():
    note_title = input("Enter the note title: ")
    note_content = input("Enter the content of note: ")
    note_tags = input("Enter the tags(comma separated): ").split(",")
    while True:
        note_date = input("Enter the date(DD-MM-YYYY): ")
        try:
            datetime.strptime(note_date, "%d-%m-%Y")  # validate format
            break
        except ValueError:
            print("Invalid date format! Please enter in DD-MM-YYYY format.")

    notes = {
        "note title": note_title,
        "content": note_content,
        "tags": note_tags,
        "date": note_date
    }
    note_management.append(notes)
    print("Note has been added successfully.\n")

def view_notes():
    if len(note_management) == 0:
        print("No Note Found.\n")
    else:
        print("The titles in the notes are:")
        for note in note_management:
            print("--->", note["note title"])
        print()

def view_note_details():
    note_title = input("Enter the title of note to get details: ")
    found = False
    for note_details in note_management:
        if note_details["note title"] == note_title:
            print(f"The details of the {note_title} are:")
            print(f"{note_details['note title']} , {note_details['content']} , {note_details['tags']} , {note_details['date']}\n")
            found = True
            break
    if not found:
        print("Note not found in your collection.\n")

def search_note():
    keyword = input("Enter keyword to search: ")
    for note in note_management:
        if keyword in note["note title"] or keyword in note["content"] or any(keyword in tag for tag in note["tags"]):
            print("Found:", note["note title"])
            break
    else:
        print(f"No title found with keyword: {keyword}\n")

def delete_note():
    note_title = input("Enter the title of note to delete: ")
    for note in note_management:
        if note["note title"] == note_title:
            note_management.remove(note)
            print("Note has been deleted successfully\n")
            break
    else:
        print("Note not found.\n")

def save_to_csv(file_name, note_management):
    print("Saving notes to:", os.path.abspath(file_name))
    with open(file_name, "w") as file:
        file.write("note title,content,tags,date\n")
        for note in note_management:
            title = note["note title"]
            content = note["content"]
            tags = "|".join(note["tags"])
            date = note["date"]
            file.write(f"{title},{content},{tags},{date}\n")
    print("Notes saved successfully!\n")

def summarize_note():
    from openai import OpenAI
    script_folder = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(script_folder, ".env"))

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("API key not found! Please create a .env file in the project folder with your key.")
        return

    client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=api_key)

    query = input("Enter what do you want to get from AI: ")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": query}]
    )

    print(response.choices[0].message.content)

def main():
    while True:
        print("----Notes Management Menu----")
        print("1. To Add a Note")
        print("2. To View all Notes")
        print("3. To View specific Note Details")
        print("4. To search the note by keyword")
        print("5. To delete a note")
        print("6. To save all notes to csv")
        print("7. To Summarize notes using AI")
        print("8. Exit")

        try:
            ch = int(input("Enter your choice: "))
            if ch == 1:
                add_note()
            elif ch == 2:
                view_notes()
            elif ch == 3:
                view_note_details()
            elif ch == 4:
                search_note()
            elif ch == 5:
                delete_note()
            elif ch == 6:
                file_name = "notes_management.csv"
                save_to_csv(file_name, note_management)
            elif ch == 7:
                summarize_note()
            elif ch == 8:
                break
            else:
                print("Invalid choice. Please enter between 1-8\n")
        except ValueError:
            print("Invalid choice. Please enter a number between 1-8\n")


if __name__ == "__main__":
    main()