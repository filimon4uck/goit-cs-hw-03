# All sql queries for the task management system
queries = {
    "1. Отримати всі завдання певного користувача": "SELECT * FROM tasks WHERE user_id = 1;",
    "2. Вибрати завдання за певним статусом": "SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'Completed');",
    "3. Оновити статус конкретного завдання": "UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'In Progress') WHERE id = 1 RETURNING *;",
    "4. Отримати список користувачів без завдань": "SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);",
    "5. Додати нове завдання": "INSERT INTO tasks (title, description, status_id, user_id) VALUES ('New task','This is a new task', 1, 2) RETURNING *;",
    "6. Завдання, які ще не завершено": "SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'Completed');",
    "7. Видалити завдання": "DELETE FROM tasks WHERE id = 6 RETURNING *;",
    "8. Знайти користувачів за поштою": "SELECT * FROM users WHERE email LIKE '%@example.org';",
    "9. Оновити ім’я користувача": "UPDATE users SET fullname = 'Updated Name' WHERE id = 3 RETURNING *;",
    "10. Кількість завдань для кожного статусу": """
        SELECT s.name, COUNT(t.id)
        FROM status s
        LEFT JOIN tasks t ON s.id = t.status_id
        GROUP BY s.name;
        """,
    "11. Завдання користувачів із певним доменом": """
        SELECT t.* FROM tasks t
        JOIN users u ON t.user_id = u.id
        WHERE u.email LIKE '%@example.com';
        """,
    "12. Завдання без опису": "UPDATE tasks SET description = null WHERE id = 2;"
    "SELECT * FROM tasks WHERE description IS NULL;",
    "13. Користувачі та їхні завдання у статусі 'In Progress'": """
        SELECT u.fullname, t.title
        FROM users u
        JOIN tasks t ON u.id = t.user_id
        JOIN status s ON t.status_id = s.id
        WHERE s.name = 'In Progress';
        """,
    "14. Користувачі та кількість їхніх завдань": """
        SELECT u.fullname, COUNT(t.id)
        FROM users u
        LEFT JOIN tasks t ON u.id = t.user_id
        GROUP BY u.fullname;
        """,
}
