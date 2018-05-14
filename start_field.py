from component import Component

class StartField(Component):

    PROTOCOLNAME = ''
    PROTOCOLDESCR = ''
    DEPENDENTPROTONAME = ''
    DEPENDENCYPATTERN = ''

    def __init__(self, ID, protocolname, protocoldescr, dependentprotoname, dependencypattern):
        Component.__init__(self, ID, 'start_field', None)
        self.PROTOCOLNAME = protocolname
        self.PROTOCOLDESCR = protocoldescr
        self.DEPENDENTPROTONAME = dependentprotoname
        self.DEPENDENCYPATTERN = dependencypattern

    def detailedStr(self):
        currField = '(' + self.FieldID + ':' + self.FieldType + \
               ':' + self.PROTOCOLNAME + ':' + self.PROTOCOLDESCR + \
               ':' + self.DEPENDENTPROTONAME + ':' + self.DEPENDENCYPATTERN

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + nextID + ')'
        else:
            currField += ':None)'
        return currField

if __name__ == '__main__':
    pass