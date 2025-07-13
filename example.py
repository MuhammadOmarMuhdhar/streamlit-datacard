import streamlit as st
from streamlit_datacard import datacard

st.set_page_config(page_title="Streamlit DataCard Component", layout="centered")

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
st.markdown("**Employee Directory**")

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

datacard(
    data=st.session_state.sample_data,
    title_field="name",
    image_field="image",
    field_types=field_types,
    card_width=200,
    max_height=500,
    key="employee_cards"
)

st.markdown("**Project Tasks**")

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

datacard(
    data=tasks,
    title_field="task", 
    field_types={"priority": "badge", "status": "badge"},
    card_width=200,
    max_height=250,
    key="tasks"
)

st.markdown("**Product Catalog**")

products = [
    {
        "name": "Wireless Headphones",
        "price": "$199.99",
        "category": "Electronics", 
        "rating": "⭐⭐⭐⭐⭐",
        "stock": "In Stock",
        "description": "Premium noise-cancelling headphones",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300&h=200&fit=crop&crop=center"
    },
    {
        "name": "Smart Watch",
        "price": "$299.99", 
        "category": "Wearables",
        "rating": "⭐⭐⭐⭐",
        "stock": "Low Stock",
        "description": "Advanced fitness tracking",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=300&h=200&fit=crop&crop=center"
    },
    {
        "name": "Laptop Stand",
        "price": "$49.99",
        "category": "Accessories",
        "rating": "⭐⭐⭐⭐⭐",
        "stock": "In Stock",
        "description": "Ergonomic workspace solution",
        "image": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=300&h=200&fit=crop&crop=center"
    },
    {
        "name": "Bluetooth Speaker",
        "price": "$79.99",
        "category": "Electronics",
        "rating": "⭐⭐⭐⭐",
        "stock": "In Stock",
        "description": "Portable wireless speaker with bass",
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=300&h=200&fit=crop&crop=center"
    }
]

datacard(
    data=products,
    title_field="name",
    image_field="image",
    field_types={"category": "badge", "stock": "badge"},
    card_width=220,
    max_height=500,
    key="products"
)

