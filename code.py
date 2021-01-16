import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics

dicelist = []
count = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dicelist.append(dice1 + dice2)
    count.append(i)

mean = statistics.mean(dicelist)
median = statistics.median(dicelist)
mode = statistics.mode(dicelist)
sd = statistics.stdev(dicelist)

print("mean = ", mean)
print("median = ", median)
print("mode = ", mode)
print("Standard Deviation: ",sd)

#fig = ff.create_distplot([dicelist], ["Result"], show_hist = False)
#fig.show()

first_sd_start, first_sd_end = mean-sd, mean+sd
second_sd_start, second_sd_end = mean-(2*sd), mean+(2*sd)
third_sd_start, third_sd_end = mean-(3*sd), mean+(3*sd)

list_data_1_sd = [result for result in dicelist if result > first_sd_start and result < first_sd_end]
print("Data that lies between the first standard deviation = ", format(len(list_data_1_sd)*100/len(dicelist)))

list_data_2_sd = [result for result in dicelist if result > second_sd_start and result < second_sd_end]
print("Data that lies between the second standard deviation = ", format(len(list_data_2_sd)*100/len(dicelist)))

list_data_3_sd = [result for result in dicelist if result > third_sd_start and result < third_sd_end]
print("Data that lies between the third standard deviation = ", format(len(list_data_3_sd)*100/len(dicelist)))