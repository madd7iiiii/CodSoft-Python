import tkinter as tk
from tkinter import ttk, messagebox
import json


class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        # GUI Elements
        self.name_label = ttk.Label(root, text="Name:")
        self.name_entry = ttk.Entry(root)
        self.phone_label = ttk.Label(root, text="Phone Number:")
        self.phone_entry = ttk.Entry(root)

        self.add_button = ttk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = ttk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = ttk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = ttk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = ttk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Place GUI elements on the grid
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)
        self.search_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.update_button.grid(row=5, column=0, columnspan=2, pady=5)
        self.delete_button.grid(row=6, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            contact = {"name": name, "phone": phone}
            self.contacts.append(contact)
            self.save_contacts()
            self.clear_entries()
            self.show_message("Contact Added", f"{name} has been added to the contacts.")
        else:
            self.show_message("Error", "Please enter both name and phone number.")

    def view_contacts(self):
        if not self.contacts:
            self.show_message("No Contacts", "There are no contacts to display.")
            return

        contact_list = "\n".join([f"{contact['name']}: {contact['phone']}" for contact in self.contacts])
        self.show_message("Contact List", contact_list)

    def search_contact(self):
        search_query = self.name_entry.get()
        if not search_query:
            self.show_message("Error", "Please enter a name for searching.")
            return

        found_contacts = [contact for contact in self.contacts if search_query.lower() in contact['name'].lower()]
        if found_contacts:
            contact_list = "\n".join([f"{contact['name']}: {contact['phone']}" for contact in found_contacts])
            self.show_message("Search Results", contact_list)
        else:
            self.show_message("Not Found", f"No contacts found with the name '{search_query}'.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name:
            for contact in self.contacts:
                if contact['name'].lower() == name.lower():
                    contact['phone'] = phone
                    self.clear_entries()
                    self.show_message("Contact Updated", f"{name}'s contact information has been updated.")
                    return

            self.show_message("Not Found", f"No contact found with the name '{name}'.")
        else:
            self.show_message("Error", "Please enter a name for updating contact information.")

    def delete_contact(self):
        name = self.name_entry.get()

        if name:
            for contact in self.contacts:
                if contact['name'].lower() == name.lower():
                    self.contacts.remove(contact)
                    self.clear_entries()
                    self.show_message("Contact Deleted", f"{name}'s contact has been deleted.")
                    return

            self.show_message("Not Found", f"No contact found with the name '{name}'.")
        else:
            self.show_message("Error", "Please enter a name for deleting contact.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            # Create the file if it doesn't exist
            with open("contacts.json", "w") as file:
                json.dump([], file)
                
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
