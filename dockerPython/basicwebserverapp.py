from flask import Flask
import sys
import optparse
import time
import os

app = Flask(__name__)

start = int(round(time.time()))

@app.route("/")
def display_instance():
	ec2_id = 'wget -q -O - http://169.254.169.254/latest/meta-data/instance-id'
    return "This is the EC2 ID of the webserver listening!" % ec2_id

def start_instance():
	os.system('Start-EC2Instance -InstanceId %s' % ec2_id)	

def stop_instance():
	os.system('Stop-EC2Instance -InstanceId %s' % ec2_id)
	
if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python basicwebserverapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
	parser.add_option('-u', '--start', action='store', dest='start', help='To start the instance.')
	parser.add_option('-x', '--stop', action='store', dest='stop', help='To stop the instance.')
    (args, _) = parser.parse_args()
	if args.start:
		print "The instance will now be started"
		start_instance()
	if args.stop:
		print "The instance will now be stopped"
		stop_instance()
	if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
