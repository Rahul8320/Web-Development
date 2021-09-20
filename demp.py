
class Chapter:
    number = ""
    page = 0
    marks = 0
    name = ""
    def __init__(self,number,page,marks,name) -> None:
        self.number = number
        self.page = page
        self.marks = marks
        self.name = name

class Exam(Chapter):
    examName = ""
    chapterList = []
    def __init__(self,examName,chapterList) -> None:
        self.examName=examName
        for e in chapterList:
            self.chapterList.append(e)

    def findMinimumChapterByMarks(self):
        minMarks = 999999
        chapter = None
        for e in self.chapterList:
            if e.marks < minMarks:
                minMarks = e.marks
                chapter = e
        return chapter 
    
    def sortChapterByPage(self):
        dict = {}
        for e in self.chapterList:
            dict[e.page] = e
        chapterlist = []
        for e in sorted(dict.keys()):
            chapterlist.append(e)
        if len(chapterlist) == 0:
            return None
        else:
            return chapterlist

    
def main():
    try:
        n = int(input())
        templist = []
        for i in range(n):
            number = input()
            page = int(input())
            marks = int(input())
            name = input()
            temp = Chapter(number, page, marks, name)
            templist.append(temp)

        examName = input()
        obj = Exam(examName,templist) 
        tempobj = obj.findMinimumChapterByMarks()
        if tempobj is not None:
            print(tempobj.number)
            print(tempobj.page)
            print(tempobj.marks)
            print(tempobj.name)
        else:
            print("No Data Found")

        lst = obj.sortChapterByPage()
        if lst is not None:
            for e in lst:
                print(e)
        else:
            print("No Data Found")
            
    except:
        pass

if __name__ == "__main__":
    main()