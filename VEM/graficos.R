library(ggplot2)
library(scales)

typeOfFramework = "Code Samples"
frameworkName1 = "Android"
frameworkName2 = "Spring"
frameworkName3 = "AWS"
frameworkName4 = "Azure"
factorPositionMedianLabel = 1.4
mainDirectory = "C:\\Users\\Gabriel\\Documents\\gabrielsmenezes\\pesquisamestrado\\"
output_width = 3.5
output_height = 2.5


point <- format_format(big.mark = ".", decimal.mark = ",", scientific = FALSE)


plotGraphic <- function ()  {
  p1 <- ggplot(all, aes) + 
    scale_y_log10(labels = comma) +
    geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
    geom_boxplot(width=0.7,alpha=0.7) + ggtitle(title) + xlab(typeOfFramework) + ylab(verticalTitle) + 
    annotate("text", x = 1, y = framework1_median*factorPositionMedianLabel, label = point(round(framework1_median, 2)), size = 4) + 
    annotate("text", x = 2, y = framework2_median*factorPositionMedianLabel, label = point(round(framework2_median, 2)), size = 4) +
    annotate("text", x = 3, y = framework3_median*factorPositionMedianLabel, label = point(round(framework3_median, 2)), size = 4) +
    annotate("text", x = 4, y = framework4_median*factorPositionMedianLabel, label = point(round(framework4_median, 2)), size = 4) +
    theme(plot.title=element_text(size=10,face="bold") ,axis.title=element_text(size=8),axis.text=element_text(size=8))
  return(p1)
}

###### RQ1

