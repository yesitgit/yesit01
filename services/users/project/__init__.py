import os
from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS') # new
app.config.from_object(app_settings) # new

import sys
print(app.config, file=sys.stderr)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
	return jsonify({
		'status': 'success',
		'message': 'pong!'
	})