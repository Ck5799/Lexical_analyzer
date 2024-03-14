token = {
    'keyword': ['while', 'int', 'cout', 'for', 'return'], 
    'separator': ['(', ')', '{', '}'],
    'operator': ['>', '<', '=', '==', '>=', '<=', '+', '-', '*', '/', '<<', '+=', '-=', '*=', '/='],
    'punctuation': [';'],
    'comment': ['//'],
    'string': ['"', "'"]
}   #Dictionary of elements

found = {
    'keyword': [], 
    'separator': [],
    'operator': [],
    'punctuation': [],
    'integer': [],
    'float': [],
    'identifier': [],
    'comment': [],
    'string': []
}   #Dictionary to store found elements

def add_spaces(string): #Function to go through input code and add spaces
    spaces = token['separator'] + token['operator'] + token['punctuation'] + token['comment'] + token['string'] #Things I want to add spaces around
    for stuff in spaces:
        if stuff in string and len(stuff) == 1:
            string = string.replace(stuff, " " + stuff + " ")
    
    for long_stuff in spaces:
        if len(long_stuff) > 1:
            to_find = long_stuff[0] + "  " + long_stuff[1]
            string = string.replace(to_find, long_stuff)
            
    return string

def identifier(unknown):    #Function to identify what is unknown
    integer = False
    float = False
    
    if unknown[0].isdigit():                        
    #if unknown[0].isdigit() or unknown[0] == '-':
        integer = True
    for j in range(len(unknown)):
        if unknown[j] == '.':
            float = True
                            #Can be either float, integer, or identifier
    if float:
        return 'float'
    if integer:
        return 'integer'
    return 'identifier'
    
with open("C:\\Users\\sidsc\\Downloads\\input_sourcecode.txt") as f:    #Opens sourcecode
    lines = f.readlines()
    #print(lines)

out_file = open('out_file.txt', 'w+')   #creates out_file

unknown = []

for i in range(len(lines)): #Goes through code in file line by line
    temp = ''
    comment = False
    string = False
    
    new = add_spaces(lines[i]) #Adds spaces to line of code its currently on
    #int main(){
    # int main ( ) {
    
    for code in new.split():    #Goes through elements in the line split by white space
        
        if string:  #If string was found go in here
            temp += ' ' + code  #Adds current element to string 
            if code in token['string']: #Keeps adding if another quotation was found.
                
                temp = temp.replace('" ', '"')  #Formatting
                temp = temp.replace(' "', '"')
                
                found['string'].append(temp)
                print('string:' + " "*(20 - len('string')) + temp + "\t")
                out_file.write('string:' + " "*(20 - len('string')) + temp + "\t\n") #Adds string to found dictionary, adds to out_file
                
                temp = ''       
                string = False  #Resets temp and string variables
        
        elif comment:   #If comment was found
            temp += ' ' + code  #Adds current element to temp
        
        else:
            if code in token['keyword']: # Found keyword
                found['keyword'].append(code)
                print('keyword:' + " "*(20 - len('keyword')) + code + "\t") 
                out_file.write('keyword:' + " "*(20 - len('keyword')) + code + "\t\n")  #Writes to out_file
                
            elif code in token['separator']: # Found separator
                found['separator'].append(code)
                print('separator:' + " "*(20 - len('separator')) + code + "\t")
                out_file.write('separator:' + " "*(20 - len('separator')) + code + "\t\n")  #Writes to out_file
                
            elif code in token['operator']: # Found operator
                found['operator'].append(code)
                print('operator:' + " "*(20 - len('operator')) + code + "\t")
                out_file.write('operator:' + " "*(20 - len('operator')) + code + "\t\n")    #Writes to out_file
                
            elif code in token['punctuation']:  # Found punctuation
                found['punctuation'].append(code)
                print('punctuation:' + " "*(20 - len('punctuation')) + code + "\t")
                out_file.write('punctuation:' + " "*(20 - len('punctuation')) + code + "\t\n")  #Writes to out_file
                
            elif code in token['comment']:  # Found comment and switches to comment mode
                temp = code
                comment = True
            elif code in token['string']:   # Found string and switches to string mode
                temp = code
                string = True
            else:
                type = identifier(code) # Unknown element, uses identifier function to determine what it is
                found[type].append(code)
                print(type + ":"+ " "*(20 - len(type)) + code + "\t")
                out_file.write(type + ":"+ " "*(20 - len(type)) + code + "\t\n")    #Writes to out_file
    
    if comment:
        found['comment'].append(temp)
        print('comment:' + " "*(20 - len('comment')) + temp + "\t")
        out_file.write('comment:' + " "*(20 - len('comment')) + temp + "\t\n")  #Writes to out_file
        
        temp = ''
        comment = False     #Resets temp and comment variables

out_file.close()    #Closes out_file

found['identifier'] = list(set(found['identifier'])) #Makes it so that if there are multiple same identifiers, the occurence is only once

for key in found:   #Prints out found dictionary
    pass
    #print(key, ':\t', found[key])

'''
SPACES_SPACES_SPACES_SPACES_SPACES_SPACES_SPACES_SPACES_SPACES_SPACES_SPACES_SPACES_SPACES_SPACES
int main (  )  { 
    for ( int i = 22 ; i <= 100 ; i = i + 1 )  { 
        while ( i == 100 )  {  
          cout << "Hello World!" ; //print out
         } 
     }  
    return 0 ; 
 } 
 
NO_SPACES_NO_SPACES_NO_SPACES_NO_SPACES_NO_SPACES_NO_SPACES_NO_SPACES_NO_SPACES_NO_SPACES_NO_SPACES

int main(){
    for(int i=22;i<=100;i=i+1){
        while(i==100){
          cout<<"Hello World!";//print out
        }
    }
    return 0; 
}
'''

"asdfadsfintasdfsdf"