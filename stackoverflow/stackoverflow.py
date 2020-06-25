from stackapi import StackAPI
from datetime import datetime
from utils import output_write, get_samples, print_status_samples

# max_date = datetime(year=2019, month=4, day=20)
directory = "stackoverflow"


def get_questions_when_body_has(sample):
    return api.fetch("search/advanced?body={0}".format(sample))


def get_top_five_tags(api, user_id):
    tags = []
    page = 1
    query = api.fetch("users/{0}/top-tags".format(user_id), page=page)
    for tag in query["items"]:
        tags.append(tag)
    while query["has_more"]:
        page += 1
        query = api.fetch("users/{0}/top-tags".format(user_id), page=page)
        for tag in query["items"]:
            tags.append(tag)
    tags = sorted(tags, key=lambda tag: tag["answer_score"], reverse=True)[:5]
    tags_return = []
    for tag in tags:
        tags_return.append(tag["tag_name"])
    return tags_return


def list_to_string(list):
    string = ""
    for item in list:
        string += item + ";"
    return string


def create_output(framework, sample, question, answer, question_owner, answer_owner):
    question_tags = list_to_string(question["tags"])
    question_owner_tags = list_to_string(get_top_five_tags(api, question_owner["user_id"]))
    answer_owner_tags = [] if answer_owner["user_id"] == "" else list_to_string(get_top_five_tags(api, answer_owner["user_id"]))
    output = framework + "," + sample
    output = output + "," + str(question["question_id"]) + "," + question_tags + "," + str(question["view_count"]) + "," + str(question["answer_count"]) + "," + str(question["score"]) + "," + str(datetime.fromtimestamp(question["creation_date"])) + "," + str(question["link"]) + "," + str(question_owner["user_id"]) + "," + str(question_owner["reputation"]) + "," + str(datetime.fromtimestamp(question_owner["creation_date"])) + "," + str(question_owner_tags)
    output = output + "," + str(answer["answer_id"]) + "," + str(answer["score"]) + "," + ("" if answer["creation_date"] == "" else str(datetime.fromtimestamp(answer["creation_date"]))) + "," + str(answer_owner["user_id"]) + "," + str(answer_owner["reputation"]) + "," + ("" if answer_owner["creation_date"] == "" else str(datetime.fromtimestamp(answer_owner["creation_date"]))) + "," + str(answer_owner_tags)
    return output


def get_header():
    return "framework,path,question_id,question_tags,question_view_count,question_answer_count," \
           "question_score,question_creation_date,question_link,question_owner_id," \
           "question_owner_reputation,question_owner_creation_date,question_owner_tags," \
           "answer_id," \
           "answer_score," \
           "answer_creation_date," \
           "answer_owner_id," \
           "answer_owner_reputation," \
           "answer_owner_creation_date," \
           "answer_owner_tags"


def get_owner_by_user_id(api, id):
    return api.fetch("users", ids=[id])["items"][0]


def stackoverflow(framework, projects):
    global api
    api = StackAPI("stackoverflow")
    samples = get_samples(projects)
    output_write(framework, directory, "questions_and_answers", get_header(), True)
    for index, sample in enumerate(samples):
        print_status_samples(index+1, len(samples))
        questions = get_questions_when_body_has(sample)
        for indx, question in enumerate(questions["items"]):
            print("{0}% questions analysed of {1}".format( (indx+1)/len(questions)*100, sample))
            try:
                answer = api.fetch("answers/{ids}", ids=[question["accepted_answer_id"]])["items"][0]
                answer_owner = get_owner_by_user_id(api, answer["owner"]["user_id"])
            except KeyError:
                answer = {
                    "answer_id": "",
                    "score": "",
                    "creation_date": ""
                }
                answer_owner = {
                    "user_id": "",
                    "reputation": "",
                    "creation_date": "",
                    "tags": []
                }
            question_owner = get_owner_by_user_id(api, question["owner"]["user_id"])
            output = create_output(framework, sample, question, answer, question_owner, answer_owner)
            output_write(framework, directory, "questions_and_answers", output, False)
