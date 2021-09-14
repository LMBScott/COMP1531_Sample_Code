def interleavings(a, b):
    if not len(a): # If a is empty
        if not len(b): # If b is empty
            return [''] # No interleavings to be made, return blank string
        return [b] # If b is the only non-blank string, b is the only interleaving
    elif not len(b):
        return [a] # If a is the only non-blank string, a is the only interleaving
    interleavings = []
    iSteps = step_interleavings('',a,b) # Get the set of first-step interleavings
    nextISteps = [] # Store the interleavings of the next step
    while len(iSteps): # While there are interleavings to be made
        for iStep in iSteps: # For each interleaving step, get the next interleaving step
            base, aChars, bChars = iStep
            nextISteps.extend(step_interleavings(base,aChars,bChars))
        if not len(nextISteps): # If all steps have been carried out, collect the interleaving strings
            interleavings = [step[0] for step in iSteps]
        iSteps = nextISteps # Set the current set of interleaving steps to that which was the next set
        nextISteps = [] # Clear the set of next-step interleavings
    return sorted(interleavings) # Return the interleavings, sorted lexographically

# For two strings a, b return a list of all combinations of the next letter from a or b with a given base string
# Each string combination is contained within a tuple along with the a and b strings, one of which is missing
# The letter used in the combination
def step_interleavings(base, a, b):
    interleavings = []
    if len(a): # If a is not blank
        if len(a) > 1: #
            interleavings.append((base+a[0], a[1:], b)) # If a had more than one character, it loses its first character
        else:
            interleavings.append((base+a[0], '', b)) # If a had only one character, it is now empty
    if len(b): # If b is not blank
        if len(b) > 1:
            interleavings.append((base+b[0], a, b[1:])) # If b had more than one character, it loses its first character
        else:
            interleavings.append((base+b[0], a, '')) # If b had only one character, it is now empty
    return interleavings