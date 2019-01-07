from flask import Flask, render_template, jsonify
import time, datetime

app = Flask(__name__)

@app.route('/')
def health():
	return jsonify(ok=1)

@app.route('/api')
def api():
	print 'Starting api...'
	t_end = time.time() + 60 * 10
	while time.time() < t_end:
		print 'Echo ',datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
		time.sleep(10)
	return jsonify(ok=1)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

