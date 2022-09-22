from flask import Flask,render_template
app=Flask(__name__)
@app.route("/",methods=["GET"])
def fn():return ("<html><body><h1>WORKING !!</h1></body></html>")
app.run(host="0.0.0.0",port=8085)