# miniblogger
Flask App on AWS

Todo: 
- Change name from miniblogger to footy_api. For some reason if I just change the name python refuses to do a relative import.

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
