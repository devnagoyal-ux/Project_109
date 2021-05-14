import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
math_score_list = df["math score"].to_list()
reading_score_list = df["reading score"].to_list()
#Mean for height and Weight
math_score_mean = statistics.mean(math_score_list)
reading_score_mean = statistics.mean(reading_score_list)

math_score_median = statistics.median(math_score_list)
reading_score_median = statistics.median(reading_score_list)

math_score_mode = statistics.mode(math_score_list)
reading_score_mode = statistics.mode(reading_score_list)

print("Mean, Median and Mode of math_score is {}, {} and {} respectively".format(math_score_mean, math_score_median, math_score_mode))
print("Mean, Median and Mode of reading_score is {}, {} and {} respectively".format(reading_score_mean, reading_score_median, reading_score_mode))

math_score_std_deviation = statistics.stdev(math_score_list)
weight_std_deviation = statistics.stdev(reading_score_list)

math_score_first_std_deviation_start, height_first_std_deviation_end = math_score_mean-math_score_std_deviation, math_score_mean+math_score_std_deviation
math_score_second_std_deviation_start, height_second_std_deviation_end = math_score_mean-(2*math_score_std_deviation), math_score_mean+(2*math_score_std_deviation)
math_score_third_std_deviation_start, height_third_std_deviation_end = math_score_mean-(3*math_score_std_deviation), math_score_mean+(3*math_score_std_deviation)

reading_score_first_std_deviation_start, weight_first_std_deviation_end = reading_score_mean-weight_std_deviation, reading_score_mean+weight_std_deviation
reading_score_second_std_deviation_start, weight_second_std_deviation_end = reading_score_mean-(2*weight_std_deviation), reading_score_mean+(2*weight_std_deviation)
reading_score_third_std_deviation_start, weight_third_std_deviation_end = reading_score_mean-(3*weight_std_deviation), reading_score_mean+(3*weight_std_deviation)

math_score_list_of_data_within_1_std_deviation = [result for result in math_score_list if result > math_score_first_std_deviation_start and result < height_first_std_deviation_end]
math_score_list_of_data_within_2_std_deviation = [result for result in math_score_list if result > math_score_second_std_deviation_start and result < height_second_std_deviation_end]
math_score_list_of_data_within_3_std_deviation = [result for result in math_score_list if result > math_score_third_std_deviation_start and result < height_third_std_deviation_end]

reading_score_list_of_data_within_1_std_deviation = [result for result in reading_score_list if result > reading_score_first_std_deviation_start and result < weight_first_std_deviation_end]
reading_score_list_of_data_within_2_std_deviation = [result for result in reading_score_list if result > reading_score_second_std_deviation_start and result < weight_second_std_deviation_end]
reading_score_list_of_data_within_3_std_deviation = [result for result in reading_score_list if result > reading_score_third_std_deviation_start and result < weight_third_std_deviation_end]

print("{}% of data for math_score lies within 1 standard deviation".format(len(math_score_list_of_data_within_1_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for math_score lies within 2 standard deviations".format(len(math_score_list_of_data_within_2_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for math_score lies within 3 standard deviations".format(len(math_score_list_of_data_within_3_std_deviation)*100.0/len(math_score_list)))
print("{}% of data for math_score lies within 1 standard deviation".format(len(reading_score_list_of_data_within_1_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for math_score lies within 2 standard deviations".format(len(reading_score_list_of_data_within_2_std_deviation)*100.0/len(reading_score_list)))
print("{}% of data for math_score lies within 3 standard deviations".format(len(reading_score_list_of_data_within_3_std_deviation)*100.0/len(reading_score_list)))