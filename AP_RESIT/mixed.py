# Flyweight + Factory Practice

class InvalidTokenError(Exception):
    def __init__(self):
        super().__init__("Some exception due to invalid tokens")
   


class TokenType:
    def __init__(self, text, token_id, length, is_stopword):
        # TODO1:
        # store shared/intrinsic state
        self.text = text
        self.token_id = token_id
        self.length = length
        self.is_stopword = is_stopword
    


class TokenOccurrence:
    def __init__(self, token_type, position, sentence_id):
        # TODO2:
        # store unique/extrinsic state
        self.token_type= token_type
        self.position = position
        self.sentence_id = sentence_id
        

    def describe(self):
        # TODO3:
        # return:
        # "word='code', id=1, pos=0, sentence=0, stopword=False"
        
        pass


class TokenFactory:
    def __init__(self):
        # TODO4:
        # create cache dictionary
        # create next_id starting at 1
        # create stopwords set
        pass

    def get_token_type(self, text):
        # TODO5:
        # validate that text is a non-empty string
        # lowercase the text
        # if token already exists, return it
        # otherwise create TokenType with:
        #   text
        #   token_id
        #   length
        #   is_stopword
        # store and return it
        pass


def tokenize(sentences):
    # TODO6:
    # sentences is a list of strings
    # create a TokenFactory
    # create an empty occurrences list
    # for each sentence, split into words
    # create TokenOccurrence objects
    # return occurrences and factory
    pass


sentences = [
    "Code in Python and code in Java",
    "The code of Python is clean",
    "Java and Python are languages"
]

occurrences, factory = tokenize(sentences)

for occurrence in occurrences:
    print(occurrence.describe())

# Tests:
python1 = factory.get_token_type("Python")
python2 = factory.get_token_type("python")
code1 = factory.get_token_type("code")
code2 = factory.get_token_type("Code")

print(python1 is python2)  # True
print(code1 is code2)      # True

# Uncomment to test validation:
# factory.get_token_type("")
# factory.get_token_type(123)