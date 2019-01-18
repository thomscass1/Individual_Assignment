#Import the csv file and call it DRC
DRC <- read.csv("DRC_Conflict.csv")
view(DRC)

#Load tidyverse so you can 
library(tidyverse)


#Plot a bar graph
ggplot() + 
stat_count(data= DRC, mapping = aes(x = type_of_violence))

#Plot a bar graph for each year and group them by type_of_violence
ggplot() + 
  stat_count(data= DRC, mapping = aes(x = year))+ 
  facet_wrap(~type_of_violence, nrow=3)
#stat_count creates a bar graph

#Now get the frequency counts for all three types of violence
violence <-table(DRC$type_of_violence)
violence
#The command table() gives the counts of the variable type of violence
#... which was extracted from the DRC file 

