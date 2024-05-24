# import streamlit as st
# import pandas as pd
# import random
# import streamlit.components.v1 as components

# # Function to select a single winner
# def select_winner(participants):
#     winner = random.choice(participants)
#     return winner

# # Display the logo/image
# logo_path = "./Images/iberia-logo.png"
# st.image(logo_path)

# st.title("Iberia Garmin Fenix Watch Raffle Winner")

# # Option to upload an Excel file
# uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx", "xls"])

# if uploaded_file is not None:
#     # Read Excel file and extract names from the 'Name' column
#     df = pd.read_excel(uploaded_file)
#     participants = df["My name is..."].tolist()
# else:
#     # User input for participants
#     participants = st.text_area("Enter participants (one per line):").split("\n")

# # Clean up participants list
# participants = [p.strip() for p in participants if p.strip()]

# # Check if participants list is empty
# if len(participants) == 0:
#     st.warning("Please enter or upload participant names.")
# else:
    
#     # Display the KPI for the total number of unique participants
#     unique_participants = len(set(participants))
#     # st.metric(label="Total  Participants", value=unique_participants)
#     # Make KPI more prominent
#     st.markdown("""
#     <div style='text-align: center;'>
#         <h2>Total Participants</h2>
#         <div style='font-size: 48px; color: #007bff;'>{}</div>
#     </div>
#     """.format(unique_participants), unsafe_allow_html=True)

#     # Display the slot machine HTML
#     slot_machine_html = """
#     <div class="slot-machine">
#       <div class="reel" id="reel1"></div>
#       <div class="reel" id="reel2"></div>
#       <div class="reel" id="reel3"></div>
#     </div>
#     <div id="winner" style="text-align: center; font-size: 24px; margin-top: 20px;"></div>

#     <style>
#     .slot-machine {
#       display: flex;
#       justify-content: center;
#       align-items: center;
#       margin-top: 50px;
#     }

#     .reel {
#       width: 100px;
#       height: 100px;
#       border: 2px solid #000;
#       margin: 0 10px;
#       display: flex;
#       justify-content: center;
#       align-items: center;
#       overflow: hidden;
#       background-color: #f0f0f0;
#       border-radius: 10px;
#     }

#     .slot-item {
#       font-size: 24px;
#       text-align: center;
#       color: #fff;
#       padding: 20px;
#       background-color: #007bff;
#       border-radius: 50%;
#     }
#     </style>

#     <script>
#     function spin(reel, values) {{
#         const reelElement = document.getElementById(reel);
#         reelElement.innerHTML = '';  // Clear previous content

#         // Add spinning effect
#         const spinAnimation = setInterval(() => {{
#             const randomValue = values[Math.floor(Math.random() * values.length)];
#             reelElement.innerHTML = `<div class="slot-item">${{randomValue}}</div>`;
#         }}, 100);

#         // Stop the spinning effect after some time
#         setTimeout(() => {{
#             clearInterval(spinAnimation);
#             const finalValue = "{selected_winner}";
#             reelElement.innerHTML = `<div class="slot-item">${{finalValue}}</div>`;
#         }}, 3000);  // Duration of spin
#     }}

#     function startSlotMachine(participants) {{
#         const values = participants.split(',');

#         spin('reel1', values);
#         spin('reel2', values);
#         spin('reel3', values);

#         setTimeout(() => {{
#             document.getElementById('winner').innerText = `Winner: {selected_winner}`;
#         }}, 3200);  // Duration of spin + some delay for winner announcement
#     }}

#     startSlotMachine("{participants_str}");
#     </script>
#     """

#     # Button to select winner
#     if st.button("Select Winner"):
#         selected_winner = select_winner(participants)

#         # Combine participants into a comma-separated string
#         participants_str = ",".join(participants)

#         # Inject HTML, JS, and CSS for the slot machine
#         components.html(f"""
#         {slot_machine_html}
#         <script>
#         function spin(reel, values) {{
#             const reelElement = document.getElementById(reel);
#             reelElement.innerHTML = '';  // Clear previous content

