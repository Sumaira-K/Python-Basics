# style of the code is subjective
"""PEP 8 is Python Enhancement Proposal is a set of proposals that
community within the world of Python typically to not only peopose
new ideas, but also to codify ultimately certain standards and PEP 8
happens to be such a proposal that standardize or rather try to
standardize what our code should look like, a code that is not only
correct but also well-designed and properly formatted and readable."""

""" Readability Counts - A style guide is about consistency.
Consistency with this style guide is important. Consistency within a 
project is important, Consistency within one module or function is
the most important.

- Indentation
- Tabs or Spaces (Spaces)
- Maximum Line Length
- Blank Lines
- Imports """

""" pylint - A program which is an example of linter that is a program
that statically analyzes that is, read your code from top to bottom,
left to right anf tries to figure out if there are potentially
mistakes or inconsistencies with style guide. It is a bit noisy.

pip install pylint """

""" pycodestyle - A program that cannot only run on your computer but
will also take care of the reformatting if it's a bit messy. It is
less noisy."""

""" Black - 
pip install black
The name is actually an illusion to Henry Ford who invented cars way
back then and only sold quite a few black models for the same and indeed
is generally known with this quote ' Any customer can have a car painted
any color that he wants as long as it is black'. It is opinionated. It
is most popular these days."""

students = {
    "Hermoine": "Gryfiddor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Darco": "Slytherin",
    "Padma": "Ravenclaw",
}
for student in students:
    print(student)
