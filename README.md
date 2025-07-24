# Design Number Lookup App
This is a simple Streamlit web application designed to look up information based on a given registered design number within a dataset of The National Archives' catalogue data (covering registered designs - BT records) provided in a CSV file. The app searches for design numbers within ranges specified in the 'Description' column and retrieves relevant information from the corresponding rows.

Features
* Input a design number to search for.
* Displays 'Citable Reference', 'Context Description', 'Title', and 'Covering Dates' for matching entries.
* Handles cases where the design number is not found in any range.
* Includes error handling for file loading and invalid input.
