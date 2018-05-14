from protocol_decision_tree import ProtocolDecisionTree

class protocol_manager:

    def __init__(self):
        self.PDT = ProtocolDecisionTree()

    def getPDT(self):
        return self.PDT

    def setPDTDescription(self, description):
        self.PDT.enterDescription('' + description)

    def getPDTDescription(self):
        return self.PDT.getDescription()

    def deleteComponent(self, component):
        currentParent = self.PDT
        current = currentParent.getNext()
        while current:
            if str(current.FieldID) == str(component):
                currentParent.setNext(current.getNext())
                return
            else:
                currentParent = current
                current = current.getNext()
        print "Error: Component does not exist in PDT"
        return

    def addField(self, name = 'DEFAULT', abbrev = 'DFLT', descr = '', referencelist = None,
                 datatype = 'None', base = 'base.NONE', mask = 'None', valueconstr = 'None', required = False):
        self.PDT.addField(name, abbrev, descr, referencelist, datatype, base, mask, valueconstr, required)

    def addStartField(self, protocolname = 'DEFAULT', protocoldescr = '',
                      dependentprotoname = '', dependencypattern = ''):
        self.PDT.addStartField(protocolname, protocoldescr, dependentprotoname, dependencypattern)

    def addEndField(self):
        self.PDT.addEndField()

    def addReferenceList(self, reflistname = 'DEFAULT'):
        self.PDT.addReferenceList(reflistname)

    def addPacketInfoList(self):
        self.PDT.addPacketInfoList()

    def findComponent(self, component):
        return self.PDT.findComponent(component)

    def generateIntermediateScript(self):
        pass

if __name__ == '__main__':
    test = protocol_manager()
    print str(test.PDT)
    test.setPDTDescription("test pdt")
    print test.getPDTDescription()
    test.addStartField()
    print str(test.PDT)
    test.addField()
    print str(test.PDT)
    test.addPacketInfoList()
    print str(test.PDT)
    test.addReferenceList()
    print str(test.PDT)
    test.addEndField()
    print str(test.PDT)
    print str(test.PDT.detailedPDT())
