from component import Component

class EndField(Component):

    def __init__(self, ID):
        Component.__init__(self, ID, 'end_field', None)

    def detailedStr(self):
        currField = '(' + self.FieldID + ':' + self.FieldType

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + nextID + ')'
        else:
            currField += ':None)'
        return currField

if __name__ == '__main__':
    pass