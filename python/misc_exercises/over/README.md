Create a function named `is_over_13` that takes a `datetime` and returns whether or not the difference between that `datetime` and today is 4745 days or more.

Then, create a function named `date_string` that takes a datetime and returns a string like "May 20" (using `strftime`). The format string is `"%B %d"`.

Finally, make a variable named `birth_dates`. Use `map()` and `filter()`, along with your two functions, to create date strings for every datetime in birthdays so long as the datetime is more than 13 years old.
