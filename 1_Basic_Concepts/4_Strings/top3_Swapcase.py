def swap_case(s):
  Length = len(s)
  p=""
  if (Length<=10 and Length>=0):
      for i in s:
          if (i.isupper()):
              k = i.lower()   
          else:
              k = i.upper()
          p+=k 
      return p 
  
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)