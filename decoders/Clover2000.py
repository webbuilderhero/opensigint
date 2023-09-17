""" 
#TODO: Add additional logic to decode Clover2000

#decoder for Clover2000 protocol
def decodeClover2000(sigint):
    #Signal Intelligence / RF Signal Information
    signalInfo = sigint.getBasebandFrequencyInfo()
    
    #Check for Clover2000 protocol
    if signalInfo.get("protocol") == "Clover2000":
        #TODO: Parse data from RF signal 
        
        # Check for Clover2000 message
        if signalInfo.get("msgType") == "Clover2000":
            #TODO: Parse header information
            headerInfo = sigint.getHeaderInfo()
            messageId = headerInfo.get("messageId")
            senderId = headerInfo.get("senderId")
            #TODO: Parse data fields 
            dataFields = sigint.getDataFields()
            data1 = dataFields.get("data1")
            data2 = dataFields.get("data2")
            data3 = dataFields.get("data3")
            #Return decoded message
            return {"messageId": messageId, "senderId": senderId, "data1": data1, "data2": data2, "data3": data3} 
    #No Clover2000 protocol found
    else:
        return None