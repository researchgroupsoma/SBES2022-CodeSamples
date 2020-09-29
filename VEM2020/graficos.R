library(ggplot2)
library(scales)

typeOfFramework = "Code Samples"
frameworkName1 = "Android"
frameworkName2 = "Spring"
frameworkName3 = "AWS"
frameworkName4 = "Azure"
factorPositionMedianLabel = 3
mainDirectory = "C:\\Users\\dudur\\Documents\\gabrielsmenezes\\pesquisamestrado\\"
output_width = 3.5
output_height = 2.5
size = 5

point <- format_format(big.mark = ".", decimal.mark = ",", scientific = FALSE)


plotGraphic <- function ()  {
  p1 <- ggplot(all, aes) + 
    scale_y_log10(labels = comma) +
    geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
    geom_boxplot(width=0.7,alpha=0.7) + ggtitle(title) + xlab(typeOfFramework) + ylab(verticalTitle) + 
    annotate("text", x = 1, y = framework1_median*factorPositionMedianLabel, label = point(round(framework1_median, 2)), size = size) + 
    annotate("text", x = 2, y = framework2_median*factorPositionMedianLabel, label = point(round(framework2_median, 2)), size = size) +
    annotate("text", x = 3, y = framework3_median*factorPositionMedianLabel, label = point(round(framework3_median, 2)), size = size) +
    annotate("text", x = 4, y = framework4_median*factorPositionMedianLabel, label = point(round(framework4_median, 2)), size = size) +
    theme(plot.title=element_text(size=12,face="bold") ,axis.title=element_text(size=10),axis.text=element_text(size=10))
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
verticalTitle = "Arquivos Java (log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), numberOfJavaFiles)
plotGraphic()
ggsave(paste(mainDirectory, "VEM2020\\java-files.pdf", sep = ""), width = output_width, height = output_height)



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
verticalTitle = "Linhas de Código (log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), CountLineCode/numberOfJavaFiles)
plotGraphic()
ggsave(paste(mainDirectory, "VEM2020\\loc.pdf", sep = ""), width = output_width, height = output_height)



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
verticalTitle = "Complexidade (log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), (SumCyclomaticStrict/CountDeclMethod))
plotGraphic()
ggsave(paste(mainDirectory, "VEM2020\\cc.pdf", sep = ""), width = output_width, height = output_height)



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
verticalTitle = "Readability (log)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
framework3_median = median(unlist(dataFramework3), na.rm = TRUE)
framework4_median = median(unlist(dataFramework4), na.rm = TRUE)

aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2, frameworkName3, frameworkName4)), readability * 100)
plotGraphic()
ggsave(paste(mainDirectory, "VEM2020\\readability.pdf", sep = ""), width = output_width, height = output_height)


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
ggsave(paste(mainDirectory, "VEM2020\\question-reputation.pdf", sep = ""), width = output_width, height = output_height)


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
ggsave(paste(mainDirectory, "VEM2020\\accepted-answer-reputation.pdf", sep = ""), width = output_width, height = output_height)


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
ggsave(paste(mainDirectory, "VEM2020\\all-answer-reputation.pdf", sep = ""), width = output_width, height = output_height)







###### Grafico de pizza #####
##### Android ##############




df <- data.frame(
  group = c("Import", "Running", "Reference", "Modify"),
  value = c(5.69, 11.95, 32.26, 50.09)
)

head(df)


blank_theme <- theme_minimal()+
  theme(
    axis.title.x = element_blank(),
    axis.title.y = element_blank(),
    panel.border = element_blank(),
    panel.grid=element_blank(),
    axis.ticks = element_blank(),
    plot.title=element_text(size=14, face="bold")
  )


# Use brewer palette
pie + scale_fill_brewer("Blues") + blank_theme +
  theme(axis.text.x=element_blank())+
  geom_text(aes(y = value + c(0, cumsum(value)[-length(value)]),label = value), size=5)









library(ggplot2)
library(dplyr)

df <- data.frame(Make=c('toyota','toyota','honda','honda','jeep','jeep','jeep','accura','accura'),
                 Model=c('camry','corolla','city','accord','compass', 'wrangler','renegade','x1', 'x3'),
                 Cnt=c(10, 4, 8, 13, 3, 5, 1, 2, 1))
dfc <- df %>%
  group_by(Make) %>%
  summarise(volume = sum(Cnt)) %>%
  mutate(share=volume/sum(volume)*100.0) %>%
  arrange(desc(volume))

bp <- ggplot(dfc[c(1:10),], aes(x="", y= share, fill=Make)) +
  geom_bar(width = 1, stat = "identity")
pie <- bp + coord_polar("y")
pie




ggplot(dfc, aes("", share, fill = Make)) +
  geom_bar(width = 1, size = 1, color = "white", stat = "identity") +
  coord_polar("y") +
  geom_text(aes(label = paste0(round(share), "%")), 
            position = position_stack(vjust = 0.5)) +
  labs(x = NULL, y = NULL, fill = NULL, 
       title = "market share") +
  guides(fill = guide_legend(reverse = TRUE)) +
  scale_fill_manual(values = c("#ffd700", "#bcbcbc", "#ffa500", "#254290")) +
  theme_classic() +
  theme(axis.line = element_blank(),
        axis.text = element_blank(),
        axis.ticks = element_blank(),
        plot.title = element_text(hjust = 0.5, color = "#666666"))














df = data.frame("brand" = c("Samsung","Huawei","Apple","Xiaomi","OPPO","Other"),"share" = c(.2090,.1580,.1210,.0930,.0860,.3320))


library(ggplot2)

# Create a basic bar
pie = ggplot(df, aes(x="", y=share, fill=brand)) + geom_bar(stat="identity", width=1)

# Convert to pie (polar coordinates) and add labels
pie = pie + coord_polar("y", start=0) + geom_text(aes(label = paste0(round(value*100), "%")), position = position_stack(vjust = 0.5))

# Add color scale (hex colors)
pie = pie + scale_fill_manual(values=c("#55DDE0", "#33658A", "#2F4858", "#F6AE2D", "#F26419", "#999999")) 

# Remove labels and add title
pie = pie + labs(x = NULL, y = NULL, fill = NULL, title = "Phones - Market Share")

# Tidy up the theme
pie = pie + theme_classic() + theme(axis.line = element_blank(),
                                    axis.text = element_blank(),
                                    axis.ticks = element_blank(),
                                    plot.title = element_text(hjust = 0.5, color = "#666666"))




rdown.os = rdown %>% 
  filter(os != "NA") %>% 
  group_by(os) %>% 
  count() %>% 
  ungroup()%>% 
  arrange(desc(os)) %>%
  mutate(percentage = round(n/sum(n),4)*100,
         lab.pos = cumsum(percentage)-.5*percentage)


ggplot(data = df, 
       aes(x = "", y = value, fill = group))+
  geom_bar(stat = "identity")+
  coord_polar("y", start = 200) +
  geom_text(aes(y = value, label = paste(value,"%", sep = "")), col = "black") +
  theme_void() +
  scale_fill_brewer(palette = "Blues")
