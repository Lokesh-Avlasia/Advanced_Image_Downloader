
from flask import Flask,request,redirect,url_for,render_template
from scrapper import main
from mail import mail

# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.mime.text import MIMEText
# from email.utils import COMMASPACE
# from email import encoders
# import os

# from flask_cors import cross_origin
# from Scheduler import ScheduleJob
# from Logger import Logging

app = Flask(__name__)


@app.route('/', methods=['GET'])
# @cross_origin()
def index():
    """
    Function is responsible for showing the index page
    """
  
    if request.method == 'GET':
        return render_template('index.html')



@app.route('/job_submitted', methods=['POST','GET'])
def submit_job():
    if request.method == "GET":
        to_addr = request.args.get("email")
        mail(to_addr)
    elif request.method == 'POST':
        search_query = request.form['search-query'].lower()
        to_addr = str(request.form['email'].lower())
        no_images = request.form['images']
        main(search_query,to_addr,int(no_images))

        return redirect(url_for('submit_job', email=to_addr))
        
       
    return render_template('job_submitted.html')


if __name__ == '__main__':
    app.debug = True
    app.run()









