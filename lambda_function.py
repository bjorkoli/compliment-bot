from twilio.twiml.voice_response import VoiceResponse
import random

def lambda_handler(event, context):
    compliments = [
        "You are amazing!",
        "You have a great sense of humor!",
        "You're really talented!",
        "You are an awesome person!",
        "You brighten everyone's day!"
    ]

    # pick random compliment
    chosen_compliment = random.choice(compliments)

    resp = VoiceResponse()
    resp.say(chosen_compliment, voice="Polly.Joanna")
    resp.hangup()

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/xml"},
        "body": str(resp)
    }
