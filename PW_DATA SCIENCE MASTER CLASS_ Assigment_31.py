#!/usr/bin/env python
# coding: utf-8

# # Assignment_07.03.2023(Basic Statistic-2)

# ## Q1.What are the three measures of Central tendency?
# 
# ### Ans:-
# 
#     The central Tendency refer to the measure used to determine the "CENTRE" of the distribution of data.
# 
#     The three measures of central tendency are:
# 
#     1.Mean:- It is the most common measure of central tendency, calculated by adding up all the values in a dataset and 
#            dividing the sum by the total number of values.
# 
#     2.Median:- The median is the middle value of a dataset when it is arranged in ascending or descending order. In other 
#               words, it is the value that separates the highest and lowest values in the dataset.
# 
#     3.Mode:- The mode is the most frequently occurring value in a dataset. It can be more than one if there are multiple 
#             values that occur with the same frequency.
# 
# 
# 
# 
# 

# ## Q2. What is the different between the mean,median and mode ? How are they used to measure the central tendency of a dataset?
# 
# ### Ans:-
# 
#     Mean, median, and mode are all measures of central tendency, but they each describe different aspects of a dataset.
# 
#     The mean is the sum of all the values in a dataset, divided by the total number of values. It is sensitive to outliers
#     and extreme values in a dataset, and can be heavily influenced by them. The mean is often used to describe the typical
#     value of a variable in a dataset.
# 
#     The median is the middle value of a dataset when it is arranged in ascending or descending order. It is less sensitive 
#     to outliers and extreme values than the mean, and can give a better representation of the "typical" value in a skewed
#     dataset. The median is often used when the dataset has extreme values that can skew the mean.
# 
#     The mode is the most frequently occurring value in a dataset. It is used to describe the most common value or category
#     in a dataset. The mode is useful for categorical or nominal data where the values can't be arranged in ascending or 
#     descending order.
# 
#     All three measures can be used to describe the central tendency of a dataset, depending on the type of data and the 
#     purpose of the analysis. Mean is used for interval and ratio data, median is used for ordinal data and when there are
#     outliers or extreme values in a dataset, and mode is used for nominal and categorical data.
# 
# 
# 
# 
#             

# ## Q3. Measure the three measures of central tendency for the given height data:
# ##       [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
# 
# ### Ans:-
#  
#  1. MEAN - height data [172.5+175+175+176+176.2+176.5+177+177+177+178+178.2+178.9+178+178+179+180] = 2832.3/16= 177.01
#  
#  2. MEDIAN - height data [172.5+175+175+176+176.2+176.5+177+177+177+178+178.2+178.9+178+178+179+180] = Middiel number =177
#  
#  3. MODE - height data [172.5+175+175+176+176.2+176.5+177+177+177+178+178.2+178.9+178+178+179+180]= most frequent number = 177
#                          
#  
# 

# ## Q4. Find the standard deviation for the given data:
# ##        [172.5+175+175+176+176.2+176.5+177+177+177+178+178.2+178.9+178+178+179+180] 
# 
# ### Ans:-
#           First we have calculate the mean of the above data set.
#           [172.5+175+175+176+176.2+176.5+177+177+177+178+178.2+178.9+178+178+179+180]=2832.3
#           Numner of integer =16
#           then Mean = 2832.3/16=177.01 ~ 177
#           
#           Second we have calculate the variance of the above data set by using mean value, which have calculate on above.
#           ((172.5-177)^2+(175-177)^2+(176-177)^2+(176.2-177)^2+(176.6-177)^2+(177-177)^2+(177-177)^2+(177-177)^2+
#           (178-177)^2+(178.2-177)^2+(178.9-177)^2+(178-177)^2+(178-177)^2+(179-177)^2+(180-177)^2)/16 = 3.2
#           
#           Finally Calculation of Standard Daviation is Sqrt of Variances.
#           so that Sqrt(variance) then Sqrt(3.2)= 1.78
#           
#           The Final answer of standard deviation of the above data set is 1.78..
#           

# ## Q5. How to measure of dispersion such as range,variance, and standard deviation used to describe the spread of a data set? Provide an example.
# 
# ### Ans:-
# 
#        Measures of dispersion such as range, variance, and standard deviation are used to describe.
#        
#        Range: The range is the difference between the highest and lowest values in a dataset. It gives an idea of how spread
#               out the data is, but it can be influenced heavily by outliers. For example, suppose we have the following 
#               dataset of exam scores: 75, 80, 85, 90, 95. The range would be 95 - 75 = 20.
#               
#       Variance: The variance is the average of the squared differences of each value from the mean. It measures how far each
#                 value in the dataset is from the mean. A higher variance indicates that the data is more spread out. For 
#                 example, suppose we have the following dataset of exam scores: 75, 80, 85, 90, 95. The mean would be 
#                 (75+80+85+90+95)/5 = 85. The variance would be ((75-85)^2 + (80-85)^2 + (85-85)^2 + (90-85)^2 + (95-85)^2)/5
#                 = 100.
#                 
#       Standard deviation: The standard deviation is the square root of the variance. It is a commonly used measure of
#                           dispersion as it is in the same units as the original data, and it is easier to interpret than 
#                           the variance. For example, suppose we have the same dataset of exam scores as in the variance
#                           example. The standard deviation would be the square root of the variance, i.e., sqrt(100) = 10.
# 
# 

