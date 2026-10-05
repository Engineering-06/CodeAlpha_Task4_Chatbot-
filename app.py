from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(message):
    message = message.lower().strip()
    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"
    elif "cloud" in message:
        return "Cloud computing means using servers, storage and computing resources through the internet."
    elif "python" in message:
        return "Python is a popular programming language used in web development, AI, automation and data science."
    elif "internship" in message:
        return "Complete your assigned tasks, upload your projects to GitHub and submit the required links."
    elif "thank" in message:
        return "You're welcome!"
    elif "bye" in message:
        return "Goodbye! Have a nice day."
    return "Sorry, I don't understand. Ask me about Cloud, Python or Internship."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    return jsonify({"response": chatbot_response(data.get("message", ""))})

if __name__ == "__main__":
    app.run(debug=True)
