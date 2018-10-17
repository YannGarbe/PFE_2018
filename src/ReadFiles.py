
class ReadFiles:

    def ReadAllFiles(self, filespath):
        """Read each files in given the file array and store it on a dictionnary

        Attributes:
            filespath : the file array containing the files' path
        """
        dictData = {}
        tmp_data = []
        filename = ""
        for filepath in filespath:
            filename = filepath.split("/")[-1]
            tmp_data = self.ReadAFile(filepath)

            dictData[filename] = tmp_data

        """Return the dictionnary containing the data of all the files"""
        return dictData

    def ReadAFile(self, filepath):
        """Read a 'hisea', 'paf' or 'mhap' file and store its data on a 2 dimensions array
        
        
        Attributes:
            filepath : the file's path
        """
        extension = filepath.split('.')[-1]
        data = []
        
        
        file = open (filepath, "r")
        for line in file:
            data_line = []
            on_word = False
            word = ""

            line = line.replace("\t", " ")

            for c in line:
                if c != ' ':
                    word = word + c
                    on_word = True
                elif c == ' ' and on_word:
                    data_line.append(word)
                    word = ""
                    on_word = False
            data_line.append(word[:-1])
            data.append(data_line)
        
        """Return the array containing the file's data"""
        return data