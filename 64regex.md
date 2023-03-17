Regex Quick Reference
=====================

Make your own regex cheat sheet
Format it in Markdown

## Basic Characters:
| Expression | Explanations|
| :-: | :-: |
| ^ | Matches the expression to its right, at the start of a string before it experiences a line break. |
| $	| Matches the expression to its left, at the end of a string before it experiences a line break. |
| . | Matches any character except newline. |
| a	| Matches exactly one character a. |
| xy | Matches the string xy. |
| a\|b | Matches expression a or b. If a is matched first, b is left untried. |

## Quantifiers:
| Expressions | Explanations|
| :-: | :-: |
| +	| Matches the expression to its left 1 or more times. |
| \* | Matches the expression to its left 0 or more times. |
| ?	| Matches the expression to its left 0 or 1 times. |	
| {p} |Matches the expression to its left p times, and not less. |
| {p, q} |Matches the expression to its left p to q times, and not less. |
| {p, }	| Matches the expression to its left p or more times. |

## Character Classes:	
| Expressions | Explanations|
| :-: | :-: |
| \w | Matches alphanumeric characters, that is a-z, A-Z, 0-9, and underscore(_) |
| \W | Matches non-alphanumeric characters, that is except a-z, A-Z, 0-9 and_ |
| \\d | Matches digits, from 0-9 |
| \D | Matches any non-digits. |
| \s | Matches whitespace characters, which also include the \t, \n, \r, and space characters. |
| \S |Matches non-whitespace characters. |
| \A | Matches the expression to its right at the absolute start of a string whether in single or multi-line mode.|
| \Z | Matches the expression to its left at the absolute end of a string whether in single or multi-line mode. |
| \n | Matches a newline character. |
| \\t | Matches tab character. |
| \\b | Matches the word boundary (or empty string) at the start and end of a word. |
| \B | Matches where \b does not, that is, non-word boundary. |

## Sets:
| Expressions | Explanations|
| :-: | :-: |
| [abc] | Matches either a, b, or c. It does not match abc. |
| [a-z] | Matches any alphabet from a to z. |
| [A-Z] | Matches any alphabets in capital from A to Z | 
|[a\\-p] | Matches a, -, or p. It matches – because \ escapes it. |
| [-z] | Matches – or z |
| [a-z0-9] | Matches characters from a to z or from 0 to 9 |
| [a-z0-9] | Matches characters from a to z or from 0 to 9. |
| [(+*)]  |Special characters become literal inside a set, so this matches (, +, *, or ) |
| [^ab5] |Adding ^ excludes any character in the set. Here, it matches characters that are not a, b, or 5. |
| \\[a\\] | Matches [a] because both parentheses [ ] are escaped |

## Groups:
| Expressions | Explanations|
| :-: | :-: |
| ( ) | Matches the expression inside the parentheses and groups it which we can capture as required |
|(?#…) | Read a comment |
| (?PAB) | Matches the expression AB, which can be retrieved with the group name. |
| (?:A) | Matches the expression as represented by A, but cannot be retrieved afterwards. |
| (?P=group) | Matches the expression matched by an earlier group named “group” |
## Assertions:
| Expressions | Explanations|
| :-: | :-: |
| A(?=B) | This matches the expression A only if it is followed by B. (Positive look ahead assertion) |
| A(?!B) |This matches the expression A only if it is not followed by B. (Negative look ahead assertion) |
| (?<=B)A | This matches the expression A only if B is immediate to its left.  (Positive look behind assertion) |
| (?<!B)A | This matches the expression A only if B is not immediately to its left. (Negative look behind assertion) |
| (?()\|) | If else conditional |
## Flags
| Expressions | Explanations|
| :-: | :-: |
| a | Matches ASCII only |
| i | Ignore case |
| L | Locale character classes |
| m | ^ and $ match start and end of the line (Multi-line) |
| s | Matches everything including newline as well |
| u | Matches Unicode character classes |
| x | Allow spaces and comments (Verbose) |
