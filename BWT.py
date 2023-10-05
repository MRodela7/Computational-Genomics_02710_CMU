def rle(s):
    """Run Length Encoder
    Args: s, string to be encoded
    Returns: RLE(s)
    """
    # Initialize variables
    encode = []
    currentChar = s[0]
    currentCount = 1

    # Loop through data
    for char in s[1:]:
        if char == currentChar:
            currentCount += 1
        else:
            encode.append((currentCount, currentChar))
            currentChar = char
            currentCount = 1
    # Add the final run
    encode.append((currentCount, currentChar))
    encodedString = ''
    for pair in encode:
      val = pair[0]
      if val >1:
        encodedString += pair[1]*2 + f'{val}'
      else:
        encodedString += pair[1]
    return encodedString


def bwt_encode(s):
    """Burrows-Wheeler Transform
    Args: s, string, which must not contain '{' or '}'
    Returns: BWT(s), which contains '{' and '}'
    """
    s = "{" + s + "}"
    rotatedStringList = sorted(s[i:] + s[:i] for i in range(len(s)))
    last_column = [row[-1:] for row in rotatedStringList]
    return "".join(last_column)

      
def bwt_decode(bwt):
    """Inverse Burrows-Wheeler Transform
    Args: bwt, BWT'ed string, which should contain '{' and '}'
    Returns: reconstructed original string s, must not contains '{' or '}'
    """
    table = [""] * len(bwt)  # Make empty table
    for i in range(len(bwt)):
        table = sorted(bwt[i] + table[i] for i in range(len(bwt)))  # Add a column of r
    s = [row for row in table if row.endswith("}")][0]  # Find the correct row (ending in ETX)
    return s.rstrip("}").strip("{")  # Get rid of start and end markers