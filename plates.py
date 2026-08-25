# implement a program that prompts the user for a vanity plate and then output
# Valid if meets all of the requirements or Invalid if it does not. Assume that
# any letters in the user’s input will be uppercase.

#valid plates: start with 2 letters; max 6 chars and min 2 chars; nmbrs in the end;
# 1st nbr cant be zero; no " ", ".", or punctuation!

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
        # check if the lenght is valid
        if len(s)>6 or len(s)<2:
               return False
        # check is the characters are valid
        elif not s.isalnum():
              return False
        #check if first 2 characters are letters
        elif not (s[0].isalpha() and s[1].isalpha()):
               return False
        first_nbr = len(s)
        for char in s:
               if char.isnumeric():
                      # check if hte first number is zero (invalid)
                      if char=='0':
                             return False
                      first_nbr = s.index(char)
                      break
               # check if there are letters after the first number (invalid)
        for char in s[first_nbr:]:
                if char.isalpha():
                        return False
        return True

main()