from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Chatbot API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    # Simple response logic (Replace with actual AI response)
    bot_response = f"You said: {user_message}"

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
