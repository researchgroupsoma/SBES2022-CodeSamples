from utils import output_write, get_samples, print_status_samples
from stackapi import StackAPI
from stackoverflow import *
from datetime import datetime


directory = "allanswers"


def create_output(framework, sample, question_id, answer, answer_owner):
	answer_owner_tags = [] if answer_owner["user_id"] == "" else list_to_string(get_top_five_tags(api, answer_owner["user_id"]))
	output = framework + "," + sample + "," +str(question_id)
	output = output + "," + \
	str(answer["answer_id"]) + "," + \
	str(answer["score"]) + "," + \
	str(datetime.fromtimestamp(answer["creation_date"])) + "," + \
	str(answer_owner["user_id"]) + "," + \
	str(answer_owner["reputation"]) + "," + \
	("" if answer_owner["creation_date"] == "" else str(datetime.fromtimestamp(answer_owner["creation_date"]))) + "," + \
	str(answer_owner_tags)
	return output


def get_header():
    return "framework,path,question_id,answer_id," \
           "answer_score," \
           "answer_creation_date," \
           "answer_owner_id," \
           "answer_owner_reputation," \
           "answer_owner_creation_date," \
           "answer_owner_tags"

def allanswers(framework, projects):
	global api
	api = StackAPI("stackoverflow")
	samples = get_samples(projects)
	output_write(framework, directory, "all_answers", get_header(), True)
	with open("stackoverflow/"+framework+"_questions_and_answers_output.csv") as questions:
		for index, question in enumerate(questions):
			if index == 0: continue
			print("Questions from sample " + question.split(",")[1])
			question = question.replace("\n", "")
			question_id = question.split(",")[2]
			answers = api.fetch("questions/" + question_id + "/answers")["items"]
			print(len(answers))
			for indx,answer in enumerate(answers):
				print("{0}% answers analysed of question {1}".format( (indx+1)/len(answers)*100, question_id))
				try:
					answer_owner = get_owner_by_user_id(api, answer["owner"]["user_id"])
				except KeyError:
					answer_owner = {
						"user_id": "",
						"reputation": "",
						"creation_date": "",
						"tags": []
					}

				output = create_output(framework, question.split(",")[1], question_id, answer, answer_owner)
				output_write(framework, directory, "all_answers", output, False)