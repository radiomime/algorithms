#LastName: Wright
#FirstName: Matthew
#Email: matthew.wright@colorado.edu
#Comments:
#
#

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields
    def __init__(self, isRootNode):
        
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        
        self.isRoot = isRootNode # Only true for root node on initialization.
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mapping each character from a-z to the child node
    
    
    def addWord(self,word):
        assert(len(word) > 0) # return error if word is empty
        
        currentNode = self
        for letter in word:
            nextNode = MyTrieNode(False)   # Memory leaks out the ass?
            
            if letter in currentNode.next:
                currentNode = currentNode.next[letter]


            
            
            else:
                currentNode.next[letter] = nextNode
                currentNode = nextNode

        currentNode.count += 1
        currentNode.isWordEnd = True
        return

    def lookupWord(self,word):
        #return 0 if no length?
        
        crawlerNode = self
        
        for letter in word:
            if letter in crawlerNode.next:
                crawlerNode = crawlerNode.next[letter]
            else:
                return 0
                
        if (crawlerNode.isWordEnd):
            return crawlerNode.count
        
        return 0
        
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
        
        return 0 # TODO: change this line, please
    
    
    
    
    
    def autoCompleteHelper(self, prefix):
        # print("Prefix", prefix)
        lst = []
        # lst = [("yes",3),("no",4)]
        for letter in self.next:
            newPrefix = prefix+letter
            newNode = self.next[letter]
            lst.extend(newNode.autoCompleteHelper(newPrefix))
        
        
        if self.isWordEnd:
            lst.append((prefix,self.count))
        
        return lst
    
    
    def autoComplete(self,word):
        wordList = []
        crawlerNode = self
        
        # Iterate to the end of the prefix (beginning of where autocomplete will act)
        for letter in word:
            if letter in crawlerNode.next:
                crawlerNode = crawlerNode.next[letter]
            else:
                return wordList

        # Build Word List
#        if (crawlerNode.isWordEnd):
#            wordList.append((word, crawlerNode.count))

        # lst = [("yes",3),("no",4)]
        # Get the autocomplete helper going, some recurssion will happen in it.
        wordList.extend( crawlerNode.autoCompleteHelper(word) )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j
        # Of the form, [('Walter',1),('Mitty',2),('Went',3),('To',4),('Greenland',2)]
        
        
        
        
        
        
        return wordList #TODO: change this line, please
    
    
            

if (__name__ == '__main__'):
    t = MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)
    
    
    j = t.lookupWord('testy') # should return 0
#    print( "j, should be 0, ", j)
    j2 = t.lookupWord('telltale') # should return 0
#    print( "j2, should be 0, ", j2)
    j3 = t.lookupWord ('testing') # should return 2
#    print( "j3, should be 2, ", j3)
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
 
    
    
     
