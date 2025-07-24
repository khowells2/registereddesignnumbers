import pandas as pd
import re
import streamlit as st # Assuming you'll use Streamlit

# Function to find the relevant rows for a given design number
def find_relevant_rows(design_number, df):
    relevant_rows = []
    for index, row in df.iterrows():
        description = str(row['Description'])
        match = re.search(r'Designs (\d+)-(\d+)', description)
        if match:
            start, end = int(match.group(1)), int(match.group(2))
            if start <= design_number <= end:
                relevant_rows.append(row)
    if relevant_rows:
        return pd.DataFrame(relevant_rows)
    else:
        return pd.DataFrame()

# --- Streamlit App ---

st.title('Design Number Lookup')

# Specify the URL of the CSV file in your GitHub repository
github_csv_url = 'TNA_Search_Results_23-07-2025T12_26_09.csv' # Replace with the actual URL

df = None
try:
try:
    df = pd.read_csv(github_csv_url)
    st.success("File loaded successfully from GitHub!")

    # Input for design number
    design_number_input = st.text_input('Enter Design Number', '')

    if design_number_input:
        try:
            design_number = int(design_number_input)
            relevant_df = find_relevant_rows(design_number, df)

            if not relevant_df.empty:
                st.write(f"Results for Design Number {design_number}:")

                # Manually format and display each row to mimic a table with markdown links
                for index, row in relevant_df.iterrows():
                    st.markdown("---") # Separator for each entry
                    st.markdown(f"**Citable Reference:** {row['Citable Reference']}")
                    st.markdown(f"**Context Description:** {row['Context Description']}")
                    st.markdown(f"**Title:** {row['Title']}")
                    st.markdown(f"**Covering Dates:** {row['Covering Dates']}")
                    st.markdown(f"**ID:** {row['ID']}")
                    st.markdown(f"**Discovery link:** [Discovery link](https://discovery.nationalarchives.gov.uk/details/r/{row['ID']})")

            else:
                st.warning(f"Design number {design_number} not found in any range.")
        except ValueError:
            st.error("Please enter a valid integer for the design number.")

except Exception as e:
    st.error(f"Error loading CSV from GitHub: {e}")
    st.info("Please ensure the URL is correct and the file is accessible.")
