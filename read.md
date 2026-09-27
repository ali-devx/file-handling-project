# 🗂️ File Handling CRUD Project

A simple Python project that performs **CRUD operations (Create, Read, Update, Delete)** on files, using `pathlib` and proper exception handling. Available as a **command-line tool** (`file_handler.py`) and as a **Streamlit web app** (`app.py`) with a clean UI.

---

## ✨ Features

- ➕ **Create** a new file with custom content
- 📖 **Read** and display the content of any file
- ✏️ **Update** a file:
  - Rename it
  - Append new content
  - Overwrite existing content
- 🗑️ **Delete** a file (with a confirmation checkbox in the UI)
- 📂 Live sidebar file browser showing all files in the working directory
- 📊 Quick stats: total files, total size, current time
- ⚠️ Proper error handling for missing files, duplicate names, etc.

---

## 🖥️ Tech Stack

Python 3 · Pathlib · Streamlit

---

## 📂 Project Structure

```
File Handling Project/
├── file_handler.py     # CLI version
├── app.py               # Streamlit UI version
├── requirements.txt      # Dependencies
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/file-handling-project.git
cd file-handling-project
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app

**Streamlit UI:**
```bash
streamlit run app.py
```

**CLI version:**
```bash
python3 file_handler.py
```

---

## 🧠 What I Learned

Working with `pathlib` for file operations, structuring a CLI tool with proper exception handling, building a UI on top of it with Streamlit, and managing Python virtual environments.

---
