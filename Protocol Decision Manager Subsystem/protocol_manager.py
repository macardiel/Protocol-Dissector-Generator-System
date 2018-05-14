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

    def generateIntermediateScript(self):
        pass

if __name__ == '__main__':
    test = protocol_manager()
    print str(test.PDT)
    test.setPDTDescription("test pdt")
    print test.getPDTDescription()