# ## Q6. What is a Venn Diagram?
# 
# ### Ans:- 
#     A Venn diagram is a graphical representation of sets, often used in mathematics and logic to visually display the
#     relationships between different groups of items or concepts.
#     
#     It consists of one or more circles or ovals, with each circle representing a set or group of items, and the area inside
#     the circle representing all the elements in that set. The overlapping regions of the circles represent the intersection
#     of the sets, which includes all the elements that belong to both sets.
#     
#     Venn diagrams can be used to represent complex relationships between multiple sets, and they are often used in 
#     statistics, logic, and data analysis to help visualize and understand complex data sets.

# ## Q7. For two given sets A=(2,3,4,5,6,7) & B=(0,2,6,8,10) find:
# 
# ### Ans:- 
#             (i)  = A ∩ B  = (2,6) Intersection = common data in both data sets
#             (ii) = A U bB = (0,2,3,4,5,6,7,8,10) union = combines all the elements of set A and set B into a single set
#                                                          all data in both set of only unique( not allow duplicate)

# ## Q8. What do you understand about skewness in data?
# 
# ### Ans:-
#         Skewness is a measure of the asymmetry of a probability distribution or a dataset. In other words, it indicates the
#         degree to which a dataset deviates from a normal distribution, which is perfectly symmetrical.
#         
#         If a dataset is skewed, it means that it has a longer tail on one side of the distribution than on the other side.
#         This can be caused by the presence of outliers, or by the fact that the data is naturally distributed in a 
#         non-normal way. There are three main types of skewness:-
#         
#         1. Positive skewness: This occurs when the tail of the distribution is on the right-hand side, and the majority of
#                               the data is concentrated on the left-hand side.
#         2. Negative skewness: This occurs when the tail of the distribution is on the left-hand side, and the majority of 
#                               the data is concentrated on the right-hand side.
#         3. Zero skewness:     This occurs when the distribution is perfectly symmetrical, with the same amount of data on 
#                               both sides.
#                               
#         Skewness is often measured using a statistic called the skewness coefficient, which indicates the extent and 
#         direction of skewness in the data. A skewness coefficient of 0 indicates a perfectly symmetrical distribution,
#         while positive or negative values indicate positive or negative skewness, respectively.

# ## Q9. If the data is right skewed then what will be the position of median with respected of mean?
# 
# ### Ans:-
#         If a data set is right-skewed, then the mean will be larger than the median. This is because the mean is sensitive 
#         to outliers and is influenced by the larger values in the right tail of the distribution, whereas the median is not
#         as affected by extreme values and is based solely on the middle value(s) of the data set.
# 
#         To understand this concept better, imagine a dataset with a right-skewed distribution, such as income or wealth. 
#         In this case, there may be a few individuals with very high incomes or wealth, while most people have lower incomes
#         or wealth. When we calculate the mean, these high values will have a greater impact on the final value, pulling it
#         towards the right, whereas the median will be closer to the middle of the distribution, where most of the data 
#         points are located.
#         
#         Therefore, the median will be to the left of the mean in a right-skewed distribution.

# ## Q10.Explain the different between covariance and correlation.How are these measure used in statistic analysis?
# 
# ### Ans:-
#     Covariance and correlation are two commonly used measures in statistics to describe the relationship between two 
#     variables. While both measures are used to describe the extent to which two variables are related, they differ in 
#     how they do so.
# 
#     Covariance measures the degree to which two variables vary together. Specifically, it measures the average of the 
#     product of the deviations of two variables from their respective means. The covariance can be positive, indicating 
#     that the two variables move in the same direction, or negative, indicating that they move in opposite directions. 
#     However, the magnitude of covariance is difficult to interpret, as it depends on the scale of the variables.
#     
#     On the other hand, correlation is a standardized measure of the linear relationship between two variables. Correlation
#     is obtained by dividing the covariance of two variables by the product of their standard deviations. Correlation values
#     range from -1 to +1, where -1 indicates a perfect negative correlation, +1 indicates a perfect positive correlation, 
#     and 0 indicates no correlation. Correlation coefficients have a clear interpretation and are independent of the scale
#     of measurement.
#     
#     Covariance is used in statistical analysis to determine the relationship between two variables, but it is not always 
#     clear whether the relationship is positive or negative. Correlation, on the other hand, provides a more intuitive
#     understanding of the strength and direction of the relationship between two variables. Both measures are used in 
#     regression analysis, hypothesis testing, and exploratory data analysis. However, correlation is often preferred due
#     to its ease of interpretation and ability to compare the strength of the relationships between variables on different
#     scales.
#       

