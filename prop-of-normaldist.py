import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("height + weight.csv")
height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

height_mean = statistics.mean(height_list)
height_median = statistics.median(height_list)
height_mode = statistics.mode(height_list)

weight_mean = statistics.mean(weight_list)
weight_median = statistics.median(weight_list)
weight_mode = statistics.mode(weight_list)

print("mean, median, and mode of height is {}, {}, and {} respectively".format(height_mean, height_median, height_mode))
print("mean, median, and mode of weight is {}, {}, and {} respectively".format(weight_mean, weight_median, weight_mode))

height_standard_dev = statistics.stdev(height_list)
weight_standard_dev = statistics.stdev(weight_list)

# all the stuff to do with the heights

height_first_standard_dev_start, height_first_standard_dev_end = height_mean-height_standard_dev, height_mean + height_standard_dev
height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_standard_dev_start and result < height_first_standard_dev_end]

height_second_standard_dev_start, height_second_standard_dev_end = height_mean-(2*height_standard_dev), height_mean + (2*height_standard_dev)
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_standard_dev_start and result < height_second_standard_dev_end]

height_third_standard_dev_start, height_third_standard_dev_end = height_mean-(3*height_standard_dev), height_mean + (3*height_standard_dev)
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_standard_dev_start and result < height_third_standard_dev_end]

# all the stuff to do with the weights

weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean-weight_standard_dev, weight_mean + weight_standard_dev
weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result  < weight_first_std_deviation_end]

weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean - (2*weight_standard_dev), weight_mean + (2*weight_standard_dev)
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result  < weight_second_std_deviation_end]


weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean - (3*weight_standard_dev), weight_mean + (3*weight_standard_dev)
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start and result  < weight_third_std_deviation_end]


# printing the standard deviation heights and weights

# heights
print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))

fig = ff.create_distplot([height_list], ["List of Heights"], show_hist = False)
fig.add_trace(go.Scatter(x = [height_mean, height_mean], y = [0, 0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [height_first_standard_dev_start, height_first_standard_dev_start], y = [0, 0.17], mode = "lines", name = "standard deviation 1"))
fig.add_trace(go.Scatter(x = [height_first_standard_dev_end, height_first_standard_dev_end], y = [0, 0.17], mode = "lines", name = "standard deviation 1"))

fig.add_trace(go.Scatter(x = [height_second_standard_dev_start, height_second_standard_dev_start], y = [0, 0.17], mode = "lines", name = "standard deviation 2"))
fig.add_trace(go.Scatter(x = [height_second_standard_dev_end, height_second_standard_dev_end], y = [0, 0.17], mode = "lines", name = "standard deviation 2"))
fig.show()
# weights
print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))

fig1 = ff.create_distplot([height_list], ["List of Heights"], show_hist = False)

fig1.add_trace(go.Scatter(x = [weight_mean, weight_mean], y = [0, 0.17], mode = "lines", name = "height"))
fig1.add_trace(go.Scatter(x = [weight_first_std_deviation_start, weight_first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "standard deviation 1"))
fig1.add_trace(go.Scatter(x = [weight_first_std_deviation_end, weight_first_std_deviation_end], y = [0, 0.17], mode = "lines", name = "standard deviation 1"))

fig1.add_trace(go.Scatter(x = [weight_second_std_deviation_start, weight_first_std_deviation_start], y = [0, 0.17], mode = "lines", name = "standard deviation 2"))
fig1.add_trace(go.Scatter(x = [weight_second_std_deviation_end, weight_second_std_deviation_end], y = [0, 0.17], mode = "lines", name = "standard deviation 2"))

fig1.show()



