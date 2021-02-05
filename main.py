# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    # Use a breakpoint in the code line below to debug your script.
    return render_template("index.html") # Press Ctrl+F8 to toggle the breakpoint.

@app.route('/upload', methods = ["GET","POST"])
def upload():
    if request.method=="POST":
        for file in request.files.getlist('file'):
        #file = request.files["file"]
            file.save(os.path.join("static",file.filename))
        return  render_template("upload.html", message = "File uploaded successfully")
    return render_template("upload.html")


@app.route('/retrieve', methods = ["GET","POST"])
def retrieve():
    if request.method == "POST":
        name = request.form.get('name')
        temp = 0
        with open('static/people.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for l in csv_reader:
                if l[0] == name:
                    img_name = l[5]
                    temp = 1
        if temp != 0:
            return render_template("retrieve.html",message = img_name, var = temp)
        else:
            return render_template("retrieve.html", var = temp)
    return render_template("retrieve.html")


@app.route('/update', methods = ["GET","POST"])
def update():
    if request.method == "POST":
        name = request.form.get('name')
        temp = 0
        val = 0
        with open('static/people.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for l in csv_reader:
                temp = temp + 1
                if l[0] == name:
                    row = temp
                    val = 1
                    msg = l
                    #print(msg)
                    break
        if val != 0:
            return render_template("update.html", message = msg, var = val, row = row)
        else:
            return render_template("update.html", message = "User not found", var = val)

    #else:
        #return render_template("update.html", var=val)
    #return render_template("update.html")
    return render_template("update.html")

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == "POST":

        name = request.form.get('name1')
        state = request.form.get('state')
        grade = request.form.get('grade')
        room = request.form.get('room')
        telnum = request.form.get('telnum')
        pic = request.form.get('pic')
        keyword = request.form.get('keyword')
        row = request.form.get('row')
        print(row)
        new_record = [name, state, grade, room, telnum, pic, keyword]
        #with open('static/people.csv', 'w') as csv_file:
        csv_file = open('static/people.csv','wb')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(new_record)
    return render_template("update.html", message = "Record updated successfully", var = 0)

'''
@app.route("/<user>")
def user(row):
    #row = row
    with open('static/people.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        person = csv_reader[row]
        [0]
        state = csv_reader[row][1]
        grade = csv_reader[row][2]
        room = csv_reader[row][3]
        telnum = csv_reader[row][4]
        picture = csv_reader[row][5]
        keyword = csv_reader[row][6]
        
    return render_template('user.html', message = person )
'''
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    app.debug =True
    app.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
