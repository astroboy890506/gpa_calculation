import streamlit as st

def calculate_gpa(subjects):
    total_grade_points = 0
    total_credits = 0
    
    for subject in subjects:
        marks = subject['marks']
        credits = subject['credits']
        
        if 80 <= marks <= 100:
            grade_point = 4.00
        elif 70 <= marks <= 79:
            grade_point = 3.67
        elif 60 <= marks <= 69:
            grade_point = 3.33
        elif 55 <= marks <= 59:
            grade_point = 3.00
        elif 50 <= marks <= 54:
            grade_point = 2.67
        elif 45 <= marks <= 49:
            grade_point = 2.33
        elif 40 <= marks <= 44:
            grade_point = 2.00
        elif 35 <= marks <= 39:
            grade_point = 1.67
        elif 30 <= marks <= 34:
            grade_point = 1.33
        elif 25 <= marks <= 29:
            grade_point = 1.00
        else:
            grade_point = 0.00  # Grade F
        
        subject['grade_point'] = grade_point
        total_grade_points += grade_point * credits
        total_credits += credits
    
    if total_credits == 0:
        return 0.00  # Avoid division by zero
    else:
        return round(total_grade_points / total_credits, 2)

def main():
    st.title("GPA Calculator")

    # Create a sidebar for the number of subjects
    num_subjects = st.sidebar.number_input("Enter the number of subjects for the current semester:", min_value=1, value=1, step=1)

    subjects = []

    for i in range(num_subjects):
        st.subheader(f"Subject {i + 1}")
        subject_name = st.text_input(f"Name:")
        marks = st.slider(f"Slide to select marks for {subject_name}:", min_value=0, max_value=100, value=50, step=1)
        credits = st.slider(f"Slide to select credit hours for {subject_name}:", min_value=1, max_value=5, value=1, step=1)
        subjects.append({'name': subject_name, 'marks': marks, 'credits': credits})

        if i < num_subjects - 1:
            st.button("Next Subject")

    if st.button("Calculate GPA"):
        gpa = calculate_gpa(subjects)
        st.markdown(f"<h2>Your GPA for the current semester is: {gpa}</h2>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