#             // Add spinning effect
#             const spinAnimation = setInterval(() => {{
#                 const randomValue = values[Math.floor(Math.random() * values.length)];
#                 reelElement.innerHTML = `<div class="slot-item">${{randomValue}}</div>`;
#             }}, 100);

#             // Stop the spinning effect after some time
#             setTimeout(() => {{
#                 clearInterval(spinAnimation);
#                 const finalValue = "{selected_winner}";
#                 reelElement.innerHTML = `<div class="slot-item">${{finalValue}}</div>`;
#             }}, 3000);  // Duration of spin
#         }}

#         function startSlotMachine(participants) {{
#             const values = participants.split(',');

#             spin('reel1', values);
#             spin('reel2', values);
#             spin('reel3', values);

#             setTimeout(() => {{
#                 document.getElementById('winner').innerText = `Winner: {selected_winner}`;
#             }}, 3200);  // Duration of spin + some delay for winner announcement
#         }}

#         startSlotMachine("{participants_str}");
#         </script>
#         <style>
#         .slot-machine {{
#           display: flex;
#           justify-content: center;
#           align-items: center;
#           margin-top: 50px;
#         }}

#         .reel {{
#           width: 200px;
#           height: 100px;
#           border: 2px solid #083f5a;
#           margin: 0 10px;
#           display: flex;
#           justify-content: center;
#           align-items: center;
#           overflow: hidden;
#           background-color: #D3E7FF; /*Outter Color*/
#           border-radius: 10px;
#         }}

#         .slot-item {{
#           font-size: 24px;
#           text-align: center;
#           color: #fff;
#           padding: 20px;
#           background-color: #083f5a; /*Inner Color*/
#           border-radius: 50%;
#         }}
#         </style>
#         """, height=400)



######################
# Version with design
######################



import streamlit as st
import pandas as pd
import random
import streamlit.components.v1 as components

# Function to select a single winner
def select_winner(participants):
    winner = random.choice(participants)
    return winner

    

# Define a two-column layout
col1, spacer, col2 = st.columns([1, .5, 2])

# Watch image in the left column
watch_image_path = "https://iberiaadvisoryllc.box.com/s/kn3drwnrx6xrfpzrtf0vophms9y5ysod"
# PDI image
PDI_image_path = "https://eventpower-res.cloudinary.com/image/upload/c_fit,h_200,w_300/f_auto,q_auto/v1/media/ASMC%20Education%20Department/24asmc-pdi/website_header/t8zobvei74ouzoiquqdv"

with col1:
    st.image(PDI_image_path, use_column_width=True)
    st.image(watch_image_path, use_column_width=True)

