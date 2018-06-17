from flask import Flask
from flask import render_template
from core.requests.api_calls import ApiCalls
from core.requests.web_request import WebRequest
from core.model.request import Request
import random

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def hello_world():
    return render_template('index.html')


@app.route('/callbacks', methods=["POST", "GET"])
def callback():
	request = Request()
	request.setTXN_AMOUNT("1.00")
	request.setMERCH_ORDER_ID("ORDER" + str(random.randint(9999,99999999)))
	request.setCUST_NUMBER("919716809959")
	request.setMERCH_CUST_EMAIL("sanchitsaxena9450@gmail.com")
	request.setCOLLECTOR_ID("522")


	return WebRequest.getJsonFrame(request)


if (__name__ == "__main__"):
	app.run(port = 5000)
