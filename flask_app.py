from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    a = request.form.get('input_a', '')
    b = request.form.get('input_b', '')
    c = request.form.get('input_c', '')
    result = int(a)+int(b)+int(c)
    return render_template("main_page.html", output= "x = " + str(result))

#read inputs for variables a, b, and c
#add values
#print result