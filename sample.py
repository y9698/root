from flask import Flask, render_template,request

app =Flask(__name__)

@app.route('/')
def sample():
	name = 'yk-practice2'
	return render_template('sample.html', name = name)

@app.route('/sample2' , methods=["POST"])
def sample2():
	a = int(request.form['a'])
	b = int(request.form['b'])
	return render_template("sample2.html", a = a, b = b)


if __name__ =='__main__':
	app.run(debug=True)	