# ## Q11. What is the formula for calculating the  sample mean?Provide an example calculation for a dataset.
# 
# ### Ans:-
#             The formula for calculating the sample mean, also known as the arithmetic mean, is:
# 
#             Sample mean = (sum of all values in the sample) / (number of values in the sample)
# 
#             Here's an example calculation for a dataset:
# 
#             Consider the following dataset of 7 values: 2, 4, 6, 8, 10, 12, 14.
# 
#             To find the sample mean, we first sum up all the values:
# 
#             2 + 4 + 6 + 8 + 10 + 12 + 14 = 56
# 
#             Next, we divide the sum by the number of values in the sample, which in this case is 7:
# 
#             Sample mean = 56 / 7 = 8
# 
#            Therefore, the sample mean for this dataset is 8.

# ## Q12. For a normal distribution data what is the relationship between its measure of central tendency?
# 
# ### Ans:-
#         For a normal distribution, the three main measures of central tendency, which are the mean, median, and mode, are 
#         equal to each other. This means that the peak of the normal distribution (which represents the mode), the middle of
#         the distribution (which represents the median), and the balance point of the distribution (which represents the mean)
#         all coincide at the same value.
# 
#         This property of a normal distribution is a consequence of its symmetrical bell-shaped curve, where the data is 
#         evenly distributed on both sides of the mean. As a result, the mean, median, and mode are all located at the center 
#         of the distribution, and their values are equal to each other.
# 
#        Therefore, in a normal distribution, the mean, median, and mode are the same, and they all represent the typical or 
#        central value of the dataset.

# ## Q13.How is Covariance different from Correlation?
# 
# ### Ans:-
# 
#         Covariance and correlation are both statistical measures that describe the relationship between two variables. 
#         However, there are several key differences between them:
#         
#         1.Definition:- Covariance measures how two variables vary together, or in other words, it measures the degree to 
#                        which two variables are linearly associated. Correlation, on the other hand, measures both the 
#                        strength and the direction of the linear relationship between two variables.
#                        
#         2.Range:-      Covariance values can range from negative infinity to positive infinity, which makes it difficult to
#                        interpret the strength of the relationship between the two variables. In contrast, correlation values                          always range from -1 to 1, where a value of -1 indicates a perfect negative correlation, a value of 0                          indicates no correlation,and a value of 1 indicates a perfect positive correlation.
# 
#        3.Unit of measurement:-Covariance is a measure that is affected by the scale of the variables. This means that the
#                               magnitude of the covariance will depend on the units in which the variables are measured. 
#                               Correlation, on the other hand, is a unitless measure, which makes it easier to compare the 
#                               strength of the relationship between variables that are measured in different units.
# 
#        4.Interpretation:-Covariance does not provide a clear interpretation of the strength and direction of the 
#                          relationship between two variables, whereas correlation provides a more intuitive interpretation.
#                          A correlation coefficient of -1 or 1 indicates a strong linear relationship, whereas a correlation
#                          coefficient of 0 indicates no linear relationship between the variables.
# 
#                                                     In summary, covariance measures the degree to which two variables are
#                          linearly associated, whereas correlation measures both the strength and the direction of the 
#                          linear relationship between two variables. Correlation is a standardized measure that is unitless
#                          and provides a more intuitive interpretation of the relationship between variables.
# 
# 

# ## Q14. How do outliers affected measure of central tendency and dispersion ?provide an example.
# 
# ### Ans:-
# 
#             Outliers can have a significant impact on both measures of central tendency and measures of dispersion.
#             A single outlier can skew the mean and median, making them less representative of the data. Similarly, 
#             outliers can also have a significant impact on measures of dispersion such as the range, variance, and 
#             standard deviation.
# 
#                 For example, consider the following dataset of exam scores:
#                 Score = [65,70,72,74,75,76,78,80,82,85,90]
#                 
#                 The mean of this dataset is 76.7, the median is 76, and the range is 25. However, if we introduce an 
#                 outlier score of 100, the mean increases to 81.8, the median remains the same, but the range increases
#                 to 35. This demonstrates how a single outlier can have a significant impact on the mean and range, while
#                 the median remains relatively unchanged.
#                 
#                 Similarly, outliers can also impact measures of dispersion such as the variance and standard deviation. 
#                 In this example, the variance of the dataset is 81.21 and the standard deviation is 9.01. If we introduce
#                 the outlier score of 100, the variance increases to 375.6 and the standard deviation increases to 19.38. 
#                 This demonstrates how outliers can increase the variability of the data and make it more difficult to 
#                 interpret.
# 
#     In summary, outliers can have a significant impact on both measures of central tendency and measures of dispersion. 
#     It is important to identify and handle outliers appropriately in order to accurately interpret and analyze data.
