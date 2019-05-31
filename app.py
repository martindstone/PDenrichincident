import grequests
from flask import Flask, request, render_template, url_for, redirect, session, Response
import json
import requests

import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or os.urandom(20)

@app.route('/incidents')
def incidents():
	headers = {
		'Authorization': request.headers['Authorization'],
		'Accept': 'application/vnd.pagerduty+json;version=2'
	}

	params = {}
	for (k, v) in request.args.lists():
		if len(v) == 1:
			params[k] = v[0]
		else:
			params[k] = v

	# req = requests.Request(
	# 	method='GET',
	# 	url='https://api.pagerduty.com/incidents',
	# 	headers=headers,
	# 	params=params
	# )

	# prepped = req.prepare()
	# response = requests.Session().send(prepped)

	response = requests.get(
		url='https://api.pagerduty.com/incidents',
		headers=headers,
		params=params
	)

	incidents = response.json()

	incidents_index = {}
	rs = []
	for index, incident in enumerate(incidents["incidents"]):
		incidents_index[incident['id']] = index
		rs.append(grequests.get(f"https://api.pagerduty.com/incidents/{incident['id']}/notes", headers=headers, params={"limit": 100}))
	noteses = grequests.map(rs)

	for notes in noteses:
		incident_id = notes.url.split('/')[4]
		incidents["incidents"][incidents_index[incident_id]]["notes"] = notes.json()["notes"]

	r = Response(json.dumps(incidents))
	r.headers = {
		"Content-Type": "application/json",
		"Access-Control-Allow-Origin": "*"
	}
	return r
