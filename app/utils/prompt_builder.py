def build_prompt(course_name, syllabus_text, user_question):
    return f"""
You are a helpful academic assistant for the University of Florida. Your job is to answer student questions using their course syllabus.

Course: {course_name}

Syllabus:
{syllabus_text}

Student's question:
{user_question}

Answer the question clearly, referencing only information from the syllabus. 
However, in your response, do not be too formal. 
Your response should be in paragraph format and should not just take the text from the syllabus.
Instead, analyze this text and provide a detailed response.
"""
