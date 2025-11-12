# Accept the input string with Regular expression of FA: (a+b)*bba.
def FA(s):
    size = 0
    # Step 1: Scan the string and ensure it contains only 'a' and 'b'
    for i in s:
        if i == 'a' or i == 'b':
            size += 1
        else:
            return "Rejected"
    
    # Step 2: Check that the length is atleast 3 
    if size >= 3:
        # Step 3: Check the last 3 characters are 'b', 'b', 'a'
        if s[size - 3] == 'b':
            if s[size - 2] == 'b':
                if s[size - 1] == 'a':
                    return "Accepted"
                return "Rejected"
            return "Rejected"
        return "Rejected"
    return "Rejected"

inputs=['bba', 'ababbba', 'abba', 'baba','bbb','']
for i in inputs:
    print(i,':',FA(i))
