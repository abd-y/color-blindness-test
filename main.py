import streamlit as st

#making custom vars in the st class
if "list_index" not in st.session_state:
    st.session_state["list_index"] = 0
if "counter" not in st.session_state:
    st.session_state["counter"] = 0

#here are all the image file names
images = ["images/" + str(i) + ".jpg" for i in range(1, 19)]

def true_press():
    '''
    When the correct number is pressed this function will execute
    basically it changes the displayed image by this
    st.session_state["list_index"] += 1
    and it add 1 to the to the counter which is st.session_state["counter"]
    '''
    st.session_state["list_index"] += 1
    st.session_state["counter"] += 1
    if st.session_state["list_index"] == len(images):
        st.session_state["list_index"] = 0

def false_press():
    '''
    When the wrong number is pressed this function will execute
    basically it changes the displayed image by this
    st.session_state["list_index"] += 1
    '''
    st.session_state["list_index"] += 1
    if st.session_state["list_index"] == len(images):
        st.session_state["list_index"] = 0

def main():
    #display a text in the page
    st.title("Color blindness test")
    #adding a custom style for buttons
    st.markdown(
        """
        <style>
        button {
            width: 100px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    #diplay an image in the page from the list "images"
    st.image(images[st.session_state["list_index"]])
    print(st.session_state)
    st.write("Choose the number you see in the image above:")
    #making columns for each button
    col1, col2, col3 = st.columns(3)
    #change the button values when the list_index is changed
    #also each button will call a specific function when it's clicked
    if st.session_state.list_index == 0:
        col1.button("10", on_click=false_press)
        col2.button("13", on_click=false_press)
        col3.button("12", on_click=true_press)
    elif st.session_state.list_index == 1:
        col1.button("8", on_click=true_press)
        col2.button("5", on_click=false_press)
        col3.button("3", on_click=false_press)
    elif st.session_state.list_index == 2:
        col1.button("9", on_click=false_press)
        col2.button("6", on_click=true_press)
        col3.button("5", on_click=false_press)

main()

