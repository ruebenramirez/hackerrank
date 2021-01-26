Hacker Rank - 30 Days of Code challenge - Day 12

https://www.hackerrank.com/challenges/30-inheritance/problem

Objective
Today, we're delving into Inheritance. Check out the attached tutorial for learning materials and an instructional video.

Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:
----------------------------------------------------

* A Student class constructor, which has 4 parameters:
	* A string, _firstName_.
	* A string, _lastName_.
	* An integer, _idNumber_.
	* An integer array (or vector) of test scores, _scores_.
* A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

Grading scale:
-------------

| Letter | Average (a) |
| ------ | ----------- |
| O      | 90 <= a <= 100 |
| E      | 80 <= a < 90 |
| A      | 70 <= a < 80 |
| P      | 55 <= a < 70 |
| D      | 40 <= a < 55 |
| T      | a < 40 |


Constraints
-----------

* 1 <= length of _firstName_, length of _lastName_ <= 10
* length of _idNumber_ ≡ 7
* 0 <= _score_ <= 100


Output Format
-------------

Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate() method are properly implemented.


Sample Input
------------

```
Heraldo Memelli 8135627
2
100 80
```


Sample Output
-------------

```
 Name: Memelli, Heraldo
 ID: 8135627
 Grade: O
```


Explanation
-----------

This student had 2 scores to average: 100 and 80. The student's average grade is `(100+80)/2 = 90`. An average grade of 90 corresponds to the letter grade _O_, so the calculate() method should return the character 'O'.



How to run the code
-------------------

```
make run
```
