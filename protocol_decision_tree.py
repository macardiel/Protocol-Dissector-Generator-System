from component import Component
from field import Field
from start_field import StartField
from end_field import EndField
from reference_list import ReferenceList
from packet_information import PacketInformation

class ProtocolDecisionTree:

    def __init__(self):
        self.componentCount = 0
        root_ID = 'comp' + str(self.componentCount)
        self.PDT = Component(root_ID, 'root', None)
        self.PDT_end = self.PDT
        self.PDT_Description = ""

        self.componentCount += 1

    def updatePDTEnd(self, object):
        self.PDT_end.NextField = object
        self.PDT_end = self.PDT_end.NextField
        self.componentCount += 1

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

    def enterDescription(self, description):
        self.PDT_Description = '' + description

    def addField(self, name = 'DEFAULT', abbrev = 'DEFAULT', descr = 'DEFAULT', referencelist = None,
                 datatype = 'DEFAULT', base = 'DEFAULT', mask = 'DEFAULT', valueconstr = 'DEFAULT', required = False):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(Field(ID, name, abbrev, descr, referencelist, datatype, base, mask, valueconstr, required))

    def addStartField(self, protocolname = 'DEFAULT', protocoldescr = 'DEFAULT',
                      dependentprotoname = 'DEFAULT', dependencypattern = 'DEFAULT'):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(StartField(ID, protocolname, protocoldescr, dependentprotoname, dependencypattern))

    def addEndField(self):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(EndField(ID))

    def addReferenceList(self, reflistname = 'DEFAULT'):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(ReferenceList(ID, reflistname))

    def addPacketInfoList(self):
        ID = 'comp' + str(self.componentCount)
        self.updatePDTEnd(PacketInformation(ID))

    def findComponent(self, component):
        current = self.PDT
        while current:
            if current.FieldID == component:
                return current
            current = current.NextField
        print "Error: component not in list"
        return None

    def detailedPDT(self):
        current = self.PDT
        PDT_str = '[ ' + current.detailedStr() + ' '
        current = current.NextField
        while current:
            PDT_str += current.detailedStr() + ' '
            current = current.NextField
        PDT_str += ']'
        return PDT_str

    def __str__(self):
        current = self.PDT
        PDT_str = '[ ' + str(current) + ' '
        current = current.NextField
        while current:
            PDT_str += str(current) + ' '
            current = current.NextField
        PDT_str += ']'
        return PDT_str

if __name__ == '__main__':
    # root = ProtocolDecisionTree()
    # #root.printPDT()
    # print str(root)
    # root.addField('newField', 'nf', 'a new field', 'None', 'int', '8', 'None', 'None', '0')
    # root.addStartField('startfield', 'n/a', 'n/a', 'n/a')
    # #root.printPDT()
    # print str(root)
    # print str(root.findComponent('comp1'))
    # print str(root.findComponent('comp3'))
    # print str(root)
    # print root.detailedPDT()
    # temp = root.findComponent('comp1')
    # print temp.detailedStr()
    # print str(root)
    # root.addEndField()
    # print str(root)
    # root.deleteComponent('comp2')
    # print str(root)
    test = ProtocolDecisionTree()
    test.addStartField("Hyper Text Transfer Protocol", "Transfer text accross the web", "", "")
    print str(test)
    test.addField()
    print str(test)
    test.addReferenceList()
    print str(test)
    test.addPacketInfoList()
    print str(test)
    test.addEndField()
    print str(test)
    test.deleteComponent('comp3')
    print str(test)
    test.deleteComponent('comp2')
    test.deleteComponent('comp4')
    test.deleteComponent('comp1')
    print str(test)
    test.deleteComponent('comp5')
    print str(test)

