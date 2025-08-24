import json
from recommender import recommend_content


def save_user(user_data):
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    users.append(user_data)
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)


def main():
    print("\n🎓 Personalized Learning Assistant\n")

    name = input("Enter your name: ")
    goal = input("What do you want to learn? (e.g., Python): ")
    level = input("Your level? (beginner/intermediate): ")
    daily_time = input("Study time per day (in minutes): ")
    preference = input("Preferred format? (video/reading): ")

    user_input = {
        "name": name,
        "goal": goal,
        "level": level.lower(),
        "daily_time": daily_time,
        "preference": preference.lower()
    }

    save_user(user_input)

    print("\n📚 Recommended content for you:\n")
    recommendations = recommend_content(user_input)

    for item in recommendations:
        print(f"✅ {item['title']} — {item['format']} ({item['level']})")

    print("\n✅ Happy Learning!")


if __name__ == "__main__":
    main()
