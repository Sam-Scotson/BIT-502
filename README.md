<h1>Introduction

In this assessment, you will develop a Python console application, and design and develop a
prototype of a user interface design. 

The main objective of this assessment is to apply the
programming fundamentals experience used to design and develop business applications.

You need to submit your assessment in two files: the report as an MS Word file and the
Python code file as a zip file.
Read the following case study and complete the tasks.

<h1>Case study

City Gym has been in business for two years and is seeing a steady increase in the number of
members. The gym offers its members access to a standard range of exercise equipment
and personalised training. New members have an initial fitness assessment where their
personal fitness goals are set (for example, weight loss, toning, bulking up, improving
cardio), and soon after, a personal trainer takes them through their personalised fitness
programme.

City Gym also provides online fitness videos that clients can access. As the number of
members has increased, it has become more difficult to keep track of client information.
Currently, the owners have a rather old-fashioned approach to signing up new members.
A paper membership form would be provided to the customer (see Appendix A), and the
employee would calculate the fees manually using a calculator. The customer would then be
given one copy, and another copy would be stored in a filing cabinet.

City Gym is looking to purchase new computers for its employees and is interested in
pursuing a digital approach that will allow new members to sign up through the new
computer application. 

The new application would allow the user to enter all their personal
details as required from their current membership form and calculate their membership
costs. Further requirements:
• Convert a paper-based form into an electronic form (for submission purposes, you
must develop a console application only for Assessment 1, with a clear consideration
of the prototype).
• Before creating the actual form and applying functionality to it, first design a
prototype form.

Task 1: Create a Python console application

Write a Python console application that will satisfy the following requirements:
Part 1: Main menu
You need to create a main menu that allows the user to select from the following three
options:
• calculate body mass index (BMI)
• view membership cost
• exit the application.
(Part 1: 5 marks)

Part 2: BMI sub-menu

Question 1: Calculate BMI
Develop the Calculate BMI option that will prompt the user to enter their height and weight
and perform the calculation.

A sample BMI calculation is shown below for your reference:
BMI = weight (kg) / [height (m)]2
In two simple steps:
• multiply the height in metres (m) by itself
• divide the weight in kilograms (kg) by the step 1 result.
For example, an adult of 1.8 m tall and weighing 75 kg:
BMI step 1 = 1.8 × 1.8 = 3.24
BMI step 2 = 75 ÷ 3.24
BMI = 23.15
(Question 1: 15 marks)

Question 2: Display BMI result

The following information needs to be displayed as BMI result:
• If the BMI is under 18.5, then display the text ’Underweight’.
• If greater than or equal to 18.5 but less than 25, then display the text ’Normal’.
• If greater than or equal to 25 but less than 30, then display the text ’Overweight’.
• If 30 or above, then display the text ’Obese’.
(Question 2: 10 marks)
(Part 2 total: 25 marks)

Part 3: Membership sub-menu
Question 1: Membership selection
Develop the View Membership Rates option that takes input from the user about the type
of membership; that is, 1 for Basic, 2 for Regular and 3 for Premium.

(Question 1: 10 marks)

Question 2: Display membership cost
The following information needs to be displayed:
• Membership costs: $10 for Basic, $15 for Regular and $20 for Premium. Note that
these rates are weekly.
• Monthly membership cost, which is the weekly rate x 52 divided by 12.
(Question 2: 10 marks)
(Part 3 total: 20 marks)
Part 4: Navigation and exit options

In your Python console application:
• The user should be able to navigate between the main menu and carry out other
operations without needing to terminate the program.
• There should also be an option to exit or terminate at any stage when the program is
running. Refer to the flow chart (Fig. 1) for navigation between menus.
• If the input is wrong in any menu (that is, an invalid option has been entered other
than the valid options), an error message should be displayed. The flow should not
progress to the next step unless the correct option/value has been entered.
See the example below for a sample display.
