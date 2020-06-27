library(ggplot2)
library(scales)

typeOfFramework = "Code Samples"
frameworkName1 = "Android"
frameworkName2 = "Spring"
frameworkName3 = "AWS"
frameworkName4 = "Azure"
factorPositionMedianLabel = 1.4
mainDirectory = "/home/gabriel/Documentos/gabrielsmenezes/pesquisamestrado/"

plotGraphic <- function ()  {
  p1 <- ggplot(all, aes) + 
    scale_y_log10(labels = comma) +
    geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
    geom_boxplot(width=0.7,alpha=0.7) + ggtitle(title) + xlab(typeOfFramework) + ylab(verticalTitle) + 
    annotate("text", x = 1, y = framework1_median*factorPositionMedianLabel, label = round(framework1_median, 2), size = 8) + annotate("text", x = 2, y = framework2_median*factorPositionMedianLabel, label = round(framework2_median, 2), size = 8) +
    theme(plot.title=element_text(size=24,face="bold") ,axis.title=element_text(size=20),axis.text=element_text(size=18))
  return(p1)
}

##### Graphics of Introduction

framework1=read.csv(paste(mainDirectory, "githubmetadata/android_metadata_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "githubmetadata/spring_metadata_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)

#### Stars
dataFramework1=framework1$stargazers
dataFramework2=framework2$stargazers
title = "Number of Stars"
verticalTitle = "Number of Stars (log scale)"
framework1_median =  median(unlist(dataFramework1), na.rm = TRUE)
framework2_median =  median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), stargazers)
plotGraphic()
ggsave(paste(mainDirectory, "githubmetadata/stars.pdf", sep = ""), width = 4.5, height = 4.5)


#### Commits
dataFramework1=framework1$commits
dataFramework2=framework2$commits
title = "Number of Commits"
verticalTitle = "Number of Commits (log scale)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), commits)
plotGraphic()
ggsave(paste(mainDirectory, "githubmetadata/commits.pdf", sep = ""), width = 4.5, height = 4.5)



