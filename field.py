from component import Component

class Field(Component):

    NAME = ''
    ABBREV = ''
    DESCRIPTION = ''
    REFERENCELIST = ''
    DATATYPE = ''
    BASE = ''
    MASK = ''
    VALUECONSTR = ''
    REQUIRED = ''

    def __init__(self, ID, name, abbrev, descr, referencelist, datatype, base, mask, valueconstr, required):
        Component.__init__(self, ID, 'field', None)
        self.NAME = name
        self.ABBREV = abbrev
        self.DESCRIPTION = descr
        self.REFERENCELIST = referencelist
        self.DATATYPE = datatype
        self.BASE = base
        self.MASK = mask
        self.VALUECONSTR = valueconstr
        self.REQUIRED = required

    def getField(self):
        currField = '[' + self.FieldID + ':'+ self.FieldType + \
               ':' + self.NAME + ':' + self.ABBREV + \
               ':' + self.DESCRIPTION + ':' + self.REFERENCELIST + \
               ':' + self.DATATYPE + ':' + self.BASE + ', ' + self.MASK + \
               ':' + self.VALUECONSTR + ':' + self.REQUIRED

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + nextID + ')'
        else:
            currField += ':None]'
        return currField

    def detailedStr(self):
        currField = '(' + self.FieldID + ':'+ self.FieldType + \
               ':' + self.NAME + ':' + self.ABBREV + \
               ':"' + self.DESCRIPTION + '":' + self.REFERENCELIST + \
               ':' + self.DATATYPE + ':' + self.BASE + ':' + self.MASK + \
               ':' + self.VALUECONSTR + ':' + self.REQUIRED

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + nextID + ')'
        else:
            currField += ':None)'
        return currField

if __name__ == '__main__':
    #newField = Field('newField', 'nf', 'a new field', 'None', 'int', '8', 'None', 'None', '0')
    #print newField.getField()
    pass