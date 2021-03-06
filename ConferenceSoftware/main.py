"""
    An application written in Flask for 
    conference management

    Written by Henry Ling and Nick Fong 2016
"""
from ConferenceSoftware import app
from werkzeug import secure_filename


@app.route('/')
def index():
	return 'HARRO WURLD!'

# THIS DOESN'T WORK YET
"""
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['the_file']
		f.save('/var/www/uploads/' + secure_filename(f.filename))
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid password'
		else:
			session['logged_in'] = True
			flash('Logged in')
			return redirect(url_for('index'))
	return render_template('login.html', error=error)

