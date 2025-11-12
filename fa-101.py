def  FA(s):
    # If the length is less than 3, it can't be accepted
    if len(s) < 3:
        return "Rejected"
    # The first three characters must be '1', '0', '1'
    if s[0] == '1':
        if s[1] == '0':
            if s[2] == '1':
                # After index 2, only '1' can appear
                for i in range(3, len(s)):
                    if s[i] != '1':
                        return "Rejected"
                return "Accepted"
            return "Rejected"
        return "Rejected"
    return "Rejected"

# Test inputs
inputs = ['1','10101','101','10111','01010','100','','10111101','1011111']
for i in inputs:
    print(i,':',FA(i))