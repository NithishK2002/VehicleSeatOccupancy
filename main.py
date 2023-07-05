from flask import Flask , jsonify , request , redirect , render_template
import random
import time
# time.sleep(5)
app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

@app.route("/",methods=['POST','GET'])
def index():
  return render_template("newindex.html")
def getBusValue():
  global data
  data = random.randint(1,50)
  print(data)
  time.sleep(5)
  return { "Seat Count" : data}
  
@app.route('/getBusData',methods=['POST','GET'])
def get():
  data2 = request.get_json()
  global value 
  value = 50 - data2['NumberOfHeads']
  print(value)
  print(data2)
  return jsonify(data2)

@app.route("/display",methods=['POST','GET'])
def displayBusDetails():
  #dict = get()
  # print(value)
  val = getBusValue()
  value=val["Seat Count"]
  return render_template("index1.html",data=value)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run(host='0.0.0.0', port=8080)
