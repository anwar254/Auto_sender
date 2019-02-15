import json

class Auto_scheduler(object):
    """THis file will get the list of contacts and the message to be sent"""
    def __init__(self, contacts, message):
        self.contacts = contacts

    def get_contacts(self):
        with open(self.contacts, 'r', encoding="utf-8") as contacts:
        	json_data = json.load(contacts)
        	contact_list = []
        	for key in json_data:
        		names = key
        		emails = json_data[key]
        		contact_list.append([names, emails])
        return contact_list

    def get_message(self):
        print("you got the message")

auto_scheduler = Auto_scheduler('contacts.json', 'message.txt')
