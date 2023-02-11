class univariate():
    
    def init(self):
        pass
    
    def QuanQual(self,dataset):
        quan=[]
        qual=[]

        for columnName in dataset.columns:
            if (dataset[columnName].dtype=="object"):
                print(columnName,"Qual")
                qual.append(columnName)
            else:
                    print(columnName,"Quan")
                    quan.append(columnName)  
        return quan,qual            