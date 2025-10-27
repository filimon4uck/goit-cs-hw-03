from faker import Faker


def seed(cursor):
    fake = Faker()
    # Add users
    for _ in range(20):
        fullname = fake.name()
        email = fake.unique.email()
        cursor.execute(
            "INSERT INTO users (fullname, email) VALUES (%s, %s);",
            (fullname, email),
        )
    # Add statuses
    statuses = ["To Do", "In Progress", "Completed", "Cancelled"]
    for status in statuses:
        cursor.execute(
            "INSERT INTO status (name) VALUES (%s);",
            (status,),
        )
    # Add tasks
    for _ in range(6):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=200)
        status_id = fake.random_int(min=1, max=len(statuses))
        user_id = fake.random_int(min=1, max=20)
        cursor.execute(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
            (title, description, status_id, user_id),
        )
    print("Database seeded successfully.\n")
