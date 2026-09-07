from pymongo import MongoClient


client = MongoClient("<MongoDB Atlas connection string>")
db = client["college"]
students = db["students"]


while True:

    print("\n--- Student Database ---")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # CREATE
    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")

        result = students.insert_one({
            "name": name,
            "age": age,
            "email": email
        })

        print("Student inserted:", result.inserted_id)

    # READ
    elif choice == "2":
        print("\nStudents:")

        for student in students.find():
            print(student)

    # UPDATE
    elif choice == "3":
        name = input("Enter name to update: ")
        email = input("Enter new email: ")

        result = students.update_one(
            {"name": name},
            {"$set": {"email": email}}
        )

        if result.matched_count > 0:
            print("Student updated.")

            student = students.find_one({"name": name})
            print(student)
        else:
            print("Student not found.")

    # DELETE
    elif choice == "4":
        name = input("Enter name to delete: ")

        result = students.delete_one({"name": name})

        if result.deleted_count > 0:
            print("Student deleted.")
        else:
            print("Student not found.")

    # EXIT
    elif choice == "5":
        break

    else:
        print("Invalid choice.")

client.close()