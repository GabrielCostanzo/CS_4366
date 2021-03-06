import flask
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import jsonify, request

app = flask.Flask(__name__)
app.config['DEBUG'] = True

# email declarations
port = 465
password = "Drink_Traders"
senderEmail = "drink.traders.ttu@gmail.com"


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to Drink Traders</h1>'''


@app.route('/listings/bids/notify', methods=['GET'])
def outbid_email():
    query_parameters = request.args
    uid = query_parameters.get('uid')
    lid = int(query_parameters.get('lid'))

    # query luke for listing info
    req = request.post("http://127.0.0.1:5000/getListingbyID", data={'lid': lid})
    listing = req.json()
    product = listing['Product']

    # create outbid message
    # create multipart message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Outbid notification"
    message["From"] = senderEmail
    message["To"] = uid

    # create text object
    text = """
    Dear user,
    
    You are receiving this email because your bid for """ + product['DrinkBrand'] + " " + product['DrinkName'] +\
           " from " + listing['Seller'] + """ has been beaten.
    
    This listing expires on: """ + listing['Expiration'] + """
    
    Use this link to go to the listing: http://127.0.0.1:5000/auction/listing_detail/""" + str(lid) + """
    
    The Drink Traders Team"""
    # create HTML object
    link = "http://127.0.0.1:5000/auction/listing_detail/" + str(lid)
    html = """
    <html>
        <body>
            <p>Dear user<br><br>
                You are receiving this email because your bid for """ + product['DrinkBrand'] + \
           " " + product['DrinkName'] + " from " + listing['Seller'] + """ has been beaten<br><br>
                This Listing expires on: """ + listing['Expiration'] + """<br><br>
                Click <a href=" """ + link + """ " >here</a> to go to the listing page<br><br><br>
                The Drink Traders Team.
            </p>
        </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # render objects for email
    message.attach(part1)
    message.attach(part2)

    # create secure SSL context
    conn = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=conn) as server:
        server.login(senderEmail, password)
        server.sendmail(senderEmail, uid, message.as_string())

    return {"success": True}


@app.route('/listings/bids/confirmation', methods=['GET'])
def confirmation_email():
    query_parameters = request.args
    uid = query_parameters.get('uid')
    lid = query_parameters.get('lid')

    # query User API for user info
    req_user = request.post("http://127.0.0.1:5000/getUserInfo", data={'uid': uid})
    user = req_user.json()
    user_email = user['email']
    name = user['name']

    # query Listing API for listing info
    req_list = request.post("http://127.0.0.1:5000/getListingbyID", data={'lid': lid})
    listing = req_list.json()
    product = listing['Product']

    # create message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Bid Confirmation"
    message["From"] = senderEmail
    message["To"] = user_email

    # create text object
    text = """
    Dear """ + name + """,

    This is a confirmation email for your bid on """ + product['DrinkBrand'] + " " + product['DrinkName'] + " from " + \
           listing['Seller'] + """

    This listing expires on: """ + listing['Expiration'] + """

    Please log into your account for any further action

    The Drink Traders Team"""
    # create HTML object
    html = """
    <html>
        <body>
            <p>Dear """ + name + """,<br><br>
                This is a confirmation email for your bid on """ + product['DrinkBrand'] + " " + \
       product['DrinkName'] + " from " + listing['Seller'] + """<br><br>
                This Listing expires on: """ + listing['Expiration'] + """<br><br>
                Please log into your account for any further action<br><br><br>
                The Drink Traders Team.
            </p>
        </body>
    </html>
    """


    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    # create secure SSL context
    conn = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=conn) as server:
        server.login(senderEmail, password)
        server.sendmail(senderEmail, user_email, message.as_string())

    return {"success": True}


app.run()













