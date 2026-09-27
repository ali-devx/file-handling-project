import streamlit as st
from pathlib import Path
from datetime import datetime

# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(
    page_title="File Manager | CRUD App",
    page_icon="🗂️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------- CUSTOM CSS -----------------------------
st.markdown("""
    <style>
        .main-header {
            padding: 1.5rem 2rem;
            border-radius: 16px;
            background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #DB2777 100%);
            color: white;
            margin-bottom: 1.5rem;
        }
        .main-header h1 { margin: 0; font-size: 2rem; }
        .main-header p { margin: 0.3rem 0 0 0; opacity: 0.9; }

        .card {
            padding: 1.5rem;
            border-radius: 14px;
            background-color: rgba(127, 127, 127, 0.06);
            border: 1px solid rgba(127, 127, 127, 0.15);
            margin-bottom: 1rem;
        }

        .file-row {
            padding: 0.5rem 0.8rem;
            border-radius: 8px;
            background-color: rgba(127, 127, 127, 0.08);
            margin-bottom: 0.4rem;
            font-size: 0.85rem;
        }

        div[data-testid="stMetric"] {
            background-color: rgba(127, 127, 127, 0.08);
            padding: 0.8rem;
            border-radius: 12px;
        }

        .stButton>button {
            border-radius: 10px;
            font-weight: 600;
            padding: 0.5rem 1.2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------- WORKING DIRECTORY -----------------------------
if "work_dir" not in st.session_state:
    st.session_state.work_dir = str(Path.cwd())

# ----------------------------- HEADER -----------------------------
st.markdown("""
    <div class="main-header">
        <h1>🗂️ File Handling CRUD App</h1>
        <p>Create • Read • Update • Delete files — all from a simple UI</p>
    </div>
""", unsafe_allow_html=True)

# ----------------------------- SIDEBAR -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    work_dir_input = st.text_input("📁 Working directory", value=st.session_state.work_dir)
    st.session_state.work_dir = work_dir_input
    base_dir = Path(st.session_state.work_dir)

    st.divider()
    st.header("🧭 Navigation")
    operation = st.radio(
        "Choose an operation",
        ["➕ Create", "📖 Read", "✏️ Update", "🗑️ Delete"],
        label_visibility="collapsed",
    )

    st.divider()
    st.header("📂 Files in directory")

    if base_dir.exists() and base_dir.is_dir():
        files = sorted([f for f in base_dir.iterdir() if f.is_file()])
        if files:
            for f in files:
                size_kb = f.stat().st_size / 1024
                st.markdown(
                    f'<div class="file-row">📄 <b>{f.name}</b><br>'
                    f'<span style="opacity:0.7;">{size_kb:.1f} KB</span></div>',
                    unsafe_allow_html=True,
                )
        else:
            st.caption("No files found in this directory.")
    else:
        st.error("Directory does not exist.")

# ----------------------------- MAIN AREA -----------------------------
col1, col2, col3 = st.columns(3)
file_count = len([f for f in base_dir.iterdir() if f.is_file()]) if base_dir.exists() else 0
total_size = sum(f.stat().st_size for f in base_dir.iterdir() if f.is_file()) / 1024 if base_dir.exists() else 0
col1.metric("📄 Total Files", file_count)
col2.metric("💾 Total Size", f"{total_size:.1f} KB")
col3.metric("🕒 Time", datetime.now().strftime("%H:%M:%S"))

st.write("")

# ----------------------------- CREATE -----------------------------
if operation == "➕ Create":
    st.subheader("➕ Create a New File")
    with st.container(border=True):
        file_name = st.text_input("File name", placeholder="example.txt")
        content = st.text_area("File content", placeholder="Type what you want to write...", height=180)

        if st.button("Create File 🚀", type="primary"):
            if not file_name.strip():
                st.warning("Please enter a file name.")
            else:
                path = base_dir / file_name
                try:
                    if path.exists():
                        st.error(f"⚠️ '{file_name}' already exists.")
                    else:
                        path.write_text(content)
                        st.success(f"✅ File '{file_name}' created successfully!")
                        st.balloons()
                except Exception as err:
                    st.error(f"An error occurred: {err}")

# ----------------------------- READ -----------------------------
elif operation == "📖 Read":
    st.subheader("📖 Read a File")
    with st.container(border=True):
        file_name = st.text_input("File name to read", placeholder="example.txt")

        if st.button("Read File 🔍", type="primary"):
            if not file_name.strip():
                st.warning("Please enter a file name.")
            else:
                path = base_dir / file_name
                try:
                    if path.exists():
                        content = path.read_text()
                        st.success(f"✅ Showing content of '{file_name}'")
                        st.code(content if content.strip() else "(File is empty)", language=None)
                    else:
                        st.error("❌ No such file exists.")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

# ----------------------------- UPDATE -----------------------------
elif operation == "✏️ Update":
    st.subheader("✏️ Update a File")
    with st.container(border=True):
        file_name = st.text_input("File name to update", placeholder="example.txt")
        action = st.radio(
            "What would you like to do?",
            ["Rename", "Append content", "Overwrite content"],
            horizontal=True,
        )

        path = base_dir / file_name if file_name else None

        if action == "Rename":
            new_name = st.text_input("New file name")
            if st.button("Rename File 🔁", type="primary"):
                if not file_name.strip() or not new_name.strip():
                    st.warning("Please fill in both file names.")
                else:
                    try:
                        if not path.exists():
                            st.error("❌ No such file exists.")
                        else:
                            new_path = base_dir / new_name
                            if new_path.exists():
                                st.error(f"⚠️ '{new_name}' already exists.")
                            else:
                                path.rename(new_path)
                                st.success(f"✅ Renamed to '{new_name}' successfully!")
                    except Exception as err:
                        st.error(f"An error occurred: {err}")

        elif action == "Append content":
            append_content = st.text_area("Content to append", height=150)
            if st.button("Append ➕", type="primary"):
                if not file_name.strip():
                    st.warning("Please enter a file name.")
                else:
                    try:
                        if not path.exists():
                            st.error("❌ No such file exists.")
                        else:
                            with open(path, "a") as fs:
                                fs.write(append_content)
                            st.success("✅ Content appended successfully!")
                    except Exception as err:
                        st.error(f"An error occurred: {err}")

        elif action == "Overwrite content":
            new_content = st.text_area("New content", height=150)
            if st.button("Overwrite ♻️", type="primary"):
                if not file_name.strip():
                    st.warning("Please enter a file name.")
                else:
                    try:
                        if not path.exists():
                            st.error("❌ No such file exists.")
                        else:
                            path.write_text(new_content)
                            st.success("✅ Content overwritten successfully!")
                    except Exception as err:
                        st.error(f"An error occurred: {err}")

# ----------------------------- DELETE -----------------------------
elif operation == "🗑️ Delete":
    st.subheader("🗑️ Delete a File")
    with st.container(border=True):
        file_name = st.text_input("File name to delete", placeholder="example.txt")
        confirm = st.checkbox("I understand this action cannot be undone.")

        if st.button("Delete File 🗑️", type="primary", disabled=not confirm):
            if not file_name.strip():
                st.warning("Please enter a file name.")
            else:
                path = base_dir / file_name
                try:
                    if path.exists():
                        path.unlink()
                        st.success(f"✅ '{file_name}' deleted successfully!")
                    else:
                        st.error("❌ No such file exists.")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

# ----------------------------- FOOTER -----------------------------
st.divider()
st.caption("Built with ❤️ using Python & Streamlit — File Handling CRUD Project")