library(ggplot2)
library(scales)

typeOfFramework = "Code Samples"
frameworkName1 = "android"
frameworkName2 = "spring"
factorPositionMedianLabel = 1.4
mainDirectory = "../"

plotGraphic <- function ()  {
  p1 <- ggplot(all, aes) + 
    scale_y_log10() +
    geom_violin(width=1, trim=TRUE, fill="#87CEFA") + 
    geom_boxplot(width=0.7,alpha=0.7) + ggtitle(title) + xlab(typeOfFramework) + ylab(verticalTitle) + 
    annotate("text", x = 1, y = framework1_median*factorPositionMedianLabel, label = framework1_median, size = 8) + annotate("text", x = 2, y = framework2_median*factorPositionMedianLabel, label = framework2_median, size = 8) +
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
ggsave("../githubmetadata/stars.pdf", width = 4.5, height = 4.5)


#### Commits
dataFramework1=framework1$commits
dataFramework2=framework2$commits
title = "Number of Commits"
verticalTitle = "Number of Commits (log scale)"
framework1_median = median(unlist(dataFramework1), na.rm = TRUE)
framework2_median = median(unlist(dataFramework2), na.rm = TRUE)
aes = aes(factor(framework,levels = c(frameworkName1, frameworkName2)), commits)
plotGraphic()
ggsave("../githubmetadata/commits.pdf", width = 4.5, height = 4.5)



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
ggsave("../numberofextensionfile/files.pdf", width = 4.5, height = 4.5)

