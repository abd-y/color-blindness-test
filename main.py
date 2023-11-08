import streamlit as st
from pyswip import Prolog

#making custom vars in the st class
if "list_index" not in st.session_state:
    st.session_state["list_index"] = 0
if "score" not in st.session_state:
    st.session_state["score"] = 1
if "p_score" not in st.session_state:
    st.session_state["p_score"] = 0
if "d_score" not in st.session_state:
    st.session_state["d_score"] = 0
if "result" not in st.session_state:
    st.session_state["result"] = ''

#getting all images names into a list
images = ["images/" + str(i) + ".jpg" for i in range(1, 19)]

def check_answer(answer):

    prolog = Prolog()
    prolog.consult("logic.pl")

    correct_answer = bool(list(prolog.query(f"answer(plate{st.session_state.list_index + 1}, {answer})")))
    if correct_answer:
        st.session_state["list_index"] += 1
        st.session_state["score"] += 1
    else:
        st.session_state["list_index"] += 1

    if st.session_state["list_index"] == len(images):
        p_score = st.session_state["p_score"]
        d_score = st.session_state["d_score"]

        if  (p_score == d_score) and st.session_state.list_index > 11 :
            st.session_state.result = " We recommend you, to check in with ophthalmologist."
        elif st.session_state["p_score"] > st.session_state["d_score"]:
            st.session_state.result = "You have Protanopia."
        elif st.session_state["p_score"] < st.session_state["d_score"]:
            st.session_state.result = "You have Deuteranopia."

def check_color_blind_type(answer):

    #connecting to prolog
    prolog = Prolog()
    prolog.consult("logic.pl")

    correct_answer = bool(list(prolog.query(f"answer(plate{st.session_state.list_index + 1}, {answer})")))
    if correct_answer:
        check_answer(answer)
    else:
        has_protanopia = bool(list(prolog.query(f"protanopia(answer(plate{st.session_state.list_index + 1}, {answer}))")))
        has_deuteranopia = bool(list(prolog.query(f"deuteranopia(answer(plate{st.session_state.list_index + 1}, {answer}))")))
        print(f"has_protanopia: {has_protanopia} has_deuteranopia: {has_deuteranopia}",)
        if has_protanopia:
            st.session_state["p_score"] += 1
        elif has_deuteranopia:
            print(has_deuteranopia)
            st.session_state["d_score"] += 1

        st.session_state["list_index"] += 1

        if st.session_state["list_index"] == len(images):

            p_score = st.session_state["p_score"]
            d_score = st.session_state["d_score"]
            
            if p_score == d_score:
                st.session_state.result = " We recommend you, to check in with ophthalmologist."
            elif p_score > d_score:
                st.session_state.result = "You have Protanopia."
            elif p_score < d_score:
                st.session_state.result = "You have Deuteranopia."

def display():
    #display page content
    #display a text in the page
        st.title("Color blindness test")
        #adding a custom style for buttons
        #inside the markdown function there is a html code
        st.markdown(
            """
            <style>
            button {
                width: 100px !important;
            },
            </style>
            """,
            unsafe_allow_html=True,
        )
        #diplay an image in the page from the list "images"
        #the bellow statment is to make the image in the middle of the page
        _, cl, _, _ = st.columns(4)
        if st.session_state["list_index"] < len(images): #18 plates.
            #stop going to the next image when the score is more than or equal 12
            if st.session_state["list_index"] == 12 and st.session_state["score"] >= 12:
                cl.image(images[11], width=250)
            elif st.session_state["list_index"] == 13 and st.session_state["score"] >= 12:
                cl.image(images[12], width=250)
            elif st.session_state["list_index"] == 14 and st.session_state["score"] >= 12:
                cl.image(images[13], width=250)
            else:
                cl.image(images[st.session_state["list_index"]], width=250)#continue
        else:
            cl.image(images[len(images) - 1], width=250)
        print(st.session_state)
        st.write("Choose the number you see in the image above:")
        #divide buttons into 3 columns
        return st.columns(3)

def reset():
    '''
    reset screen and start again
    '''
    st.session_state["list_index"] = 0
    st.session_state["score"] = 1
    st.session_state["p_score"] = 0
    st.session_state["d_score"] = 0
    st.session_state["result"] = ''






