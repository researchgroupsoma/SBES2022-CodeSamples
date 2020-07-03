from violin import Violin
import os

os.chdir("/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado")

v = Violin(["stackoverflow/android_questions_and_answers_output.csv","stackoverflow/spring_questions_and_answers_output.csv","stackoverflow/aws_questions_and_answers_output.csv","stackoverflow/azure_questions_and_answers_output.csv"], "question_owner_reputation")
v.save(title="Reputação de quem pergunta", ylabel="Reputação em escala log", filename="graphics/reputacao_perguntas.pdf", xlabel="Code Samples")

v = Violin(["stackoverflow/android_questions_and_answers_output.csv","stackoverflow/spring_questions_and_answers_output.csv","stackoverflow/aws_questions_and_answers_output.csv","stackoverflow/azure_questions_and_answers_output.csv"], "answer_owner_reputation")
v.save(title="Reputação de quem responde (aceitas)", ylabel="Reputação em escala log", filename="graphics/reputacao_respostas.pdf", xlabel="Code Samples")


v = Violin(["allanswers/android_all_answers_output.csv","allanswers/spring_all_answers_output.csv","allanswers/aws_all_answers_output.csv","allanswers/azure_all_answers_output.csv"], "answer_owner_reputation")
v.save(title="Reputação de quem responde (todas)", ylabel="Reputação em escala log", filename="graphics/reputacao_todas_respostas.pdf", xlabel="Code Samples")