#### Number of Files
framework1=read.csv(paste(mainDirectory, "numberofextensionfile/android_numberofextensionfile_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "numberofextensionfile/spring_numberofextensionfile_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$numberOfFiles
dataFramework2=framework2$numberOfFiles
title = "Number of Files"
verticalTitle = "Number of Files (log scale)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), numberOfFiles)
plotGraphic()
ggsave(paste(mainDirectory, "numberofextensionfile/files.pdf", sep = ""), width = 4.5, height = 4.5)


###### RQ1

###### Java Files
framework1=read.csv(paste(mainDirectory, "understandmetrics/android_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "understandmetrics/spring_understandmetrics_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$numberOfJavaFiles
dataFramework2=framework2$numberOfJavaFiles
title = "Number of Java Files"
verticalTitle = "Number of Files (log scale)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), numberOfJavaFiles)
plotGraphic()
ggsave(paste(mainDirectory, "understandmetrics/numberOfJavaFiles.pdf", sep = ""), width = 4.5, height = 4.5)



###### Lines of code per java file
framework1=read.csv(paste(mainDirectory, "understandmetrics/android_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "understandmetrics/spring_understandmetrics_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$CountLineCode/framework1$numberOfJavaFiles
dataFramework2=framework2$CountLineCode/framework2$numberOfJavaFiles
title = "Lines of Code per File"
verticalTitle = "Lines of Code (log scale)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), CountLineCode/numberOfJavaFiles)
plotGraphic()
ggsave(paste(mainDirectory, "understandmetrics/RLOC_files.pdf", sep = ""), width = 4.5, height = 4.5)



###### Complexity
framework1=read.csv(paste(mainDirectory, "understandmetrics/android_understandmetrics_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "understandmetrics/spring_understandmetrics_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=(framework1$SumCyclomaticStrict/framework1$CountDeclMethod) * 100
dataFramework2=(framework2$SumCyclomaticStrict/framework2$CountDeclMethod) * 100
title = "Cyclomatic Complexity\nper method"
verticalTitle = "Nº of Decisions Points (log scale)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), (SumCyclomaticStrict/CountDeclMethod) * 100)
plotGraphic()
ggsave(paste(mainDirectory, "understandmetrics/ACC.pdf", sep = ""), width = 4.5, height = 4.5)


#####RQ2


#####Lifetime
framework1=read.csv(paste(mainDirectory, "githubmetadata/android_metadata_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "githubmetadata/spring_metadata_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$lifetime
dataFramework2=framework2$lifetime
title = "Lifetime"
verticalTitle = "Nº of day (log scale)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), lifetime)
plotGraphic()
ggsave(paste(mainDirectory, "githubmetadata/lifetime.pdf", sep = ""), width = 4.5, height = 4.5)



#####Lifetime per commit
framework1=read.csv(paste(mainDirectory, "githubmetadata/android_metadata_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "githubmetadata/spring_metadata_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$lifetime/framework1$commits
dataFramework2=framework2$lifetime/framework2$commits
title = "Lifetime per commit"
verticalTitle = "Frequency of commits (log scale)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), lifetime/commits)
plotGraphic()
ggsave(paste(mainDirectory, "githubmetadata/lifetime_commits.pdf", sep = ""), width = 4.5, height = 4.5)



###### Versoes atual do framework Android
framework1=read.csv(paste(mainDirectory, "currentframeworkversion/android_currentframeworkversion_output.csv", sep = ""), sep=",",header=T)
table <- table(framework1$minSdkVersion)
dataframe <- data.frame(table)
subtipos = rep(c("TargetSdk", "MinSdk"), each=17)
apiLevel <- rep( dataframe$Var1, 2 )
values <- dataframe$Freq
df2 <- data.frame(supp=subtipos,dose=apiLevel,len=values)
p <- ggplot(data=df2, aes(x=dose, y=len, fill=supp)) +
  geom_bar(stat="identity", position=position_dodge()) +
  labs(title="Android Samples", x="API Level", y = "Number of Projects / Subprojects") +
  scale_fill_manual("", values = c("MinSdk" = "#87CEFA", "TargetSdk" = "#4682b4"))+
  theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18), legend.position = c(0.2, 0.80))
p
ggsave(paste(mainDirectory, "currentframeworkversion/androidAPILevel.pdf", sep = ""), width = 4.5, height = 4.5)



###### Versoes atual do framework Spring
framework1=read.csv(paste(mainDirectory, "currentframeworkversion/spring_currentframeworkversion_output.csv", sep = ""), sep=",",header=T)
table <- table(framework1$version)
dataframe <- data.frame(table)
p <- ggplot(data=dataframe, aes(x=Var1, y=Freq)) +
  geom_bar(stat="identity", position=position_dodge()) +
  labs(title="Spring Samples", x="Spring Version", y = "Number of Projects / Subprojects") +
  theme(plot.title=element_text(size=20, face = "bold"), axis.title=element_text(size=18),axis.text=element_text(size=18), legend.position = c(0.2, 0.80))
p
ggsave(paste(mainDirectory, "currentframeworkversion/springVersions.pdf", sep = ""), width = 4.5, height = 4.5)



####### Delay to update
framework1=read.csv(paste(mainDirectory, "delay/android_delay_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "delay/spring_delay_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$delay_in_days
dataFramework2=framework2$delay_in_days
title = "Delay to update"
verticalTitle = "Delay in days (log scale)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), delay_in_days+ 0.01)
plotGraphic()
ggsave(paste(mainDirectory, "delay/delay.pdf", sep = ""), width = 4.5, height = 4.5)



####### Mantenedores
framework1=read.csv(paste(mainDirectory, "maintainers/android_maintainers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "maintainers/spring_maintainers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$commom.sample
dataFramework2=framework2$commom.sample
title = "Framework Contributors Inside Code Sample Project"
verticalTitle = "Percent of Contributors"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), commom.sample+0.01)
plotGraphic()
ggsave(paste(mainDirectory, "maintainers/maintainers.pdf", sep = ""), width = 4.5, height = 4.5)



####### Imports
framework1=read.csv(paste(mainDirectory, "importcount/android_importcount_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "importcount/spring_importcount_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$imports.java_files
dataFramework2=framework2$imports.java_files
title = "Relative Distinct Framework Imports"
verticalTitle = "Imports"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), imports.java_files)
plotGraphic()
ggsave(paste(mainDirectory, "importcount/importcount.pdf", sep = ""), width = 4.5, height = 4.5)




###### RQ4

####### Relative ahead forks
framework1=read.csv(paste(mainDirectory, "forksahead/android_forks_ahead_by_projects_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "forksahead/spring_forks_ahead_by_projects_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$ratio * 100
dataFramework2=framework2$ratio * 100
title = "Relative Ahead Forks"
verticalTitle = "Percent of Ahead Forks"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), ratio * 100)
plotGraphic()
ggsave(paste(mainDirectory, "forksahead/relative_ahead_forks.pdf", sep = ""), width = 4.5, height = 4.5)



####### Number of Forks
framework1=read.csv(paste(mainDirectory, "forksahead/android_forks_ahead_by_projects_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "forksahead/spring_forks_ahead_by_projects_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$number_of_forks
dataFramework2=framework2$number_of_forks
title = "Number of Forks"
verticalTitle = "Percent of Ahead Forks"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), number_of_forks)
plotGraphic()
ggsave(paste(mainDirectory, "forksahead/number_of_forks.pdf", sep = ""), width = 4.5, height = 4.5)


############################# Stack Overflow ###########################################
######## reputation de quem pergunta sobre os code samples

framework1=read.csv(paste(mainDirectory, "stackoverflow/android_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "stackoverflow/spring_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$question_owner_reputation
dataFramework2=framework2$question_owner_reputation
title = "Reputação de quem\npergunta"
verticalTitle = "Reputação em escala log"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), question_owner_reputation)
plotGraphic()
ggsave(paste(mainDirectory, "stackoverflow/question_reputation.pdf", sep = ""), width = 4.5, height = 4.5)

framework1=read.csv(paste(mainDirectory, "stackoverflow/aws_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "stackoverflow/azure_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$question_owner_reputation
dataFramework2=framework2$question_owner_reputation
title = "Reputação de quem\npergunta"
verticalTitle = "Reputação em escala log"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName3, frameworkName4)), question_owner_reputation)
plotGraphic()
ggsave(paste(mainDirectory, "stackoverflow/question_reputation2.pdf", sep = ""), width = 4.5, height = 4.5)

######## reputation de quem tem respostas ACEITAS de perguntas sobre os code samples

framework1=read.csv(paste(mainDirectory, "stackoverflow/android_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "stackoverflow/spring_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$answer_owner_reputation
dataFramework2=framework2$answer_owner_reputation
title = "Reputação de quem\nresponde"
verticalTitle = "Reputação em escala log"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), answer_owner_reputation)
plotGraphic()
ggsave(paste(mainDirectory, "stackoverflow/answer_reputation.pdf", sep = ""), width = 4.5, height = 4.5)

framework1=read.csv(paste(mainDirectory, "stackoverflow/aws_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "stackoverflow/azure_questions_and_answers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$answer_owner_reputation
dataFramework2=framework2$answer_owner_reputation
title = "Reputação de quem\nresponde"
verticalTitle = "Reputação em escala log"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName3, frameworkName4)), answer_owner_reputation)
plotGraphic()
ggsave(paste(mainDirectory, "stackoverflow/answer_reputation2.pdf", sep = ""), width = 4.5, height = 4.5)


######## reputation de quem tem respostas NAO ACEITAS de perguntas sobre os code samples
framework1=read.csv(paste(mainDirectory, "allanswers/android_all_answers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "allanswers/spring_all_answers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$answer_owner_reputation
dataFramework2=framework2$answer_owner_reputation
title = "Reputação de quem\nresponde"
verticalTitle = "Reputação em escala log"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), answer_owner_reputation)
plotGraphic()
ggsave(paste(mainDirectory, "allanswers/answer_reputation1.pdf", sep = ""), width = 4.5, height = 4.5)

framework1=read.csv(paste(mainDirectory, "allanswers/aws_all_answers_output.csv", sep = ""), sep=",",header=T)
framework2=read.csv(paste(mainDirectory, "allanswers/azure_all_answers_output.csv", sep = ""), sep=",",header=T)
all=rbind.data.frame(framework1, framework2)
dataFramework1=framework1$answer_owner_reputation
dataFramework2=framework2$answer_owner_reputation
title = "Reputação de quem\nresponde"
verticalTitle = "Reputação em escala log"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName3, frameworkName4)), answer_owner_reputation)
plotGraphic()
ggsave(paste(mainDirectory, "allanswers/answer_reputation2.pdf", sep = ""), width = 4.5, height = 4.5)