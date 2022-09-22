# Calcium v1.4
Calcium is a Mathematical equation parser and solver. It gets a string of a mathematical equation **e.g 2 + 8** and it solves it.

PLY is used for the parser and lexer. It is the CPython implementation of Lex and YACC. It is available on PIP.

Calcium consits of a Python library and a Shell. Everything is done in the Calcium Library as it manages the parser and lexer. It will be available on PIP for everyone.

The change log can be found in this folder (File called **'changelog'**).

### Calcium Shell

The shell exists as a program to test and use Calcium. If you run the shell without any parameters, it will launch the shell and you can type mathematical equations and Calcium shell will solve it for you. In addition, the Calcium shell supports input from parameters. **e.g calciumshell 2 + 7** and it will output to the screen. This is very useful for shell scripts which can use pipes to take advantage of the output.

Overall currently, Calcium is really simple. In future updates, Calcium is going to get more features and bug fixes.