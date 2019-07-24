<style>
table, tr, td ,th {
    border:none !important;
	border-collapse:collapse
}
</style>
**Exercise 1:** Run the program on your system and see what numbers you get.   Run the program more than once and see what numbers you get.

	import random
	for i in range(10):
		x = random.random()
		print(x)  

**Exercise 2:** Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.  
**Exercise 3:** Move the function call back to the bottom and move the definition of print\_lyrics after the definition of repeat\_lyrics. What happens when you run this program?  

	def print_lyrics():  
		print("I'm a lumberjack, and I'm okay.")  
		print('I sleep all night and I work all day.')  
	 
	def repeat_lyrics():  
		print_lyrics()  
		print_lyrics()  
	
	repeat_lyrics()  

**Exercise 4:** What is the purpose of the “def” keyword in Python?  
a) It is slang that means “the following code is really cool”  
b) It indicates the start of a function  
c) It indicates that the following indented section of code is to be stored for later  
d) b and c are both true  
e) None of the above  

	D

**Exercise 5:** What will the following Python program print out?  
	
	def fred():  
		print("Zap")  

	def jane():  
		print("ABC")  

	jane()  
	fred()  
	jane()  

a) Zap ABC jane fred jane  
b) Zap ABC Zap  
c) ABC Zap jane  
d) ABC Zap ABC  
e) Zap Zap Zap  

	D

**Exercise 6:** Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).  
Enter Hours: 45  
Enter Rate: 10  
Pay: 475.0  

	Ans : ex6.py

**Exercise 7:** Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string. 
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

Run the program repeatedly to test the various different values for input.  

	Ans : ex7.py