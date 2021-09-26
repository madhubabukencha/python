"""
1. An array is a collection of items stored at contiguous memory
   locations.The idea is to store multiple items of the same type
   together.
2. This makes it easier to calculate the position of each element
   by simply adding an offset to a base value.
3. A user can treat lists as arrays. However, user cannot constraint
   the type of elements stored in a list. If you create arrays using
   the array module, all elements of the array must be of the same type
4. Some of the data types are mentioned below which will help in creating
   an array of different data types.

'b' signed char        int 1
'B' unsigned char      int 1
'u' wchar_t Unicode    character 2 (1)
'h' signed short       int 2
'H' unsigned short     int 2
'i' signed int         int 2
'I' unsigned int       int 2
'l' signed long        int 4
'L' unsigned long      int 4
'q' signed long long   int 8
'Q' unsigned long long int 8
'f' float              float 4
'd' double             float 8
"""
import array


# Array with characters
array_num = array.array('b', [1, 2, 4])
print(array_num)
