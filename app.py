from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = "John"  # 這裡可以換成你想顯示的名字
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
