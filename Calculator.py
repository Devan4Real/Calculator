def calc(operator, num1, num2=None):
    if not isinstance(num1, (int, float)):
        raise Exception(f"Invalid number \"{num1}\"")
    
    if num2 is not None and not isinstance(num2, (int, float)):
        raise Exception(f"Invalid number \"{num2}\"")
    
    if operator == '+' or operator == "add":
        if num2 is None:
            return num1
        return num1 + num2
    elif operator == '-' or operator == "sub":
        if num2 is None:
            return -num1
        return num1 - num2
    elif operator == '*' or operator == "mul":
        return num1 * num2
    elif operator == '/' or operator == "div":
        if num2 != 0:
            return num1 / num2
        else:
            raise Exception("Division by zero")
    elif operator == '%' or operator == "mod":
        if num2 != 0:
            return num1 % num2
        else:
            raise Exception("Division by zero")
    elif operator == '^' or operator == "pow":
        return num1 ** num2
    else:
        raise Exception(f"Invalid operator \"{operator}\"")



def eval(expression):
    if not isinstance(expression, list):
       raise Exception(f"Failed to evaluate \"{expression}\"")
   
    if len(expression) not in [2, 3]:
       raise Exception(f"Failed to evaluate \"{expression}\"")
    
    if len(expression) == 2:
        operator = expression[0]
        num1 = expression[1]
        
        if isinstance(num1, list):
            num1 = eval(num1)
            
        return calc(operator, num1)  
    elif len(expression) == 3:    
        operator = expression[0]
        num1 = expression[1]
        num2 = expression[2]
    
        if isinstance(num1, list):
            num1 = eval(num1)
        if isinstance(num2, list):
            num2 = eval(num2)
            
        return calc(operator, num1, num2)



def struct(lst):
    try:   
        nlst = lst
        if len(nlst) == 2:
            return nlst
        elif len(nlst) < 2:
            raise Exception
        else:
            i = 1
            while i < (len(nlst)-1):
                if nlst[i] == '^' or nlst[i] == 'pow':
                    new_list = [nlst[i], nlst[i-1], nlst[i+1]]
                    nlst = nlst[:i-1] + [new_list] + nlst[i+2:]
                else:
                    i += 1
            
            i = 1
            while i < (len(nlst)-1):
                if nlst[i] == '*' or nlst[i] == '/' or nlst[i] == '%' or nlst[i] == 'mul' or nlst[i] == 'mod' or nlst[i] == 'div':
                    new_list = [nlst[i], nlst[i-1], nlst[i+1]]
                    nlst = nlst[:i-1] + [new_list] + nlst[i+2:]
                else:
                    i += 1
                    
        
            i = 1
            while i < len(nlst) - 1:
                if nlst[i] == '+' or nlst[i] == '-' or nlst[i] == 'add' or nlst[i] == 'sub':
                    new_list = [nlst[i], nlst[i-1], nlst[i+1]]
                    nlst = nlst[:i-1] + [new_list] + nlst[i+2:]
                else:
                    i += 1
             
     
            i = 1
            while i < len(nlst) - 1:
                if not(isinstance(nlst[i], int) or isinstance(nlst[i], float) or isinstance(nlst[i], list)):
                    new_list = [nlst[i], nlst[i-1], nlst[i+1]]
                    nlst = nlst[:i-1] + [new_list] + nlst[i+2:]
                else:
                    i +=2

            
                
            if nlst[-1] in ['+', 'add', '-', 'sub', '*', 'mul', '/', 'div', '%', 'mod', '^', 'pow']:
                raise Exception
            
            return nlst[0]
    except:
        return (f"Failed to structure \"{lst}\"")



def get_next(s, index):
    try:
        if s == '':
            raise Exception
        num = ''
        op = ''
        # Find the start of the number
        inum = index
        while inum < len(s):
            if (s[inum].isdigit() or s[inum] == '.'):
                num += s[inum]
                inum += 1
            else:
                break
          
        if not (num == ''):
            if '.' in num:
                num = float(num)
            else:
                num = int(num)
        
        iop = index
        while iop < len(s):
            if not (s[iop].isdigit() or s[iop] == '.' or s[iop] == '(' or s[iop] == ')'):
                op += s[iop]
                iop += 1
            else:
                break
        
        if s[index].isdigit() or s[index] == '.':
            return num,inum
        else:
            return op,iop
    except:
       return "End of string"
    
    

def parse(s):
    s = s.replace(' ', '')
    results = []
    index = 0
    while index < len(s):
        if s[index] == '(':
            open_para = 1
            close_para = index + 1
            while close_para < len(s):
                if s[close_para] == '(':
                    open_para += 1
                elif s[close_para] == ')':
                    open_para -= 1
                    if open_para == 0:
                        break
                close_para += 1
        
            nested_result = parse(s[index + 1:close_para])
            results.append(nested_result)
            index = close_para + 1 
        else:
            a = get_next(s, index)
            if a == "End of string":
                break
            results.append(a[0])
            index = a[1]
    
    return struct(results)


def pre_parse(s):
    index = 0
    open_para = 0
    close_para = 0
    while index < len(s):
        if s[index] == '(':
            open_para += 1
        elif s[index] == ')':
            close_para += 1
        index += 1  
                
    if (open_para != close_para):
        raise Exception("Not matching parenthesis")



def coordinate(s):
    try:
        pre_parse(s)
        s = parse(s)
        return eval(s)
    except Exception as e:
        return (f'Error: {e}')


if __name__ == '__main__':
    while True:
        inp = input()
        if inp == 'q' or inp == 'quit':
            break
        else:
            out = coordinate(inp)
            print(out)











