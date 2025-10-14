import sqlite3
from langchain.prompts import PromptTemplate
from langchain.chat_models import init_chat_model

db_path = r"./sqlite/courses.db"

def get_courses():
    # Use DBAPI
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    conn.close()
    return courses  # List[Tuple]

def concate_course(course):
    course_id, title, description, duration, fee, prerequisite = course
    return f"Title: {title}\nDescription: {description}\nFee: {fee}\nDuration: {duration}\nPrerequisite: {prerequisite}"

# Load courses data
courses = get_courses()

context = ""
for course in courses:
    context += concate_course(course) + "\n\n"

#print(context)

prompt_template_str = """
Answer the question based on the given context. 
Context : {context}
Question: {question}
"""

prompt_template = PromptTemplate.from_template(prompt_template_str)
prompt = prompt_template.format(context=context, 
                question="What is the fee for DataScience course?")

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

result = llm.invoke(prompt)
print(result.content)
 













 