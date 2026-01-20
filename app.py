from flask import Flask, render_template, request, jsonify
from model.chatbot_logic import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chatbot")
def chatbot_page():
    return render_template("chatbot.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    bot_reply = get_response(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
