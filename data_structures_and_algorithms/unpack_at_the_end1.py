record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# *phone_numbers will always be a list.
name, email, *phone_numbers = record

print(phone_numbers)
