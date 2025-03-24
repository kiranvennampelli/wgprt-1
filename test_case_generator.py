import streamlit as st
from xsd_swagger_generator import generate_test_cases 
from xsd_swagger_generator import generate_api_test_cases
from swagger import generate_bdd_swagger

#st.title('WGPRT - 1')
#st.header('WF Generative Payment Rail Testing Tool')
#st.text('This tool generates test cases for the Wells Fargo Payment Rail Testing Tool.')

# Create two columns for side-by-side layout
col1, col2 = st.columns([1, 1])

# First widget: File uploader in the first column
with col1:
    st.subheader('Upload XSD File')
    uploaded_file = st.file_uploader('Upload XSD File', type=['xsd'])
    st.text('Please upload the XSD file that you would like to generate test cases for.')
    # Button to trigger test case generation
    if st.button('Generate Test Cases'):
        if uploaded_file is not None:
                # Save the uploaded file to a temporary location
                temp_file_path = f"temp_{uploaded_file.name}"
                with open(temp_file_path, "wb") as temp_file:
                    temp_file.write(uploaded_file.getbuffer())

                # Call the generate_test_cases function from wgprt.py
                try:
                    test_cases = generate_test_cases(temp_file_path)
                    st.text('Test cases generated successfully!')
                    st.code(test_cases)  # Display the generated test cases
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                finally:
                    # Clean up the temporary file
                    import os
                    if os.path.exists(temp_file_path):
                        os.remove(temp_file_path)
    else:
        st.error('Please upload an XSD file before generating test cases.')

# Second widget: Swagger URL input in the second column
with col2:
    st.subheader('Provide Swagger URL')
    swagger_url = st.text_input('Enter the Swagger URL for your REST APIs:')
    st.text('Please provide a valid Swagger URL to generate automation test cases.')

    # Button to trigger API test case generation
    if st.button('Generate API Test Cases'):
        if swagger_url:
            # Call the generate_api_test_cases function from wgprt.py
            try:
                api_test_cases = generate_api_test_cases(swagger_url)
                st.text('API test cases generated successfully!')
                st.code(api_test_cases)  # Display the generated API test cases
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error('Please provide a valid Swagger URL before generating API test cases.')
    if st.button('Generate BDD Test Cases'):
        if swagger_url:
            # Call the generate_api_test_cases function from wgprt.py
            try:
                api_test_cases = generate_bdd_swagger(swagger_url)
                st.text('API test cases generated successfully!')
                st.code(api_test_cases)  # Display the generated API test cases
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error('Please provide a valid Swagger URL before generating API test cases.')