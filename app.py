import os
from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    question = None
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a helpful homework assistant for a student. Explain things clearly and in a friendly way."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content
    return render_template("index.html", answer=answer, question=question)

if __name__ == "__main__":
    app.run(debug=True)
