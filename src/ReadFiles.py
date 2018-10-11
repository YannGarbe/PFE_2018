
class ReadFiles:

    dictData = {}

    def ReadAllFiles(self, filespath):
        pass

    def ReadAFile(self, filepath):
        """Read a 'hisea', 'paf' or 'mhap' file and store its data on a map
        
        
        Attributes:
            filepath : the file's path
        """
        extension = filepath.split('.')[-1]
        data = []
        
        file = open (filepath, "r")
        for line in file:
            data_line = []
            on_word = False
            word = []
            for c in line:
                if c != ' ':
                    word.append(c)
                    on_word = True
                elif c == ' ' and on_word:
                    data_line.append(word)
                    word = []
                    on_word = False
            print(data_line)