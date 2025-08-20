# 📘 Contact Book using Linked List (2nd Year Level Project)

# === Node Class ===
class ContactNode:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None


# === Contact Book Class ===
class ContactBook:
    def __init__(self):
        self.head = None

    # Insert contact alphabetically
    def insert_contact(self, name, phone, email):
        new_node = ContactNode(name, phone, email)

        if self.head is None or name.lower() < self.head.name.lower():
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.name.lower() < name.lower():
                current = current.next
            new_node.next = current.next
            current.next = new_node
        print("✅ Contact added successfully!")

    # Display all contacts
    def display_contacts(self):
        if self.head is None:
            print("No contacts found.")
            return
        current = self.head
        print("\n--- Contact List ---")
        while current:
            print(f"Name: {current.name}, Phone: {current.phone}, Email: {current.email}")
            current = current.next

    # Search contact by name
    def search_contact(self, name):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                print(f"✅ Found: {current.name}, Phone: {current.phone}, Email: {current.email}")
                return
            current = current.next
        print("❌ Contact not found!")

    # Update contact
    def update_contact(self, name, new_phone, new_email):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                current.phone = new_phone
                current.email = new_email
                print("✅ Contact updated successfully!")
                return
            current = current.next
        print("❌ Contact not found!")

    # Delete contact
    def delete_contact(self, name):
        current = self.head
        prev = None
        while current:
            if current.name.lower() == name.lower():
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print("✅ Contact deleted successfully!")
                return
            prev = current
            current = current.next
        print("❌ Contact not found!")


# === Menu-Driven Program ===
def main():
    book = ContactBook()

    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.insert_contact(name, phone, email)

        elif choice == '2':
            book.display_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            book.search_contact(name)

        elif choice == '4':
            name = input("Enter name to update: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            book.update_contact(name, phone, email)

        elif choice == '5':
            name = input("Enter name to delete: ")
            book.delete_contact(name)

        elif choice == '6':
            print("👋 Exiting Contact Book. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please try again.")


# === Run Program ===
if __name__ == "__main__":
    main()
