class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print(f"Username: {self.username}, Email: {self.email}")


class Database:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if isinstance(user, User):
            self.users.append(user)
            print(f"User {user.username} added.")
        else:
            print("Invalid user object.")

    def get_all_users(self):
        return self.users


class UserService:
    def __init__(self, db):
        self.db = db

    def register_user(self, username, email):
        new_user = User(username, email)
        self.db.add_user(new_user)

    def list_users(self):
        for user in self.db.get_all_users():
            user.display_info()

    def delete_user(self, username):
        for user in self.db.get_all_users():
            if user.username == username:
                self.db.users.remove(user)
                print(f"User {username} deleted.")
                return
        print(f"User {username} not found.")


class ReportGenerator:
    def __init__(self, db):
        self.db = db

    def generate_user_report(self):
        if len(self.db.get_all_users()) == 0:
            print("No users found.")
            return

        print("User Report:")
        for user in self.db.get_all_users():
            user.display_info()

        # Cyclomatic complexity is high due to multiple decision points
        if len(self.db.get_all_users()) > 5:
            print("A lot of users.")
        else:
            print("Few users.")


def main():
    # Coupling issues, tightly coupled classes
    db = Database()
    user_service = UserService(db)
    report_generator = ReportGenerator(db)

    user_service.register_user("alice", "alice@example.com")
    user_service.register_user("bob", "bob@example.com")
    user_service.register_user("charlie", "charlie@example.com")
    user_service.register_user("dave", "dave@example.com")
    user_service.register_user("eve", "eve@example.com")
    user_service.register_user("frank", "frank@example.com")

    user_service.list_users()
    report_generator.generate_user_report()

    user_service.delete_user("charlie")
    user_service.list_users()


# Poor modularity: the main function does too much and is tightly coupled
# to UserService and ReportGenerator.
main()
