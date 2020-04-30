# A-Simple-Quiz

Use of Functions

It is expected that there will be at least two distinct functions defined for this project, as specified for Homework 6.   Each function's purpose should be summarizable in one or two sentences.   The lecture slides indicated that a function should be fewer than 30 lines of code (or not much more than that), not counting documentation and blank linles.

Each function should have a meaningful name and meaningful parameters.   Each should have a docstring (using triple quotes) at minimum describing what the function does.   The complete interface should be clear from the function heading and its documentation.

The function certainly may define additional local variables to complete its task.  The parameter list should only contain values and variables that must be shared with its caller, and no other hidden communications (such as no global variables).

If your submitted project design seems insufficient to these expectations, you are certainly permitted (and encouraged) to improve upon it, since that will help you to complete the program on time.

In any case, any program that has _no_ functions defined, but does everything without functions (as Homeworks 1-4) will not earn full credit, even if it does otherwise work correctly.

Use of Data Files

The data files are intended to allow a great deal more flexibility in the application areas without having to modify the program code.   Each program is expected to get all of the content data from the data files.   The content is not to be hard-coded into the Python code itself.

To be more specific for the recommended projects:
-- quiz program: data file has all questions and all answers 
-- hangman: data file consists of the possible words to be guessed at 
-- madlib: data file consists of all the text and prompt words for the madlib

No other examples will be given here, since other projects are considered on a case by case basis, and should have been approved in advance. For those who still were not aware that this was not a completely open-ended design-your-own project, you may still need to find a way to assure that the program code is as unaware of data content as possible.

The program should prompt the user for the name of the data file.   Whether you require the user to type an extension (such as ".txt") or whether the program automatically adds the extension is up to you.   You may assume that the user running the program knows the name of an existing data file in that same folder.

If you wish to remove that assumption, and give a user a list of choices of available files, you may do so, for 10% Extra Credit.  This would require getting a list of files from the Operating System (consider the 'listdir' method in the 'os' module).  

Your program should not make any particular assumptions about the exact size of the data file.  It should just be able to read to the end of the file (the for loop can do that).  A recent recitation demonstrated that it is rather easy to identify how many file lines were actually found, and the program can then make use of that number.

Special Hints

Here are a few things that would make the assigned projects a little interesting, with some hints about how to go about them.

Quiz Program:

The Overview already suggested that this should be able to supply the questions in a random order, and the Blackjack recitation referred to a function that would be very helpful for that.

If there are a large number of questions, it might be appropriate to just pick a subset.  For example, a quiz about US state capitals should not ask about all 50 states, but maybe 10 or 15 of them.   You can use whatever means you wish to pick as a subset (such as 10, or 1/3 of the total, or some combination).   If there is a very short list of questions, however, it would make more sense to ask them all.

Hangman:

The Extra Credit portion to the posted solution to Homework 5 built up a solution string one letter at a time, much in the same way as Hangman does.  This modified answer is most easily done with a list, replacing letters into each position where it belongs, with the string join method allowing the answer to show up in a clean fashion.

Your program should take care of case-sensitivity, not treating 'a' and 'A' as separate letters.  Whether your answers are all upper case or lower case is up to you -- just make sure that the user at the keyboard gets the appropriate responses.

MadLib:

The most challenging portion here is presenting the final results.   Some portions of the text come directly from the data file; other portions are supplied by keyboard input.  But it would not be very readable to have each portion on its own output line.  On the other hand, it would also not be readable to have all the text disappear off the right side of the screen.

So the challenge here is to combine all of the pieces of text, and put them together in such a way that the length of each displayed line 'looks' good.

Here are three different strategies (and there may be others):

Create a long string using ' '.join(), then look for suitable string slices.   "string[i:j]" would be all the characters of the string from position i up to (but not including)  j.   You would pick a j as far beyond as i as you can get, such that j refers to a space character , and the substring would still fit in displayed line length (there is a function different from but closely related to 'index' than can help you).   The next string would have a starting position just after the space.
Create a long string, but then convert it to a list of individual characters.  Find the space characters that maximize how much you get for a line (that still fits) and then replace those ' ' characters with '\n'.   Then recreate a printable string with ''.join()
Build a line up, one word at a time, accepting the next word as it fits.   This algorithm is similar to the shopping problem in the midterm.
Submission Details

Submitting for this assignment will be slightly different from the other assignments.  You may or may not have noticed a "+ Add Another File" when submitting that you must make use of this time, so that at least three files will be submitted instead of just one.

Include at least these three items in your submission on Canvas:

The Python file (.py) containing your program solution
A data file of at least 10 lines (may be more), which would be representative of a typical input to your program
A 'small' data file (perhaps fewer than 6 lines) that would also be acceptable to your program
There are a couple reasons for requesting multiple data files:

It demonstrates the ability to read the data from any named file
It demonstrates that the program does not rely too much on hardcoded data
It shows that the program can flexibly react to files of different sizes
It allows the grader to run your program very quickly, using the small file, to improve grading time
Your program should, of course, not be aware of the exact content of the files you submit.   The graders should be free to make any change to the data file that might help them evaluate your program.

