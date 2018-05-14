class Component:

    def __init__(self, fID, ftype, nextField):
        self.FieldID = fID
        self.FieldType = ftype
        self.NextField = nextField

    def getFieldID(self):
        return self.FieldID

    def getType(self):
        return self.FieldType

    def getNext(self):
        return self.NextField

    def setType(self, ftype):
        self.FieldType = ftype

    def setNext(self, nextField):
        self.NextField = nextField

    def detailedStr(self):
        return str(self)

    def __str__(self):
        component = '(' + self.FieldID + ':' + self.FieldType
        if self.NextField:
            nextID = self.NextField.FieldID
            component += ':' + nextID + ')'
        else:
            component += ':None)'
        return component

if __name__ == '__main__':
    pass