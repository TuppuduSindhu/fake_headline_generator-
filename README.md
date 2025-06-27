✅ Main Points of the Code:
1.Imports the random module

Used to select random items from lists.

2.Defines three lists

a.subjects: Characters or people (e.g., "prabhas", "virat kohli").

b.actions: Verbs (e.g., "eats", "declares war on").

c.places_or_things: Locations or events (e.g., "at railway station", "during ipl match").

3.Starts an infinite loop (while True)

4.Keeps generating headlines until the user decides to stop.

5.Randomly selects one item from each list

a.Uses random.choice() to pick a subject, action, and place/thing.

b.Creates a fake headline

c.Combines the chosen elements into a string using an f-string.

6.Prints the generated headline


7.Asks the user if they want another headline

a.Gets user input (yes or no) and uses .strip() to clean spaces.

b.Breaks the loop if the user enters "no"

8.Ends headline generation and exits the loop.

9.Prints a thank-you message at the end
