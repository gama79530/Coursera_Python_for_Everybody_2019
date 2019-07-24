<style>
table, tr, td ,th {
    border:none !important;
	border-collapse:collapse
}
</style>
**Exercise 1:** Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.  
Enter Hours: 45  
Enter Rate: 10  
Pay: 475.0  

	Ans : ex1.py

**Exercise 2:** Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:  
Enter Hours: 20  
Enter Rate: nine  
Error, please enter numeric input  
Enter Hours: forty  
Error, please enter numeric input  

	Ans : ex2.py

**Exercise 3:** Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table: 
<table>
	<tr>
		<th>Score</th><th>Grade</th>
	</tr>
	<tr>
		<td>&gt;= 0.9</td><td>A</td>
	</tr>
	<tr>
		<td>&gt;= 0.8</td><td>B</td>
	</tr>
	<tr>
		<td>&gt;= 0.7</td><td>C</td>
	</tr>
	<tr>
		<td>&gt;= 0.6</td><td>D</td>
	</tr>
	<tr>
		<td>&lt; 0.6</td><td>F</td>
	</tr>
</table>
Enter score: 0.95  
A  
Enter score: perfect  
Bad score  
Enter score: 10.0  
Bad score  
Enter score: 0.75  
C  
Enter score: 0.5  
F  
Run the program repeatedly as shown above to test the various different values for input.

	Ans : ex3.py