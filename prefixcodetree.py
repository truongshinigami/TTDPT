class PrefixCodeTree:
  def __init__(self):
    #generate new tree
    self.tree = [0]*2000

  def insert(self,codeword,symbol):
    
    #codeword index 
    i=0
    for value in codeword:
      if value == 1: 
        i = i * 2 + 2
      elif value == 0:
        i = i * 2 + 1

    self.tree[i]=symbol

  def decode(self,encodedData, datalen):

    #final message
    message=""
    i=0
    #decode encode data
    decode=""
    for byte in encodedData:
      decode += f'{byte:0>8b}'
    #start decode
    for j in range(datalen):
        char = decode[j]
        if char == '1': 
            i = i * 2 + 2
        elif char == '0':
            i = i * 2 + 1
         #if found a symbol, add to result, go back to root
        if self.tree[i] != 0:
            message += " " + self.tree[i]
            i=0 
    return message