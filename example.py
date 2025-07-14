import streamlit as st
from streamlit_datacard import datacard

st.set_page_config(page_title="Streamlit DataCard Component", layout="wide")

# Title
st.title("🎴 Streamlit DataCard")

# Brief description
st.markdown("""
A responsive card component for displaying structured data in Streamlit applications. 
Automatically arranges data into a clean grid layout with support for images, badges, and custom styling.
""")

# Parameters
st.subheader("Parameters")
st.markdown("""

- **`data`** *(list of dict)* - Your data records
- **`title_field`** *(str, optional)* - Field name to use as card title
- **`image_field`** *(str, optional)* - Field name containing image URLs  
- **`field_types`** *(dict, optional)* - Configure field display types
  - `"text"`: Regular text display (default)
  - `"badge"`: Colored pill-style badges
- **`card_width`** *(int)* - Width of each card in pixels (default: 280)
- **`max_height`** *(int)* - Maximum height of each card (default: 400)
- **`key`** *(str, optional)* - Unique component identifier
""")

# Example code
st.subheader("Example Code")
st.code("""
import streamlit as st
from streamlit_datacard import datacard

# Your data
data = [
    {
        "name": "Alice Johnson",
        "role": "Product Manager",
        "department": "Product",
        "status": "Active",
        "location": "San Francisco"
    },
    {
        "name": "Bob Smith",
        "role": "Software Engineer", 
        "department": "Engineering",
        "status": "Active",
        "location": "New York"
    }
]

# Configure field types
field_types = {
    "department": "badge",
    "status": "badge"
}

# Display cards
datacard(
    data=data,
    title_field="name",
    field_types=field_types,
    card_width=250,
    max_height=400
)
""", language="python")

st.markdown("---")

# Examples
st.subheader("Examples")

# Example 1: Employee Directory
st.markdown("**Employee Directory (Clickable)**")

if 'sample_data' not in st.session_state:
    st.session_state.sample_data = [
        {
            "name": "Alice Johnson",
            "role": "Product Manager",
            "department": "Product",
            "status": "Active",
            "location": "San Francisco",
            "email": "alice@company.com",
            "skills": "Strategy,Leadership,Analytics",
            "image": "https://api.dicebear.com/7.x/personas/svg?seed=Alice&backgroundColor=transparent"
        },
        {
            "name": "Bob Smith", 
            "role": "Software Engineer",
            "department": "Engineering",
            "status": "Active", 
            "location": "New York",
            "email": "bob@company.com",
            "skills": "Python,React,AWS",
            "image": "https://api.dicebear.com/7.x/personas/svg?seed=Bob&backgroundColor=transparent"
        },
        {
            "name": "Carol Davis",
            "role": "UX Designer",
            "department": "Design",
            "status": "On Leave",
            "location": "Los Angeles", 
            "email": "carol@company.com",
            "skills": "Figma,User Research,Prototyping",
            "image": "https://api.dicebear.com/7.x/personas/svg?seed=Carol&backgroundColor=transparent"
        }
    ]

field_types = {
    "department": "badge",
    "status": "badge", 
    "skills": "badge"
}

col1, col2 = st.columns([2, 1])

with col1:
    clicked =datacard(
        data=st.session_state.sample_data,
        title_field="name",
        image_field="image",
        field_types=field_types,
        card_width=200,
        max_height=500,
        key="employee_cards",
        clickable=True
    )

with col2:
    if clicked:
        st.subheader(f"Employee Profile: {clicked['name']}")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(clicked['image'], width=150)
        with col2:
            st.write(f"**Role:** {clicked['role']}")
            st.write(f"**Department:** {clicked['department']}")
            st.write(f"**Location:** {clicked['location']}")
            st.write(f"**Email:** {clicked['email']}")

            # Action buttons
            if st.button("📧 Send Email"):
                st.success(f"Email sent to {clicked['name']}!")
            if st.button("📅 Schedule Meeting"):
                st.success(f"Meeting scheduled with {clicked['name']}!")

    else:
        st.subheader("👈 Click on an employee card to view their profile")

st.markdown("**Project Tasks (Non-Clickable)**")

tasks = [
    {
        "task": "Design Homepage",
        "assignee": "Alice Johnson",
        "priority": "High",
        "status": "In Progress",
        "due_date": "2024-01-15",
        "completion": "75%"
    },
    {
        "task": "API Integration", 
        "assignee": "Bob Smith",
        "priority": "Medium",
        "status": "Todo",
        "due_date": "2024-01-20",
        "completion": "0%"
    },
    {
        "task": "Mobile Testing",
        "assignee": "Carol Davis",
        "priority": "High",
        "status": "Review",
        "due_date": "2024-01-18",
        "completion": "90%"
    }
]

col1, col2 = st.columns([2, 1])

with col1:
    datacard(
        data=tasks,
        title_field="task", 
        field_types={"priority": "badge", "status": "badge"},
        card_width=200,
        max_height=250,
        key="tasks"
    )
