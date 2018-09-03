
#import sunlite

from sunlite.db import connect

db = connect("user")


def add_user(name,age,phone,mail):
    #create a header with the name
    db.new(name)
    db.push("age",age)
    db.push("phone",phone)
    db.push("mail",mail)
    return True

def find_all_data(name):
    return db.pull(name)

def find_specific_data(data):
    return db.pull(data)

def update_data(name,data):
    return db.push(name,data)

print("Enter Command :")
while True:
    o = input(">> ")
    print(eval(o))

