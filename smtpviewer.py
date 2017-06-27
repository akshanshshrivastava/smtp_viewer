import smtplib
import argparse
import sys

def main(args):	
	try:
		print smtp_auth(args.server, args.port, args.username, args.password)
	except:
		usage()

def show():
	print "SMTP Viewer"
def usage():
	print "Usage: python aksmtpv.py --server 'mail server name' --port 'port for smtp' --username 'username' --password 'password'"

def smtp_auth(server, port, username, password):
	s = smtplib.SMTP(server, port)
	s.starttls()

	try:
		s.login(username, password)
		return "login successfull"

	except smtplib.SMTPAuthenticationError:
		return "Wrong username or password"

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--server", action="store", dest='server', help="server address")
	parser.add_argument("--port", action="store", dest='port', help="server port", type=int)
	parser.add_argument("--username", action="store", dest='username', help="username")
	parser.add_argument("--password", action="store", dest='password', help="password")

	args = parser.parse_args()
	
	print "\n" #next line
	show()
	main(args)

	

