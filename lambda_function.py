from twilio.twiml.voice_response import VoiceResponse

def lambda_handler(event, context):
    resp = VoiceResponse()
    resp.say("Hej! Du är fantastisk!", voice="Polly.Svenska")
    resp.hangup()

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/xml"},
        "body": str(resp)
    }
