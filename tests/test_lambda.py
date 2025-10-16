import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lambda_function import lambda_handler
import xml.etree.ElementTree as ET

def test_lambda_returns_twiml():
    result = lambda_handler({}, None)
    
    # check status code
    assert result['statusCode'] == 200
    
    # check Content-Type is XML
    assert result['headers']['Content-Type'] == 'application/xml'
    
    # check tht <Say> is in TwiML
    root = ET.fromstring(result['body'])
    say = root.find('Say')
    assert say is not None
