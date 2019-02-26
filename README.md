# Problems

1. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

2. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

    Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

3. Take a list, say for example this one:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list that are less than 5.

    Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

4. Create a program that asks the user for a number and then prints out a list of all the divisors of    that number. (If you don’t know what a divisor is, it is a number that divides evenly into another    number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)   

5. Take two lists, say for example these two:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

    Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


6.  Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome     is a string that reads the same forwards and backwards.)  

7. Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write    one line of Python that takes this list a and makes a new list that has only the even elements of     this list in it.

8. Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

9. Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

10. Take two lists, say for example these two:

	    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. 
 
11. you are given a dataset of N students belonging to the same class.
    The data contains name of the student followed by marks they scored in five subjects which are Physics, Chemsistry, Maths, English, Hindi.
    Your task is find the average marks of the class for each individual subject.

    Input Format
        First line will contain an Integer N, denoting  the number of students in the class.
        Each of the Next N lines will contain a string S denoting the student name, followed by five integers m1, m2, m3, m4, m5 denoting the marks scored in each subject.

    Constraints
        1 <= N <= 10^3
        1 <= S <= 10^2
        0 <= m1, m2, m3, m4, m5 <= 100

    Output Format
        You have to print average marks upto two decimal places for each subject followed by a space. 

    Sample TestCase 1
    
        Input
        2

        arpit 100 75 40 56 53
        anushka 100 100 76 100 100
        
        Output
        100.00 87.50 58.00 78.00 76.50    