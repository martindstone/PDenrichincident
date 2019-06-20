# PDenrichincident
Enrich the output of the PagerDuty /incidents endpoint

## Summary
This is a Flask app that presents an /incidents endpoint that is identical to the [PagerDuty /incidents endpoint](https://api-reference.pagerduty.com/#!/Incidents/get_incidents), except that each incident returned in the list will have an additional element "notes" where all the incident notes can be found, in the same format as that returned by the [/incidents/{id}/notes PagerDuty endpoint](https://api-reference.pagerduty.com/#!/Incidents/get_incidents_id_notes).

## Local Installation
Clone this repo. Then:
```
python3 -m venv venv                   # create a virtual environment
. venv/bin/activate                    # activate it
pip install -r requirements.txt        # install the dependencies
FLASK_DEBUG=true flask run             # run the app in flask with debug on
```

## Heroku Installation

Push this button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Now GET https://YOUR_DEPLOYED_APP_SERVER_NAME/incidents in the same way you would against the PagerDuty /incidents endpoint!
