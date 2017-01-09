
from util import *
from bs4 import BeautifulSoup

class Profile(object):
	
	"""Profile Class For User"""

	def __init__(self, handle=""):
		super(Profile, self).__init__()
		self.handle = handle
		self.domain_url = "https://www.codechef.com"


	def get_user_handle(self):
		self.usr_name = ''
		first_time = True
		while len(self.usr_name) == 0:
			if first_time:
				first_time = False
			else:
				print("You haven't entered any handle. Please try again.")

			self.usr_name = input("Enter Your CodeChef Handle: ").strip()


	def get_solved_problems(self):
		"""Function Processes the user page and return a dictionary object containing all successfully solved problems"""
		"""Return format { problem_code : problem_link }"""
		domain_url = self.domain_url
		handle = self.handle
		user_url = domain_url + "/users/" + handle
		user_page = get_url_data(user_url)
		soup = BeautifulSoup(user_page,"lxml")
		# Segregate problems table
		sp = soup.find_all('table')[2]
		
		prob_list = {}

		for cell in sp.find_all('td'):
			if cell.text == "Problems Successfully Solved:":
				n_soup = cell.nextSibling.nextSibling

		for s in n_soup.find_all('a'):
			ques_link = (str(s.get('href'))).strip()
			ques_link.
			prob_list[s.text.strip()] = 

		return prob_list

	def extract_code(self, prob_code, sub_link):
		"""Function Extracts the user submitted code from submission page"""
		"""Return format @tuple (problem_code, code_lang, code_str)"""

		domain_url = self.domain_url
		code_page_url = domain_url + sub_link
		code_page = get_url_data(code_page_url)
		soup = BeautifulSoup(code_page,"lxml")

		lang = (soup.find('pre')).get("class")[-1]

		code = soup.find_all('ol')[-1]
		
		# in some cases code contains stray /xa0 character
		# it needs to be removed
		cod_str = str(code)
		cod_str = cod_str.replace(u'\xa0',u' ')

		# replacing </li> with </li>\n for pretty-printing
		# then recreate a bs4 object

		cod_str = cod_str.replace("</li>", "</li>\n")
		code = BeautifulSoup(cod_str,"lxml")
		code_str = code.text

		return (prob_code, lang, code_str)