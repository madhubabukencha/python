"""
Name       : Madhu Babu Kencha
Created on : 27-02-2019

The copy() method returns a shallow copy dictionary.
This method does not take any value as argument
"""
synonyms = {'peace': 'silence', 'calm': 'silence', 'hush': 'silence'}
temp_var = synonyms.copy()
print("ID details:")
print("synonyms :{0}, temp_var : {1}".format(id(synonyms), id(temp_var)))
print("Using copy method : ", temp_var, "\n")


# We can also perform same thing using '=' operator
capitals = {'India': 'Delhi', 'Pakistan': 'Islamabad', 'China': 'Beijing'}
temp_var = capitals
print("ID details:")
print("capitals :{0}, temp_var : {1}".format(id(capitals), id(temp_var)))
print("Using '=' operator : ", temp_var, "\n")

print("The difference between 'copy()' and '=' operator: ")
chief_ministers = {'Andhra pradesh': 'Chandrababu Naidu', 'Telangana': 'Chandrashekar Rao'}
temp_var = chief_ministers.copy()
chief_ministers.clear()
print("Result if you use copy() method :", temp_var)

chief_ministers = {'Andhra pradesh': 'Chandrababu Naidu', 'Telangana': 'Chandrashekar Rao'}
temp_var = chief_ministers
chief_ministers.clear()
print("Result if you use '=' method\t:", temp_var)
