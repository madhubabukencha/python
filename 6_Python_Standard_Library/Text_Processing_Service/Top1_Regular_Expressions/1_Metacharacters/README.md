<b>Regular Expressions(re or regex):</b>
Regular Expressions are a set of sequence characters that defines a search pattern.

<b>Metacharacters</b>: To specify a regular expressions pattern  Metacharacters 
are used. Metacharacter are special character that are interpreted by Regex.<br>
<b>Eg</b> : [], {}, ^, +, (), \, |, *, $, .

<ol>
<li><b>Square Brackets []</b>:<br>Square brackets specifies a set of
        that you wish to match.<br>
        pattern --> [abc], input_text--> a, output --> match 1 <br>
        pattern --> [abc], input_text--> ac, output --> match 2<br>
        pattern --> [abc], input_text--> efsd, output --> no match <br>
        pattern --> [abc], input_text--> abc de abc, output -->match 6<br>
        <b>Usage</b>: <br>
        [a-e] is same as [abcde] <br>
        [1-4] is same as [1234] <br>
        [0-39] is same as [01239] <br>
        <b>complement(invert) the character set by using caret(^)</b>:<br>
        [^abc] means any character except a,b and c <br>
        [^0-9] means non-digit character
        
</li>
</ol>
