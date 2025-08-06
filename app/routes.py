from flask import Blueprint, render_template, request
from app.utils.syllabus_parser import extract_text_from_pdf
from app.utils.prompt_builder import build_prompt
from app.utils.openai_config import configure_openai
import os

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        course_code = request.form["course"]
        user_question = request.form["question"]

        pdf_filename = f"{course_code}_Spring_2025.pdf"
        pdf_path = os.path.join("app", "syllabi", pdf_filename)

        if not os.path.exists(pdf_path):
            response = "Sorry, syllabus not found."
        else:
            syllabus_text = extract_text_from_pdf(pdf_path)
            prompt = build_prompt(course_code, syllabus_text, user_question)
            response = call_llm(prompt)

    return render_template("index.html", response=response)

def call_llm(prompt):
    client = configure_openai()

    response = client.chat.completions.create(
        model="llama-3.1-70b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    return response.choices[0].message.content




