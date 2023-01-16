from exe import run_exe

class Graphics():
 
    def __init__(self):
        self.parameters = []
        self.parameters.append({"Excel sheet name":" ","Bands name":" ", "Subject name":" ", "Graphics name":" "})
        self.initial = 0
    
    def input(self):
        return self.parameters[self.initial]
    
    def graph(self,txt_subValue,txt_sheetValue,txt_bands,txt_group,txt_graphicsValue):
        print(txt_subValue)
        print(txt_sheetValue)
        print(txt_bands)
        print(txt_group)
        print(txt_graphicsValue)
        run_exe(txt_subValue,txt_sheetValue,txt_bands,txt_group,txt_graphicsValue)
        
