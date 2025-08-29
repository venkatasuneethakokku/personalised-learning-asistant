import json
import os

# ----------------------------
# Content: Lessons + Quizzes
# ----------------------------
LESSONS = [
    {
        "title": "Basics of Python",
        "content": "Learn about variables, data types, and basic syntax in Python.",
        "quiz": {
            "question": "Which of these is a valid variable name in Python?\n(a) 1variable\n(b) variable_1\n(c) variable-1\n(d) variable 1",
            "answer": "b"
        }
    },
    {
        "title": "Control Flow",
        "content": "Understand if-else statements, loops, and logical operators.",
        "quiz": {
            "question": "What keyword is used for a conditional branch in Python?\n(a) loop\n(b) if\n(c) switch\n(d) case",
            "answer": "b"
        }
    },
    {
        "title": "Functions",
        "content": "Define and call functions, understand arguments and return values.",
        "quiz": {
            "question": "How do you define a function in Python?\n(a) func myFunction():\n(b) def myFunction():\n(c) function myFunction():\n(d) define myFunction():",
            "answer": "b"
        }
    },
    {
        "title": "Data Structures",
        "content": "Explore lists, tuples, dictionaries, and sets.",
        "quiz": {
            "question": "Which data structure is immutable?\n(a) list\n(b) dictionary\n(c) tuple\n(d) set",
            "answer": "c"
        }
    }
]

# ----------------------------
# User Model
# ----------------------------
class UserModel:
    def __init__(self, username):
        self.username = username
        self.progress_file = f"{username}_progress.json"
        self.progress = self.load_progress()

    def load_progress(self):
        if os.path.exists(self.progress_file):
            with open(self.progress_file, "r") as file:
                return json.load(file)
        else:
            return {"completed": []}

    def save_progress(self):
        with open(self.progress_file, "w") as file:
            json.dump(self.progress, file, indent=4)

    def get_next_topic(self, lessons):
        for lesson in lessons:
            if lesson["title"] not in self.progress["completed"]:
                return lesson
        return None

    def complete_topic(self, title):
        if title not in self.progress["completed"]:
            self.progress["completed"].append(title)
            self.save_progress()

# ----------------------------
# Learning Assistant
# ----------------------------
class LearningAssistant:
    def __init__(self, user):
        self.user = user
        self.lessons = LESSONS

    def run(self):
        print(f"\n👋 Hello {self.user.username.capitalize()}! Welcome back to your learning assistant.\n")

        while True:
            next_topic = self.user.get_next_topic(self.lessons)
            if not next_topic:
                print("🎉 You have completed all lessons! Great job!")
                break

            self.present_lesson(next_topic)
            if self.quiz_user(next_topic["quiz"]):
                self.user.complete_topic(next_topic["title"])
                print("✅ Lesson completed and progress saved.\n")
            else:
                print("⏭️ Lesson skipped. You can retry later.\n")

            cont = input("Do you want to continue to the next lesson? (y/n): ").strip().lower()
            if cont != "y":
                print("Goodbye! See you next time 👋")
                break

    def present_lesson(self, lesson):
        print("="*50)
        print(f"📘 Lesson: {lesson['title']}")
        print("-"*50)
        print(lesson['content'])
        print("="*50)

    def quiz_user(self, quiz):
        print("\n📝 Quiz Time!")
        print(quiz["question"])
        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:
            ans = input("Your answer (a/b/c/d) or type 'skip' to skip: ").strip().lower()
            if ans == "skip":
                return False
            if ans == quiz["answer"]:
                print("🎉 Correct!")
                return True
            else:
                attempts += 1
                print(f"❌ Incorrect. Attempts left: {max_attempts - attempts}")
        print(f"The correct answer was: {quiz['answer']}")
        return False

# ----------------------------
# Main
# ----------------------------
def main():
    print("Welcome to the Personalized Learning Assistant!")
    username = input("Please enter your name: ").strip().lower().replace(" ", "_")
    user = UserModel(username)
    assistant = LearningAssistant(user)
    assistant.run()

if __name__ == "__main__":
    main()
