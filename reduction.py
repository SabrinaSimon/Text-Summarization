

def execute(your_input):
    x = None
    with open('sampleFile1.txt', 'r') as fp:
        x = fp.readlines()
    if x:
        return str(your_input) + ' ' + ''.join(x)