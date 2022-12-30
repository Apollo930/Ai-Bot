import random, requests, json, os
from dotenv import load_dotenv
load_dotenv()

ANAGRAM_UID=os.environ['ANAGRAM_UID']
ANAGRAM_TOKEN=os.environ['ANAGRAM_TOKEN']

def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = "`" + json_data[0]['q'] + "`" + " -" + json_data[0]['a']
	return quote

def get_anagram(text_list):
	ans = []
	for word in text_list:
		response=requests.get(f"https://www.stands4.com/services/v2/ana.php?uid={ANAGRAM_UID}&tokenid={ANAGRAM_TOKEN}&term={word}&format=json")
		data=json.loads(response.text)

		for anagrams in data["result"]:
			if int(anagrams['numwords'])>1:
				break
			else:
				ans.append(anagrams['anagram'])

	return "Anagrams: " + ", ".join(ans)

def get_response(message:str) -> str:
	p_message = message.lower()

	if p_message.split()[0] in ["hello", "hey", "hi", "yo", "sup", "wassup", "hola"]:
		return "_Hello, there!_"
	
	elif p_message.split()[0] in  ["inspire", "motivate"] or "depressed" in p_message.split():
		return get_quote()
	
	elif p_message.split()[0] == "anagram":
		return get_anagram(p_message.split()[1:])

	else:
		return "Uhh, dk what you're saying, bruh."