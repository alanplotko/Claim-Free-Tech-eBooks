import requests
import re
import os.path
import getpass
import time
import datetime
import sys

# Configure save path here
savePath = "/home/" + getpass.getuser() + "/Desktop/"

fileName = "eBookLog"
fullFilePath = os.path.join(savePath, fileName + ".txt")         
f = open(fullFilePath, "a")
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S\n------------------------\n')
f.write(timestamp)

# Authentication
loginUrl = "https://www.packtpub.com/"
data = {
	"email": sys.argv[1],
	"password": sys.argv[2],
	"op": "Login",
	"form_id": "packt_user_login_form"
}

session = requests.Session()
session.get(loginUrl)
req = session.post(loginUrl, data)

if req.status_code == 200:
	f.write("Authenticated successfully.\n")
	f.write("Establishing connection to Packtpub Free Learning...")
	siteReq = session.get("https://www.packtpub.com/packt/offers/free-learning")
	if siteReq.status_code == 200:
		f.write(" connection established!\n")
		html = siteReq.text

		f.write("Searching for free ebook url...")
		regex  = re.compile('/freelearning-claim/\d+/\d+')
		freeBookCode = regex.search(html)
		if freeBookCode is not None:
			f.write(" found code!\n")
			url = "https://www.packtpub.com" + freeBookCode.group(0)
			bookClaimReq = session.get(url)

			f.write("Claiming free ebook...")
			if bookClaimReq.status_code == 200 or bookClaimReq.status_code == 302:
				f.write(" success! Free ebook claimed!")
			else:
				if bookClaimReq.history:
					f.write(" request was redirected.\nAnalyzing response history...\n")
					success = False
					for resp in bookClaimReq.history:
						if resp.status_code == 302:
							success = True
						f.write(str(resp.status_code) + "\t" + resp.url)
					if success:
						f.write("\nPreviously claimed free ebook. Check Packtpub to confirm that the ebook has been claimed.")
				else:
					f.write("\nError claiming free ebook.\n\nWarning: Website might be down. Try manually visiting Packtpub.")
		else:
			f.write(" failed to find code.\n\nWarning: Website html has probably changed. Please update the Python script.")
	else:
		f.write(" failed to connect to Packtpub.\n\nWarning: Website might be down. Try manually visiting Packtpub.")

	f.write("\n------------------------------------------------\n\n")
	f.close()