def end(message):
    st.session_state.result = message
    st.markdown(f'<p style="color: red; text-align: center; font-weight: bold; font-size: 24px;">{st.session_state.result}</p></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    st.button("Try again", on_click=reset)


def main():
    col1, col2, col3 = display()
    #change the button values when the list_index is changed
    #also each button will call a specific function when it's clicked
    if st.session_state.list_index == 0:
        col1.button("10", on_click=check_answer, args=(10,))
        col2.button("13", on_click=check_answer, args=(13,))
        col3.button("12", on_click=check_answer, args=(12,))
    elif st.session_state.list_index == 1:
        col1.button("8", on_click=check_answer, args=(8,))
        col2.button("5", on_click=check_answer, args=(5,))
        col3.button("3", on_click=check_answer, args=(3,))
    elif st.session_state.list_index == 2:
        col1.button("9", on_click=check_answer, args=(9,))
        col2.button("6", on_click=check_answer, args=(6,))
        col3.button("5", on_click=check_answer, args=(5,))
    elif st.session_state.list_index == 3:
        col1.button("70", on_click=check_answer, args=(70,))
        col2.button("26", on_click=check_answer, args=(26,))
        col3.button("29", on_click=check_answer, args=(29,))
    elif st.session_state.list_index == 4:
        col1.button("2", on_click=check_answer, args=(2,))
        col2.button("5", on_click=check_answer, args=(5,))
        col3.button("7", on_click=check_answer, args=(7,))
    elif st.session_state.list_index == 5:
        col1.button("9", on_click=check_answer, args=(9,))
        col2.button("3", on_click=check_answer, args=(3,))
        col3.button("5", on_click=check_answer, args=(5,))
    elif st.session_state.list_index == 6:
        col1.button("15", on_click=check_answer, args=(15,))
        col2.button("11", on_click=check_answer, args=(11,))
        col3.button("17", on_click=check_answer, args=(17,))
    elif st.session_state.list_index == 7:
        col1.button("9", on_click=check_answer, args=(9,))
        col2.button("6", on_click=check_answer, args=(6,))
        col3.button("2", on_click=check_answer, args=(2,))
    elif st.session_state.list_index == 8:
        col1.button("3", on_click=check_answer, args=(3,))
        col2.button("2", on_click=check_answer, args=(2,))
        col3.button("6", on_click=check_answer, args=(6,))
    elif st.session_state.list_index == 9:
        col1.button("75", on_click=check_answer, args=(75,))
        col2.button("55", on_click=check_answer, args=(55,))
        col3.button("97", on_click=check_answer, args=(97,))
    elif st.session_state.list_index == 10:
        col1.button("9", on_click=check_answer, args=(9,))
        col2.button("6", on_click=check_answer, args=(6,))
        col3.button("5", on_click=check_answer, args=(5,))
    elif st.session_state.list_index == 11:
        col1.button("7", on_click=check_answer, args=(7,))
        col2.button("2", on_click=check_answer, args=(2,))
        col3.button("9", on_click=check_answer, args=(9,))
    elif st.session_state.list_index == 12 and st.session_state.score < 12:
        col1.button("5", on_click=check_answer, args=(5,))
        col2.button("2", on_click=check_answer, args=(2,))
        col3.button("nothing", on_click=check_answer, args=("nothing",))
    elif st.session_state.list_index == 12 and st.session_state.score >= 12: #normal color vision.
        end("You're not color blind.")
    elif st.session_state.list_index == 13 and st.session_state.score < 12:
        col1.button("7", on_click=check_answer, args=(7,))
        col2.button("2", on_click=check_answer, args=(2,))
        col3.button("nothing", on_click=check_answer, args=("nothing",))
    elif st.session_state.list_index == 13 and st.session_state.score >= 12:
        end("You're not color blind.")
    elif st.session_state.list_index == 14 and st.session_state.score >= 12:
        end("You're not color blind.")
    #continue the test to diagonose what type of color blind if the score < 12
    elif st.session_state.list_index == 14 and st.session_state.score < 12:
        col1.button("26", on_click=check_color_blind_type, args=(26,))
        col2.button("6", on_click=check_color_blind_type, args=(6,))
        col3.button("2", on_click=check_color_blind_type, args=(2,))
    elif st.session_state.list_index == 15:
        col1.button("2", on_click=check_color_blind_type, args=(2,))
        col2.button("42", on_click=check_color_blind_type, args=(42,))
        col3.button("4", on_click=check_color_blind_type, args=(4,))
    elif st.session_state.list_index == 16:
        col1.button("5", on_click=check_color_blind_type, args=(5,))
        col2.button("3", on_click=check_color_blind_type, args=(3,))
        col3.button("35", on_click=check_color_blind_type, args=(35,))
    elif st.session_state.list_index == 17:
        col1.button("96", on_click=check_color_blind_type, args=(96,))
        col2.button("6", on_click=check_color_blind_type, args=(6,))
        col3.button("9", on_click=check_color_blind_type, args=(9,))
    elif st.session_state.list_index > 17:
        st.markdown(f"<p style='color:red; text-align:center; font-weight:bold; font-size:24px;'>{st.session_state.result}</p>", unsafe_allow_html=True)
        st.button("try again", on_click=reset)

main()