import sched
import time
import pymongo
import smtplib
import ssl
from pymongo import MongoClient
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# database connections
cluster = MongoClient(
    "mongodb+srv://nicolas:capstone1@cluster0.vfv8c.mongodb.net/capstone?retryWrites=true&w=majority")
db = cluster["capstone"]
listings = db["collection"]
products = db["ProductCollection"]

# email declarations
port = 465
password = "Drink_Traders"
senderEmail = "drink.traders.ttu@gmail.com"

s = sched.scheduler(time.time, time.sleep)


def close_listings(sc):
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%m/%d/%Y")
    # print("date and time =", dt_string)
    s.enter(86400, 1, close_listings, (sc,))

    listings_to_close = listings.find({"Expiration": dt_string})
    if listings_to_close is not None:
        for listing in listings_to_close:
            highest_name = str(listing['Transaction'][0]['name'])
            highest_email = str(listing['Transaction'][0]['email'])
            final_price = str(listing['Transaction'][0]['price'])

            # send email
            # create multipart message for buyer
            buyer_message = MIMEMultipart("alternative")
            buyer_message["Subject"] = "Bid Accepted!"
            buyer_message["From"] = senderEmail
            buyer_message["To"] = highest_email

            text = """
            Dear""" + highest_name + """, 
            
            Your bid for """ + listing['Product']['DrinkBrand'] + " " + listing['Product']['DrinkName'] + " from " + \
                   listing['Seller'] + """ was accepted!
            
            Total to pay: $""" + final_price + """
            
            The Drink Traders Team"""

            print(text)

            html = """
            <html>
                <body>
                    <p>Dear """ + highest_name + """<br><br>
                        Your bid for """ + listing['Product']['DrinkBrand'] + " " + listing['Product']['DrinkName'] + \
                   " from " + listing['Seller'] + """ was accepted!<br><br>
                        Total to pay: $""" + final_price + """<br><br>
                        Please get in contact with the seller to complete the transaction<br><br>
                        The Drink Traders Team.
                    </p>
                </body>
            </html>
            """

            part1 = MIMEText(text, "plain")
            part2 = MIMEText(html, "html")

            buyer_message.attach(part1)
            buyer_message.attach(part2)

            connection = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=connection) as server:
                server.login(senderEmail, password)
                server.sendmail(senderEmail, highest_email, buyer_message.as_string())

            listings.update_one({"_id": listing['_id']}, {"$set": {"Status": "Closed"}})


s.enter(5, 1, close_listings, (s,))

s.run()

