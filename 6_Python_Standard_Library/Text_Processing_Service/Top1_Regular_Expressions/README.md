Regular Expressions
-------------------
Regular Expressions are a set of sequence characters that defines a search pattern.
 
####Sequence Characters
<hr>

All sequence characters are starts with backward slash(\\)
<table>
  <tr>
    <th> Sequence Characters </th>
    <th> Description</th>
  </tr>
  <tr>
    <td> \d </td>
    <td> It match's any digit from <strong>0 to 9</strong> in a given string <b>([0-9])</b></td>
  </tr>
  <tr>
    <td> \D </td>
    <td> It match's all <strong>non-digits</strong> in the given string <b>([^0-9])</b></td>
  </tr>
  <tr>
    <td> \s </td>
    <td> It match's <strong>whitespaces</strong> in the given string  <b>([\t\n\r\f\v])</b> </td>
  </tr>
  <tr>
    <td> \S </td>
    <td> It match's <strong>non-whitespaces</strong> in the given string <b>([^ \t\n\r\f\v])</b></td>
  </tr>
  <tr>
    <td> \w </td>
    <td> It match's any <strong>alpha numeric (a-z, A-Z, 0-9, _) </strong>value in the given string </td>
  </tr>
  <tr>
    <td> \W </td>
    <td> It match's any <strong>non-alpha numeric</strong> value in the given string </td>
  </tr>
  <tr>
    <td> \b </td>
    <td> Word Boundary </td>
  </tr>
  <tr>
    <td> \B </td>
    <td> Not a Word Boundary </td>
  </tr>
  <tr>
    <td> \A </td>
    <td> Matches only at <strong>start of the string</strong></td>
  </tr>
  <tr>
    <td> \Z </td>
    <td> Matches only at <strong>end of the string</strong></td>
  </tr>
</table>


#### Meta Character
<hr>
<table>
  <tr>
    <th> Character </th>
    <th> Description </th>
  </tr>
  <tr>
    <td>[ ]</td>
    <td> Matches characters in brackets </td>
  </tr>
  <tr>
    <td>[^ ]</td>
    <td> Matches characters NOT in brackets </td>
  </tr>
  <tr>
    <td><strong> . </strong></td>
    <td> Any character (except newline character) </td>
  </tr>
  
</table>

.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+