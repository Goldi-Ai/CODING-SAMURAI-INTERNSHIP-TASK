from flask import Flask, render_template, request, jsonify
import random
import re

app = Flask(__name__)

class RuleBot:
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_question = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does Earth have a leader?"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_intellipaat': r'.*\s*intellipaat.*'
        }

    def match_reply(self, reply):
        for intent, pattern in self.alienbabble.items():
            if re.match(pattern, reply):
                return getattr(self, intent)()
        return self.no_match_intent()

    def describe_planet_intent(self):
        return random.choice([
            "My planet is a utopia of diverse organisms.",
            "I heard the coffee is good."
        ])

    def answer_why_intent(self):
        return random.choice([
            "I come in peace.",
            "I am here to collect data on your planet and its inhabitants.",
            "I heard the coffee is good."
        ])

    def about_intellipaat(self):
        return random.choice([
            "Intellipaat is the world's largest professional education company.",
            "Intellipaat helps you learn concepts like never before.",
            "Intellipaat helps your career and skills grow."
        ])

    def no_match_intent(self):
        return random.choice([
            "Please tell me more.",
            "Tell me more!",
            "I see. Can you elaborate?",
            "Interesting. Can you tell me more?",
            "I see. How do you think?",
            "Why?",
            "How do you think I feel when I say that? Why?"
        ])

bot = RuleBot()

@app.route("/")
def home():
    return render_template("index.html", question=random.choice(bot.random_question))

@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form["msg"].lower()
    if user_input in bot.exit_commands:
        return jsonify({"response": "Have a nice day 👋"})
    else:
        return jsonify({"response": bot.match_reply(user_input)})

if __name__ == "__main__":
    app.run(debug=True)
