from database import get_cursor
from create_tables import create_tables
from seed import seed
from select_data import select
from queries import queries


def main():
    with get_cursor() as cursor:
        create_tables(cursor)
        seed(cursor)
        print("Starting select values...\n")
        for entry in queries.items():
            print(f"{entry[0]}\nQuery: {entry[1]}\n")
            print("Results:")
            results = select(cursor, entry[1])
            for row in results:
                print(row, "\n")
            print("\n")


if __name__ == "__main__":
    main()
