##  we will create a marks header and store the marks there and print them.


#import sunsketch and sunlite

from sunlite.db import connect
from sunsketch import sun


#connect to database

db = connect("students")
db.new("marks")

#lets push some datas

name = "Allan"

marks = '{"maths":50 , "english":45 , "science":60}'

db.push(name,marks)

#lets push another

name = "Kimmie"

marks = '{"maths":48 , "english":47 , "science":70}'

db.push(name,marks)

#lets try pulling them out now and print in a desktop window.

line = str(db.pull("marks"))

sun.draw(line,weight="bold",color=["white","red"])