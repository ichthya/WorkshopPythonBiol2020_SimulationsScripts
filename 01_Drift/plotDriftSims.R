#working directory
setwd("~/Dropbox/Carpentry/PalestraPython/Scripts/02_SteppingStone/")

#list of files in the working diretory witht the pattern driftedPop
f <- list.files(".", pattern = "driftedPop_Rep")
#creating an empty data frame
x <- data.frame(Generation = numeric(),
                q = numeric(),
                population = numeric(),
                PopSize = numeric())

#for loop to read all the files and merge them in a single data frame x
for (i in f){
  x_temp <- read.csv(i, header = 0)
  #creates a column with the population size that we obtained from the file name
  x_temp[,4] <- as.numeric(gsub(".csv", "",gsub("driftedPop_Rep10_N", "", i)))
  x <- rbind(x, x_temp)
}

#giving names to columns
names(x) <- c("generation","q","population","PopSize")
#calculating the frequency for the other allele
x$p <- 1 - x$q

#graphing
library(ggplot2)
png("../../Figures/DriftPlot.png", res = 300, units = "in", width = 7, height = 5)
  ggplot(data = x, aes(x = generation, y = p, col = as.factor(PopSize), 
                       group = interaction(population, PopSize)))+
    geom_line()+
    theme_bw()+
    scale_x_continuous("Generation", expand = c(0, 0)) + 
    scale_y_continuous("Allele Frequency", limits = c(0,1), expand = c(0, 0))+
    scale_colour_brewer("Population Size", palette = "Set1")
dev.off()
