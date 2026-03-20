# Notes Management System (Python)

## About the Project

This is a simple notes management system I created using Python.It helps to add, view, search, delete and save notes. I also added a feature where we can use AI to get responses or summaries.

---

## Features

* Add notes with title, content, tags and date
* View all note titles
* View full details of a note
* Search notes using keywords
* Delete notes
* Save notes into a CSV file
* Use AI to get responses

---

## Technologies Used

* Python
* CSV file handling
* datetime module
* dotenv
* OpenAI/Groq API

---

## How to Run

1. Clone the repository

```
git clone <>
cd <your-repo-folder>
```

2. Install required modules

```
pip install python-dotenv openai
```

3. Create a `.env` file and add your API key

```
OPENAI_API_KEY=your_api_key_here
```

4. Run the program

```
python notes.py
```

---

## Menu Options

When you run the program, you will see:

1. Add a Note
2. View all Notes
3. View specific Note Details
4. Search note by keyword
5. Delete a note
6. Save notes to CSV
7. Summarize using AI
8. Exit

---

## What I Learned

* How to use lists and dictionaries
* File handling using CSV
* Input validation (date format)
* Basic search logic
* How to use API in Python

---

## Limitations

* Data is not saved automatically
* No GUI (only command line)
* Search is case-sensitive

---

## Future Improvements

* Add GUI
* Use database instead of CSV
* Improve search functionality

---

## Author

Jatin (2nd Year Student)

---

This project is made for learning purposes.
