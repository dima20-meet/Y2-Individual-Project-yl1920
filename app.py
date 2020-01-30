from flask import *
from flask import session as login_session
import requests, json
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route('/')
def home():
	books=query_all()
	return render_template('index.html', books=books)

@app.route('/contact')
def contact():
	return render_template('index.html')


@app.route('/addbook',methods=['POST'])
def addbook():
	add_book(request.form["bookname"], request.form["author"], request.form["pages"], request.form["desc"], request.form["image"])
	return redirect(url_for('home'))



@app.route('/study_image', methods = ['POST'])
def study_image():
	image_url = request.form['url']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 

    # YOUR CODE HERE!


	# you can use the headers to pass in hidden info, here we are sending a secret Key (think of it as a password)
	headers = {'Authorization': 'Key 89460613ec684b3fad9f6d824450eb2f'}

	# this is the url of where your request will go
	api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"

	# this is content of the message(data) you are sending to clarifai
	data ={"inputs": [
	      {
	        "data": {
	          "image": {
	            "url": image_url	          
	            }
	        }
	      }
	    ]}

# putting everything together; sending the request!
	response = requests.post(api_url, headers=headers, data=json.dumps(data))
	request_dict = json.loads(response.content)

	isItABook=False

	for concept in (request_dict["outputs"][0]["data"]["concepts"]):
		if concept["name"]=="book" or concept["name"]=="books":
			isItABook=True
			print("It's a booooooooooooooooook")
    
	return render_template('index.html',books=query_all(), result=isItABook)

# @app.route('/mybooks')
# def mybooks():


if __name__=='__main__':
	app.run(debug=True)
