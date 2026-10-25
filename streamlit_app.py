import streamlit as st
st.title("Student Marks Analyser")
st.write("enter the student's marks and calculate results")
name=st.text_input("enter student's name")
maths=st.number_input("maths marks",min_value=0,max_value=100)
science=st.number_input("science marks",min_value=0,max_value=100)
english=st.number_input("english marks",min_value=0,max_value=100)
if st.button("calculate result:"):
    total=maths+science+english
    percentage=total/3
    st.subheader("Result")
    st.write("Student name:",name)
    st.write("total marks:",total)
    st.write("percentage:",round(percentage,2),"%")
