from component import Component

class StartField(Component):

    def __init__(self, ID, protocolname, protocoldescr, dependentprotoname, dependencypattern):
        Component.__init__(self, ID, 'start_field', None)
        self.PROTOCOLNAME = protocolname
        self.PROTOCOLDESCR = protocoldescr
        self.DEPENDENTPROTONAME = dependentprotoname
        self.DEPENDENCYPATTERN = dependencypattern

    def setROTOCOLNAME(self, protocolname):
        self.PROTOCOLNAME = protocolname

    def getROTOCOLNAME(self):
        return self.PROTOCOLNAME

    def setROTOCOLDESCR(self, protocoldescr):
        self.PROTOCOLDESCR = protocoldescr

    def setROTOCOLDESCR(self, protocoldescr):
        return self.PROTOCOLDESCR

    def setDEPENDENTPROTONAME(self, dependentprotoname):
        self.DEPENDENTPROTONAME = dependentprotoname

    def setDEPENDENTPROTONAME(self, dependentprotoname):
        return self.DEPENDENTPROTONAME

    def setDEPENDENCYPATTERN(self, dependencypattern):
        self.DEPENDENCYPATTERN = dependencypattern

    def setDEPENDENCYPATTERN(self, dependencypattern):
        return self.DEPENDENCYPATTERN

    def detailedStr(self):
        currField = '(' + str(self.FieldID) + ':' + str(self.FieldType) + \
                    ':' + str(self.PROTOCOLNAME) + ':' + str(self.PROTOCOLDESCR) + \
                    ':' + str(self.DEPENDENTPROTONAME) + ':' + str(self.DEPENDENCYPATTERN)

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + str(nextID) + ')'
        else:
            currField += ':None)'
        return currField

if __name__ == '__main__':
    pass