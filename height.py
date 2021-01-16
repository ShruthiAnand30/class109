import csv
import pandas as pd
import statistics

df = pd.read_csv("data.csv")

heightList = df["Height(Inches)"].to_list()
weightList = df["Weight(Pounds)"].to_list()

heightMean = statistics.mean(heightList)
weightMean = statistics.mean(weightList)

heightMode = statistics.mode(heightList)
weightMode = statistics.mode(weightList)

heightMedian = statistics.median(heightList)
weightMedian = statistics.median(weightList)

heightSD = statistics.stdev(heightList)
weightSD = statistics.stdev(weightList)

print("The Height mean = ", heightMean, "    The Weight Mean = ", weightMean)
print("The Height median = ", heightMedian, "    The Weight Median = ", weightMedian)
print("The Height mode = ", heightMode, "    The Weight Mode = ", weightMode)
print("The Standard Deviation = ", heightSD, "    The Standard Deviation = ", weightSD)

height_first_sd_start, height_first_sd_end = heightMean-heightSD, heightMean+heightSD
height_second_sd_start, height_second_sd_end = heightMean-(2*heightSD), heightMean+(2*heightSD)
height_third_sd_start, height_third_sd_end = heightMean-(3*heightSD), heightMean+(3*heightSD)

height_list_1_sd = [result for result in heightList if result > height_first_sd_start and result < height_first_sd_end]
print("Data that lies between the first standard deviation = ", format(len(height_list_1_sd)*100/len(heightList)))

height_list_2_sd = [result for result in heightList if result > height_second_sd_start and result < height_second_sd_end]
print("Data that lies between the second standard deviation = ", format(len(height_list_2_sd)*100/len(heightList)))

height_list_3_sd = [result for result in heightList if result > height_third_sd_start and result < height_third_sd_end]
print("Data that lies between the third standard deviation = ", format(len(height_list_3_sd)*100/len(heightList)))