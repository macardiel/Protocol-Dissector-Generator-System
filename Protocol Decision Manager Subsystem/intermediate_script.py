import xml.etree.ElementTree as ET
from protocol_manager import ProtocolManager
from protocol_decision_tree import ProtocolDecisionTree

class IntermediateScript:

    def __init__(self):
        self.PDT_list = []

    def insertToPDTList(self, PDTNode):
        currentNode = PDTNode
        self.PDT_list.insert(len(self.PDT_list), currentNode.encapsulate())

    def PDTtoXML(self, tree):
        self.PDT_list = []
        currentNode = tree.PDT
        self.insertToPDTList(currentNode)
        while currentNode.getNext():
            currentNode = currentNode.getNext()
            self.insertToPDTList(currentNode)

if __name__ == '__main__':
    tree = ProtocolDecisionTree()
    print str(tree)

    IS = IntermediateScript()
    IS.PDTtoXML(tree)

    print str(IS.PDT_list)

    tree.addStartField()
    tree.addField()
    tree.addEndField()

    print str(tree)

    IS.PDTtoXML(tree)

    print str(IS.PDT_list)