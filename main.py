from time import perf_counter
# Class defining each node of the Huffmann Tree (minHeap Tree)
class Char:
    
    def __init__(self,character, value):
        
        self.character = character
        self.value = value
        self.child0 = None
        self.child1 = None
        self.code = str()

# Sort all the characters by their weight
def order(lst):
    
    lst.sort(key=lambda x: x.value)
    return lst

# (Recursive function) Run through the Tree and give each node a value
def deepen(obj):
    
    
    base = obj.code # Parent node's binary code the children will inherit
    
    if obj.child0 != None: # Check if the child is the last one
        obj.child0.code += base + '0'
        obj.child1.code += base + '1'
        
        deepen(obj.child0) # Repeat the process for each child of each child
        deepen(obj.child1)
        
    # Complete the node's binary code to display wanted bits number
    bits = 4 # Change this value to display more or less bits in the end
    while len(obj.code) < bits:
            obj.code = '0' + obj.code # Sexy concatenation tricks
    
    
# Convert the base sentence into a minHeap Tree stored as one object
def encode(sentence : str) -> list:
    
    # List each unique character in lists (object and string lists)
    chlst = list()
    items = list()
    
    # Check if the character was already taken into account
    for ch in sentence:
        if chlst.count(ch) == 0: # If not, make an object out of it
            chlst.append(ch) # Add the character to the string list
            items.append(Char(ch,sentence.count(ch))) # Add its weight, too
    
    # Make an arbitrary node by summing the two lightest characters
    iterr = 0 # We keep the iteration value to name the variables later
    while len(items) > 1: # We aim for a len:1 list in the end
        iterr += 1
        items = order(items)
        X = Char(f'X{iterr}',items[0].value + items[1].value) # Create node
        X.child0 = items[0] # Define its children
        X.child1 = items[1]
        if len(items) >= 1: # Remove the children from the objects list
            items.pop(0)
            items.pop(0)
        items.append(X) # Add the new node as a replacement for the children

    
    return items[0]


# Convert each node object to a dictionnary and regroup them in a list
def toDict(key, dad): # (Recursion)
    dad.append(key.__dict__)
    
    if key.child0 != None:
        toDict(key.child0, dad)
        toDict(key.child1, dad)
    
    return dad # He got the milk

# Use the dictionnaries to make a code out of the original sentence
def write(dictList, sentence):
    
    output = str()
    chList = list()
    for dct in dictList: # List of the characters to find the dicts idxs
        chList.append(dct['character'])
    
    for ch in sentence: # Compare the idx with each letter
        letteridx = chList.index(ch)
        output += dictList[letteridx]['code'] + ' '
    
    return output # Return the complete sentence
    
# Model (main) function to be called 
def encrypt(sentence):
    
    start_time = perf_counter()
    
    minHeap = encode(sentence)
    deepen(minHeap)
    codesList = toDict(minHeap, [])
    code = write(codesList, sentence)
    
    end_time = perf_counter()
    process_time = end_time - start_time
    
    print(code)
    print(f"Running time : {process_time*10**3} ms")
    return code # In case you want to use the string elsewhere




if __name__ == '__main__':
    # Encrypt the sentence
    encrypt('lexcellenceexcelleenexcel')