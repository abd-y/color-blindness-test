import streamlit as st

#making custom vars in the st class
if "list_index" not in st.session_state:
    st.session_state["list_index"] = 0
if "counter" not in st.session_state:
    st.session_state["counter"] = 1

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

def is_color_blind(counter):
    #here is some code for the connection with prolog
    #not completed
    print(st.session_state["counter"])

def color_blind_type(image_index, answer):
    #here is some code for the connection with prolog
    #prolog will diagonose what type of color blind from the image index and the answer
    pass


def main():
    '''
    suggestion: instead of counting the right answers here
    we can make prolog count the answer if it's possible
    '''
    if st.session_state.list_index < 14:
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
        elif st.session_state.list_index == 3:
            col1.button("70", on_click=false_press)
            col2.button("26", on_click=false_press)
            col3.button("29", on_click=true_press)
        elif st.session_state.list_index == 4:
            col1.button("2", on_click=false_press)
            col2.button("5", on_click=true_press)
            col3.button("7", on_click=false_press)
        elif st.session_state.list_index == 5:
            col1.button("9", on_click=false_press)
            col2.button("3", on_click=true_press)
            col3.button("5", on_click=false_press)
        elif st.session_state.list_index == 6:
            col1.button("15", on_click=true_press)
            col2.button("11", on_click=false_press)
            col3.button("17", on_click=false_press)
        elif st.session_state.list_index == 7:
            col1.button("9", on_click=false_press)
            col2.button("6", on_click=true_press)
            col3.button("2", on_click=false_press)
        elif st.session_state.list_index == 8:
            col1.button("3", on_click=false_press)
            col2.button("2", on_click=false_press)
            col3.button("6", on_click=true_press)
        elif st.session_state.list_index == 9:
            col1.button("75", on_click=false_press)
            col2.button("55", on_click=false_press)
            col3.button("97", on_click=true_press)
        elif st.session_state.list_index == 10:
            col1.button("9", on_click=false_press)
            col2.button("6", on_click=false_press)
            col3.button("5", on_click=true_press)
        elif st.session_state.list_index == 11:
            col1.button("7", on_click=true_press)
            col2.button("2", on_click=false_press)
            col3.button("9", on_click=false_press)
        elif st.session_state.list_index == 12:
            col1.button("5", on_click=false_press)
            col2.button("2", on_click=false_press)
            col3.button("nothing", on_click=true_press)
        elif st.session_state.list_index == 13:
            col1.button("7", on_click=false_press)
            col2.button("2", on_click=false_press)
            col3.button("nothing", on_click=true_press)
    else:
        is_color_blind(st.session_state.counter)

main()

