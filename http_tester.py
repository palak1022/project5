import socket, ssl
from html.parser import HTMLParser

# Custom HTML parser class
class 
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_paragraph = False

    def handle_starttag(self, tag, attrs):
        # Check if the tag is a paragraph tag
        if tag == 'div':
            self.in_paragraph = True

    def handle_endtag(self, tag):
        # Reset paragraph flag when end tag is encountered
        if tag == 'div':
            self.in_paragraph = False

    def handle_data(self, data):
        # Print data if inside a paragraph
        if self.in_paragraph:
            print(data)

# Example HTML content
# html_content = "<html><body><h1>Hello</h1><p>Paragraph 1</p><p>Paragraph 2</p></body></html>"






SERVER = "proj5.3700.network"
PORT = 443

request = f"GET /accounts/login/?next=/fakebook/ HTTP/1.1\r\n"
request += f"HOST: {SERVER}:{PORT}\r\n\r\n"


mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket = ssl.wrap_socket(mysocket, ssl_version=ssl.PROTOCOL_TLSv1_2)

mysocket.connect((SERVER, PORT))
mysocket.send(request.encode('ascii'))

def receive(sock) -> str:
        message = ""
        response = sock.recv(1024).decode("ascii") # first retrieval
        while response: # looping till we get no response, which is a potential error.
            message += response # building message as whole response can not be received within one retrieval when bits > 1024
            if response[-1] == '\n': # '\n' means end of response, hence we break the loop
                break
            response = sock.recv(1024).decode("ascii")
            
        return message

# data = mysocket.recv(4096)
data = receive(mysocket)


# Instantiate the parser
parser = MyHTMLParser()

# Parse the HTML content
parser.feed(data)


# print("Response:\n%s" % data)


