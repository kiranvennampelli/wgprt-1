import streamlit as st

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "index"  # Default page

# Header with inline links


# Placeholder content for the WGPRT page
st.title("Welcome to the WGPRT Tool")
st.header("WGPRT - WF Generative Payment Rail Testing Tool")
st.text("Use below links above to navigate to different sections of the application.")

# Navigation buttons to update session state
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Test Case Generator"):
        st.session_state.page = "index"
with col2:
    if st.button("Fraudulent Detection"):
        st.session_state.page = "fraudulent"
with col3:
    if st.button("Loan Approval"):
        st.session_state.page = "loan_approval"

# Render content based on the selected page
if st.session_state.page == "index":
    #st.subheader("Index Page Content")
 
    try:
        with open("test_case_generator.py") as f:
            code = f.read()
            exec(code)  # Dynamically execute the code from index.py
    except FileNotFoundError:
        st.error("The index.py file was not found.")
    except Exception as e:
        st.error(f"An error occurred while including index.py: {e}")

elif st.session_state.page == "fraudulent":
    #st.subheader("Fraudulent Detection Page Content")
    try:
        with open("fradulent.py") as f:
            code = f.read()
            exec(code)  # Dynamically execute the code from fraudulent.py
    except FileNotFoundError:
        st.error("The fraudulent.py file was not found.")
    except Exception as e:
        st.error(f"An error occurred while including fraudulent.py: {e}")

elif st.session_state.page == "loan_approval":
    #st.subheader("Loan Approval Page Content")
    try:
        with open("loan_approval.py") as f:
            code = f.read()
            exec(code)  # Dynamically execute the code from loan_approval.py
    except FileNotFoundError:
        st.error("The loan_approval.py file was not found.")
    except Exception as e:
        st.error(f"An error occurred while including loan_approval.py: {e}")