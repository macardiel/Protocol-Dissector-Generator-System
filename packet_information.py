from component import Component

class PacketInformation(Component):

    PACKETINFOLIST = {}

    def __init__(self):
        Component.__init__(self, 'reference_list', None)
        self.PACKETINFOLIST = {}

    def addElement(self, key, value):
        if key in self.PACKETINFOLIST:
            pass
        else:
            self.PACKETINFOLIST[key] = value

    def delElement(self, key):
        del(self.PACKETINFOLIST[key])

    def detailedStr(self):
        currField = '(' + self.FieldID + ':' + self.FieldType + ':' + str(self.PACKETINFOLIST)

        if self.NextField:
            nextID = self.NextField.FieldID
            currField += ':' + nextID + ')'
        else:
            currField += ':None]'
        return currField

if __name__ == '__main__':
    pass