# UF Study Buddy

## Overview
The UF Study Buddy was created to help University of Florida students quickly find important course information by using actual UF syllabi as data. Instead of having to dig through PDF syllabi to find dates, policies, grading breakdowns, or even study resources, simply select your major and class from the dropdown menus, then type your question to recieve an AI-powered answer. 

The tool was created to make it easier for students to access relevant syllabus details. Whether you want study tips, content explanations, policy clarifications, or grading details, the AI will answer using information pulled directly from the real course syllabi.

Although this program was designed for UF students, others can use it with their own syllabi and API keys.

## Technology Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript

## Installation Directions
To use the *UF Study Buddy*, follow these directions:

**1. Clone the Repository:**

    git clone https://github.com/yourusername/uf-study-buddy.git
    cd uf-study-buddy


**2. Create a Virtual Environment:**

    python -m venv venv

**3. Activate the Virtual Environment:**

- On Windows:

         venv\Scripts\activate 
- On macOS/Linux:

        source venv/bin/activate

**4. Install Dependencies:**

    pip install -r requirements.txt

**5. Get your API key:**
- If you are a UF student:
    - Go to the Navigator Toolkit at https://ai.it.ufl.edu/navigator/
    - Sign in with your GatorLink credentials
    - Generate your free API key
    - The base URL for Navigator is:
```
https://api.ai.it.ufl.edu/
```
- If you are NOT a UF student:
    - You can use an OpenAI API key from https://platform.openai.com/
    - Your base URL will be:
```
https://api.openai.com/v1
```
**6. Update key.json and openai_config.py:**

- In the root folder of this project, there is already a file called key.json. Open it and replace the placeholders with your generated API key and the base URL. If you are a UF student using Navigator, replace the base URL with https://api.ai.it.ufl.edu/. If you are an external user, change it to the correct base URL for your provider.

- Inside openai_config.py, find this line:
```python
key_file = r"your_file_path"
```
- Replace "your_file_path" with the absolute path to the key.json file in your project folder.

  - Example:
```python
key_file = r"C:\Users\YourName\Documents\uf-study-buddy\key.json"
```
**7. Run the Program:**

- Once everything is set up, start the Flask app by running:

```bash
python app.py
```
- Then, open your browser and go to:
```
http://127.0.0.1:5000
```
## License 
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. The MIT License is a permissive license that allows reuse with minimal restrictions, making it ideal for open-source projects.
