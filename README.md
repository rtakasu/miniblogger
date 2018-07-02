# miniblogger
Flask App on Bluemix Cloud

API:
GET /entries:
	- returns json array of entries in reverse order of creation

POST /add:
	- POST JSON Body:
		{
			"title": <title>,
			"text": <text>
		}
	- Adds one entry to database and returns entries