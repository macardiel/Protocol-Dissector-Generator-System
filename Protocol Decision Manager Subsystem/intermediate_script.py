import xml.etree.ElementTree as ET

from protocol_decision_tree import ProtocolDecisionTree

class IntermediateScript:

    def __init__(self):
        self.PDT_list = []

    def getPDTList(self):
        return self.PDT_list

    def insertToPDTList(self, PDTNode):
        currentNode = PDTNode
        self.PDT_list.insert(len(self.PDT_list), currentNode.encapsulate())

    def PDTtoList(self, tree):
        self.PDT_list = []
        currentNode = tree.PDT
        self.insertToPDTList(currentNode)
        while currentNode.getNext():
            currentNode = currentNode.getNext()
            self.insertToPDTList(currentNode)

    def PDTtoXML(self, tree):
        self.PDTtoList(tree)
        root = ET.Element('Protocol Decision Tree')
        for i in self.PDT_list:
            currComp = ET.SubElement(root, 'Component ID')
            currType = ET.SubElement(currComp, 'Type')
            currNext = ET.SubElement(currComp, 'Next')

            currComp.text = self.PDT_list[self.PDT_list.index(i)][0]
            currType.text = self.PDT_list[self.PDT_list.index(i)][1]
            currNext.text = str(self.PDT_list[self.PDT_list.index(i)][2])

        #ET.dump(root)
        return root

if __name__ == '__main__':
    pass
    # tree = ProtocolDecisionTree()
    # print str(tree)
    #
    # IS = IntermediateScript()
    # IS.PDTtoList(tree)
    #
    # print str(IS.PDT_list)
    #
    # tree.addStartField()
    # tree.addField()
    # tree.addEndField()
    #
    # print str(tree)
    #
    # IS.PDTtoList(tree)
    #
    # print str(IS.PDT_list)
    #
    # ET.dump(IS.PDTtoXML(tree))