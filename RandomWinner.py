import streamlit as st
import random

def select_winners(participants, num_winners):
    if num_winners > len(participants):
        st.error("Error: Number of winners cannot exceed the number of participants.")
        return []

    winners = random.sample(participants, num_winners)
    return winners


st.title("Random Winners Selector App")

# User input for participants
participants = st.text_area("Enter participants (one per line):").split("\n")

# User input for number of winners
num_winners = st.number_input("Number of winners:", min_value=1, max_value=len(participants), value=1)

# Button to select winners
if st.button("Select Winners"):
    selected_winners = select_winners(participants, num_winners)

    # Display the selected winners
    st.success("Selected Winners:")
    for winner in selected_winners:
        st.write(winner)
