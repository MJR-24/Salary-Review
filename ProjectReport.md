# Salary-Review
An online salary review system for Title Boxing Club Franchisees.

My goal for this project was to tabulate the salary information of up to five Title Boxing Club employees.  The user needs to input the employee’s first and last name, 
their social security number, their annual salary, and what percentage of their salary goes towards retirement. 
Then there will be a prompt asking if there is another employee or not. If there is, then it will loop back to the top. If not, then it will stop and print the table. 

I implemented several checks so that the user is prevented from entering something incorrectly, including:
Making sure the SSN is nine digits long without any dashes.
Making sure the salary is a number.
Not allowing the user to include a percent sign with their retirement contribution.
Making sure the retirement percentage is between 0% and 40%

I chose to create the table using Lists because it was the simplest way to put it together, along with the ljust function. 
I also considered using Dictionaries, but that became convoluted very quickly and it just made more sense to use Lists.

I utilized many loops to gather the information with the most common being While loops. Many If loops were also used along with For loops. 
The loops were a crucial part of getting the information into the Lists and ensuring the program ran smoothly.
