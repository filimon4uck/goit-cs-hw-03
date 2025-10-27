import argparse
from database import get_collection

collection = get_collection()


def create_cat(name, age, features):
    features_list = [f.strip() for f in features.split(",")]
    cat = {"name": name, "age": age, "features": features_list}
    result = collection.insert_one(cat)
    print(f"Кота {name} додано з _id: {result.inserted_id}")


def read_all_cats():
    cats = list(collection.find())
    for cat in cats:
        print(cat)


def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Кота не знайдено.")


def update_cat_age(name, age):
    result = collection.update_one({"name": name}, {"$set": {"age": age}})
    print("Вік оновлено." if result.matched_count else "Кота не знайдено.")


def add_feature(name, feature):
    result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
    print("Характеристика додана." if result.matched_count else "Кота не знайдено.")


def delete_cat(name):
    result = collection.delete_one({"name": name})
    print("Кота видалено." if result.deleted_count else "Кота не знайдено.")


def delete_all_cats():
    result = collection.delete_many({})
    print(f"Видалено {result.deleted_count} котів.")


def main():
    parser = argparse.ArgumentParser(description="CRUD для колекції котів")
    subparsers = parser.add_subparsers(dest="command")

    # create
    parser_create = subparsers.add_parser("create")
    parser_create.add_argument("--name", required=True)
    parser_create.add_argument("--age", type=int, required=True)
    parser_create.add_argument("--features", required=True)

    # read
    parser_read = subparsers.add_parser("read")
    parser_read.add_argument("--name", required=False)

    # update-age
    parser_update_age = subparsers.add_parser("update-age")
    parser_update_age.add_argument("--name", required=True)
    parser_update_age.add_argument("--age", type=int, required=True)

    # add-feature
    parser_add_feature = subparsers.add_parser("add-feature")
    parser_add_feature.add_argument("--name", required=True)
    parser_add_feature.add_argument("--feature", required=True)

    # delete
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("--name", required=True)

    # delete-all
    subparsers.add_parser("delete-all")

    args = parser.parse_args()

    match args.command:
        case "create":
            create_cat(args.name, args.age, args.features)
        case "read":
            if args.name:
                read_cat_by_name(args.name)
            else:
                read_all_cats()
        case "update-age":
            update_cat_age(args.name, args.age)
        case "add-feature":
            add_feature(args.name, args.feature)
        case "delete":
            delete_cat(args.name)
        case "delete-all":
            delete_all_cats()
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()


# Example usages:
# python main.py create --name Barsik --age 3 --features "ходить в капці,дає себе гладити"
# python main.py read --name Barsik
# python main.py update-age --name Barsik --age 4
# python main.py add-feature --name Barsik --feature "любить їсти рибу"
# python main.py delete --name Barsik
# python main.py delete-all
