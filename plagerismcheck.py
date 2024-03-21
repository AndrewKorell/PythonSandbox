from pprint import pprint
import re 
'''
This is a challenge test I viewed online 

search a library of books for the two books
that most closely match



"I have this I like to read."

"She has this book I like to watch."

My plan is very primitive. 

Take a substring from book1. Try to match it in book2 

If it matchest in book2 expand the the size of the substring until it doesn't 

If no match adance the start by 1.

If there is a match we found the max size then advance to the end of the matching substring 

for two large strings of test we should get an array of matching substrings and their locations 


What we miss:
minor differences in capitalization, localized spelling, and punctuation. 

Some of thise could be accomplished with Regex, paricularly ignore case 


'''


book1 = "I have this book I like to read. The fox is grey. The fox is black."
book2 = "She has this book I like to watch. The fox is black. The fox is grey!"

longest = 0
min_length = 5
start = 0
end = min_length
matches = []
substring = ""

while True :
    
    if end > len(book1) :
        print("end of book")
        break

    r = re.search((searched := book1[start:end]), book2, re.IGNORECASE)
    print(searched)
    print(r)
    if r != None :
        substring = r.group(0)
        cross_index = book2.index(substring)
        end += 1
        if end > len(book1) :
            matches.append({'start1': start, 'start2': cross_index, 'length': len(substring), 'substring': substring})
    else :
        if len(substring) > 0 :
            matches.append({'start1': start, 'start2': cross_index, 'length': len(substring), 'substring': substring})
            start = end
        else :
            start += 1 
        
        end = start + min_length 
        substring = ""


pprint(matches)


