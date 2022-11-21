def Brackets_Balanced(Brackets):
    stack = []
 
    # Traversing the Expression
    for char in Brackets:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            #Checking is the 1st element is not a closing bracket
            if not stack:
                return False
            character_popped = stack.pop()
            if character_popped == '(':
                if char != ")":
                    return False
            if character_popped == '{':
                if char != "}":
                    return False
            if character_popped == '[':
                if char != "]":
                    return False
 
    #Check if stack is empty as all brackets needs to be balanced so they can be popped
    if stack:
        return False
    return True
 
 
if __name__ == "__main__":
    Brackets = "[()]{[]}{[()()]()}"

    if Brackets_Balanced(Brackets):
        print("Brackets are Balanced")
    else:
        print("Brackets are Not Balanced")