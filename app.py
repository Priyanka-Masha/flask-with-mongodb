from flask import Flask,render_template,request
import pymongo
from pymongo import MongoClient

cluster = MongoClient('')
db=cluster["learning_challenge"]
col=db["Name"] #collection

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def start():
    return render_template('index.html')

@app.route("/submit",methods=["GET","POST"])
def submit():
    name=request.form.get("username")
    desc=request.form.get("short_summary")

    col.insert_one({"Name":name, "Description":desc})
    for x in col.find():
        value1=x['Name']
        value2=x['Description']
    
    result={
        'Name':value1,
        'Description':value2
    }
    return render_template('index.html')


if __name__ =="__main__":
    app.run(debug=True)



















