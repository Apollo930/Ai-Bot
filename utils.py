import random, requests, json


def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = "`" + json_data[0]['q'] + "`" + " -" + json_data[0]['a']
	return quote

def get_response(message:str) -> str:
	p_message = message.lower()

	if p_message.split()[0] in ["hello", "hey", "hi", "yo", "sup", "wassup", "hola"]:
		return "_Hello, there!_"
	
	elif p_message.split()[0] in  ["inspire", "motivate"] or "depressed" in p_message.split():
		return get_quote()
	else:
		return "Uhh, dk what you're saying, bruh."