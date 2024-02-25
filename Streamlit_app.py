import streamlit as st



# Primary accent for interactive elements
primaryColor = '#E694FF'

# Background color for the main content area
backgroundColor = '#00172B'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#0083B8'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace)
# Default: "sans serif"
font = "sans serif"


# Set the theme to "dark" and customize the colors
st.set_page_config(layout="wide", page_title="My Streamlit App", theme="dark", primaryColor="red")

# Add your Streamlit app code here
st.title("My Streamlit App")
st.write("This is a Streamlit app.")




with st.container():
  st.subheader("Hello, I'm Rema! :wave:")
  st.title("A Passionate about Cybersecurity & Python Exploration")
  st.write("I'm a student in grade 8 with a passion for cybersecurity.")
  st.write("[learn More >](http://tinyurl.com/yc88wnmp)")

with st.container():
     st.write("---")
     left_column, right_column = st.columns(2)
     with left_column:
         st.header("what i do")
         st.write("##")
         st.write(
             """
             - Attending Al-ertiqaa school, I find myself drawn to Python 
               programming and the world of cybersecurity—it's an exciting 
               field that truly captivates me. Among my favorite subjects, 
               CCDI and Math hold a special place.

               Join me on this thrilling journey as I explore the depths 
               of cybersecurity and Python. Let's learn together and pave 
               the way for a future filled with innovation and security.


             """
        )
         st.write("[Youtube Channel >](https://youtube.com/@RemaAl-sawalhi?feature=shared)")

with st.container():
  st.write("---")
  st.header("My Projects")
  st.write("##")
  image_column, text_column = st.columns((1, 2))
  st.markdown('<iframe width="560" height="315" src="https://www.youtube.com/embed/ljISoc0kjTo?feature=shared" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