# Content in the right column
with col2:
    # Display the logo/image
    logo_path = "./Images/iberia-logo.png"
    st.image(logo_path)

    # Sidebar for file upload
    st.sidebar.header("Upload and Customize")

    # Option to upload an Excel file
    uploaded_file = st.sidebar.file_uploader("Upload Excel File", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read Excel file and extract names from the 'Name' column
        df = pd.read_excel(uploaded_file)
        participants = df["My name is..."].tolist()

        # Clean up participants list
        participants = [p.strip() for p in participants if p.strip()]

        # Check if participants list is empty
        if len(participants) == 0:
            st.warning("The uploaded file does not contain any participant names.")
        else:
            # Display the KPI for the total number of unique participants
            unique_participants = len(set(participants))
            st.markdown("""
            <div style='text-align: center;'>
                <h2>Out of {} participants</h2>
                <h2>The winner of the</h2>
                <h2>Garmin Fenix 6X Pro is…</h2>
            </div>
            """.format(unique_participants), unsafe_allow_html=True)

            # Display the slot machine HTML
            slot_machine_html = """
            <div class="slot-machine">
              <div class="reel" id="reel1"></div>
              <div class="reel" id="reel2"></div>
              <div class="reel" id="reel3"></div>
            </div>
            <div id="winner" style="text-align: center; font-size: 24px; margin-top: 20px;"></div>

            <style>
            .slot-machine {
              display: flex;
              justify-content: center;
              align-items: center;
              margin-top: 50px;
            }

            .reel {
              width: 100px;
              height: 100px;
              border: 2px solid #000;
              margin: 0 10px;
              display: flex;
              justify-content: center;
              align-items: center;
              overflow: hidden;
              background-color: #f0f0f0;
              border-radius: 10px;
            }

            .slot-item {
              font-size: 24px;
              text-align: center;
              color: #fff;
              padding: 20px;
              background-color: #007bff;
              border-radius: 50%;
            }
            </style>

            <script>
            function spin(reel, values) {{
                const reelElement = document.getElementById(reel);
                reelElement.innerHTML = '';  // Clear previous content

                // Add spinning effect
                const spinAnimation = setInterval(() => {{
                    const randomValue = values[Math.floor(Math.random() * values.length)];
                    reelElement.innerHTML = `<div class="slot-item">${{randomValue}}</div>`;
                }}, 100);

                // Stop the spinning effect after some time
                setTimeout(() => {{
                    clearInterval(spinAnimation);
                    const finalValue = "{selected_winner}";
                    reelElement.innerHTML = `<div class="slot-item">${{finalValue}}</div>`;
                }}, 3000);  // Duration of spin
            }}

            function startSlotMachine(participants) {{
                const values = participants.split(',');

                spin('reel1', values);
                spin('reel2', values);
                spin('reel3', values);

                setTimeout(() => {{
                    document.getElementById('winner').innerText = `Winner: {selected_winner}`;
                }}, 3200);  // Duration of spin + some delay for winner announcement
            }}

            startSlotMachine("{participants_str}");
            </script>
            """
            

            
            # Button to select winner
            if st.button("Select Winner", use_container_width=True):
                selected_winner = select_winner(participants)

                # Combine participants into a comma-separated string
                participants_str = ",".join(participants)

                # Inject HTML, JS, and CSS for the slot machine
                components.html(f"""
                {slot_machine_html}
                <script>
                function spin(reel, values) {{
                    const reelElement = document.getElementById(reel);
                    reelElement.innerHTML = '';  // Clear previous content

                    // Add spinning effect
                    const spinAnimation = setInterval(() => {{
                        const randomValue = values[Math.floor(Math.random() * values.length)];
                        reelElement.innerHTML = `<div class="slot-item">${{randomValue}}</div>`;
                    }}, 100);

                    // Stop the spinning effect after some time
                    setTimeout(() => {{
                        clearInterval(spinAnimation);
                        const finalValue = "{selected_winner}";
                        reelElement.innerHTML = `<div class="slot-item">${{finalValue}}</div>`;
                    }}, 3000);  // Duration of spin
                }}

                function startSlotMachine(participants) {{
                    const values = participants.split(',');

                    spin('reel1', values);
                    spin('reel2', values);
                    spin('reel3', values);

                    setTimeout(() => {{
                        document.getElementById('winner').innerText = `Winner: {selected_winner}`;
                    }}, 3200);  // Duration of spin + some delay for winner announcement
                }}

                startSlotMachine("{participants_str}");
                </script>
                <style>
                .slot-machine {{
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  margin-top: 50px;
                }}

                .reel {{
                  width: 200px;
                  height: 100px;
                  border: 2px solid #083f5a;
                  margin: 0 10px;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  overflow: hidden;
                  background-color: #D3E7FF; /*Outter Color*/
                  border-radius: 10px;
                }}

                .slot-item {{
                  font-size: 24px;
                  text-align: center;
                  color: #fff;
                  padding: 20px;
                  background-color: #083f5a; /*Inner Color*/
                  border-radius: 50%;
                }}
                </style>
                """, height=400)

#     else:
#         st.warning("Please upload an Excel file to proceed.")
