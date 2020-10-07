class Category:
    i=0

    def __init__(self,cat):
        self.name=cat
        self.ledger=[]
        self.total=0
        self.impr=""
        self.wit=0
        self.dep=0
    
    def deposit(self,amount,description=""):
        self.ledger.append({"amount":amount, "description":description})
        self.total+=amount
        self.dep+=amount

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":description})
            self.total-=amount
            self.wit+=amount
            return True
        else:
            return False

    def get_balance(self):
        return(self.total)

    def transfer(self,amount,cat):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":"Transfer to " + cat.name})
            self.total-=amount
            self.wit+=amount
            cat.ledger.append({"amount":amount, "description":"Transfer from " + self.name})
            cat.total+=amount
            self.dep+=amount
            return True
        else:
            return False

    def check_funds(self,amount):
        if amount <= self.total:
            return True
        else:
            return False

    def __str__(self):
        i=15-int(len(self.name)/2)
        while i>0:
            self.impr+="*"
            i-=1
        self.impr+=self.name
        i=15-int(len(self.name)/2)
        while i>0:
            self.impr+="*"
            i-=1
        if (len(self.name)%2)>0:
            self.impr+="*"
        for item in self.ledger:
            self.impr+="\n"
            self.impr+=item["description"][0:23]
            amount_str="{:0.2f}".format(item["amount"])
            i = 23 - len(item["description"])
            while i>0:
                self.impr+=" "
                i-=1
            i = 7 - len(amount_str)
            while i>0:
                self.impr+=" "
                i-=1
            self.impr+=amount_str
        self.impr=self.impr+"\nTotal: "+str(self.total)
        return self.impr


def create_spend_chart(categories):
    lengths = []
    maxlen = None
    total = 0
    i = 0
    porcentajes = []
    imprime="Percentage spent by category"
    for category in categories:
        lengths.append(len(category.name))
        porcentajes.append(category.wit)
        total+=category.wit 
    for porcentaje in porcentajes:
        porcentajes[i] = int((porcentaje*10)/total)*10
        i+=1
    maxlen = max(lengths)
    i=100
    while i>=0: 
        if i==100: 
            imprime=imprime+"\n"+str(i)+"|"
        elif i>0: 
            imprime=imprime+"\n "+str(i)+"|"        
        else: 
            imprime=imprime+"\n  "+str(i)+"|"
        for porcentaje in porcentajes:
            if porcentaje >= i:
                imprime+=" o "
            else:
                imprime+="   "
        imprime+=" "
        i-=10
    imprime+="\n    "
    for porcentaje in porcentajes:
        imprime+="---"
    imprime+="-"
    i=0
    while i<maxlen:
        imprime+="\n    "
        for category in categories:
            try:
                imprime=imprime+" "+category.name[i]+" "
            except:
                imprime+="   "
        imprime+=" "
        i+=1
    return imprime