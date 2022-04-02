
#is a palindrome case 1 :

def is_palindrome(string):
    
    try:
        
        string = string.lower()
        
        if string==string[::-1]:
            
            is_palindrome = True
            
        else:
            
           is_palindrome = False
           
        return is_palindrome
    
    except:
        
        print("pls enter a vaild data")
        
is_palindrome('a')



#simple string matching  case 2 :

def solve(a,b):
    
    try:
        
        if a == b:
            
            return True
        
        elif '*' not in a:
            
            return False
        
        else:
            
            s = a.split('*')
            
            return a.replace('*', b[len(s[0]):len(b)-len(s[1])]) == b


    except NameError:

        print(" pls enter a right name")

    except:
        print ("pls enter a vaild data")



#find_nth_occurrence case 3 :


def find_nth_occurrence( substr , strr , occur=1 ):
    
    try :
        
        indx = -1
        
        l_indx = 0

        for s in range(occur):
            
            indx = strr.find(substr,l_indx)
            
            l_indx = indx+1
            
        return indx
    
    except:
        
        print("pls enter a valid data")








        