###### Java Files
framework1=read.csv(paste(mainDirectory, "understandmetrics\\android_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "understandmetrics\\spring_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework3=read.csv(paste(mainDirectory, "understandmetrics\\aws_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework4=read.csv(paste(mainDirectory, "understandmetrics\\azure_understandmetrics_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2, framework3, framework4)
dataFramework1=framework1$numberOfJavaFiles
dataFramework2=framework2$numberOfJavaFiles
dataFramework3=framework3$numberOfJavaFiles
dataFramework4=framework4$numberOfJavaFiles
title = "Número de Arquivos Java"
verticalTitle = "Arquivos Java (escala log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), numberOfJavaFiles)
plotGraphic()
ggsave(paste(mainDirectory, "VEM\\java-files.pdf", sep = ""), width = output_width, height = output_height)



###### Lines of code per java file
framework1=read.csv(paste(mainDirectory, "understandmetrics\\android_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "understandmetrics\\spring_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework3=read.csv(paste(mainDirectory, "understandmetrics\\aws_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework4=read.csv(paste(mainDirectory, "understandmetrics\\azure_understandmetrics_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2, framework3, framework4)
dataFramework1=framework1$CountLineCode/framework1$numberOfJavaFiles
dataFramework2=framework2$CountLineCode/framework2$numberOfJavaFiles
dataFramework3=framework3$CountLineCode/framework3$numberOfJavaFiles
dataFramework4=framework4$CountLineCode/framework4$numberOfJavaFiles
title = "Linhas de Código por Arquivo"
verticalTitle = "Linhas de Código (escala log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), CountLineCode/numberOfJavaFiles)
plotGraphic()
ggsave(paste(mainDirectory, "VEM\\loc.pdf", sep = ""), width = output_width, height = output_height)



###### Complexity
framework1=read.csv(paste(mainDirectory, "understandmetrics\\android_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "understandmetrics\\spring_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework3=read.csv(paste(mainDirectory, "understandmetrics\\aws_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework4=read.csv(paste(mainDirectory, "understandmetrics\\azure_understandmetrics_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2, framework3, framework4)
dataFramework1=(framework1$SumCyclomaticStrict/framework1$CountDeclMethod)
dataFramework2=(framework2$SumCyclomaticStrict/framework2$CountDeclMethod)
dataFramework3=(framework3$SumCyclomaticStrict/framework3$CountDeclMethod)
dataFramework4=(framework4$SumCyclomaticStrict/framework4$CountDeclMethod)
title = "Complexidade Ciclomática por\nMétodo"
verticalTitle = "Complexidade Ciclomática (escala log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), (SumCyclomaticStrict/CountDeclMethod))
plotGraphic()
ggsave(paste(mainDirectory, "VEM\\cc.pdf", sep = ""), width = output_width, height = output_height)



###### Readability

framework1=read.csv(paste(mainDirectory, "understandmetrics\\android_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "understandmetrics\\spring_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework3=read.csv(paste(mainDirectory, "understandmetrics\\aws_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework4=read.csv(paste(mainDirectory, "understandmetrics\\azure_understandmetrics_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2, framework3, framework4)
dataFramework1=framework1$readability * 100
dataFramework2=framework2$readability * 100
dataFramework3=framework3$readability * 100
dataFramework4=framework4$readability * 100
title = "Readability por Arquivo Java"
verticalTitle = "Readability (escala log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), readability * 100)
plotGraphic()
ggsave(paste(mainDirectory, "VEM\\readability.pdf", sep = ""), width = output_width, height = output_height)


############################# Stack Overflow ###########################################
######## reputation de quem pergunta sobre os code samples

framework1=read.csv(paste(mainDirectory, "stackoverflow\\android_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "stackoverflow\\spring_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework3=read.csv(paste(mainDirectory, "stackoverflow\\aws_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework4=read.csv(paste(mainDirectory, "stackoverflow\\azure_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2, framework3, framework4)
dataFramework1=framework1$question_owner_reputation
dataFramework2=framework2$question_owner_reputation
dataFramework3=framework3$question_owner_reputation
dataFramework4=framework4$question_owner_reputation
title = "Reputação de Quem Pergunta"
verticalTitle = "Reputação (escala log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), question_owner_reputation)
plotGraphic()
ggsave(paste(mainDirectory, "VEM\\question-reputation.pdf", sep = ""), width = output_width, height = output_height)


######## reputation de quem tem respostas ACEITAS de perguntas sobre os code samples
framework1=read.csv(paste(mainDirectory, "stackoverflow\\android_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "stackoverflow\\spring_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework3=read.csv(paste(mainDirectory, "stackoverflow\\aws_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework4=read.csv(paste(mainDirectory, "stackoverflow\\azure_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2, framework3, framework4)
dataFramework1=framework1$answer_owner_reputation
dataFramework2=framework2$answer_owner_reputation
dataFramework3=framework3$answer_owner_reputation
dataFramework4=framework4$answer_owner_reputation
title = "Reputação de Quem Responde\ne tem a Resposta Aceita"
verticalTitle = "Reputação (escala log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), answer_owner_reputation)
plotGraphic()
ggsave(paste(mainDirectory, "VEM\\accepted-answer-reputation.pdf", sep = ""), width = output_width, height = output_height)


######## reputation de quem tem respostas NAO ACEITAS de perguntas sobre os code samples
framework1=read.csv(paste(mainDirectory, "allanswers\\android_all_answers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "allanswers\\spring_all_answers_output.csv", sep = ""), sep=",",header=T)
framework3=read.csv(paste(mainDirectory, "allanswers\\aws_all_answers_output.csv", sep = ""), sep=",",header=T)
framework4=read.csv(paste(mainDirectory, "allanswers\\azure_all_answers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2, framework3, framework4)
dataFramework1=framework1$answer_owner_reputation
dataFramework2=framework2$answer_owner_reputation
dataFramework3=framework3$answer_owner_reputation
dataFramework4=framework4$answer_owner_reputation
title = "Reputação de Quem Responde"
verticalTitle = "Reputação (escala log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), answer_owner_reputation)
plotGraphic()
ggsave(paste(mainDirectory, "VEM\\all-answer-reputation.pdf", sep = ""), width = output_width, height = output_height)
