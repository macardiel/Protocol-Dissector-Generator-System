from component import Component

class ReferenceList(Component):

    REFERENCELISTNAME = ''
    REFERENCELIST = {}

    def __init__(self, ID, reflistname):
        Component.__init__(self, ID, 'reference_list', None)
        self.REFERENCELISTNAME = reflistname

    def addElement(self, key, value):
        if key in self.REFERENCELIST:
            pass
        else:
            self.REFERENCELIST[key] = value

    def delElement(self, key):
        del(self.REFERENCELIST[key])

    def detailedStr(self):
        currField = '(' + self.FieldID + ':' + self.FieldType + ':' + \
                    self.REFERENCELIST + ':' + str(self.REFERENCELIST)

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + nextID + ')'
        else:
            currField += ':None]'
        return currField

if __name__ == '__main__':
    pass