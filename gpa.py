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
    num_subjects = st.number_input("Enter the number of subjects for the current semester:", min_value=1, value=1, step=1)
    subjects = []

    for i in range(num_subjects):
        subject_name = st.text_input(f"Enter the name of subject {i + 1}:")
        marks = st.slider(f"Enter the marks for {subject_name}:", min_value=0, max_value=100, value=50, step=1)
        credits = st.number_input(f"Enter the credit hours for {subject_name}:", min_value=1, value=1, step=1)
        subjects.append({'name': subject_name, 'marks': marks, 'credits': credits})

    if st.button("Calculate GPA"):
        gpa = calculate_gpa(subjects)
        st.write(f"Your GPA for the current semester is: {gpa}")

if __name__ == "__main__":
    main()
