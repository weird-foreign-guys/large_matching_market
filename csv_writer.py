import datetime
class Csv_writer:

    def __init__(self,k,rounds,lower,upper):
        self.file = f"DATA/k={k}:rounds={rounds}:lower={lower}:upper={upper}:Date={datetime.datetime.now()}"
    
    def write(self,n,ratio):
        ratio = "0,"+str(ratio)[2:]
        with open(self.file,'a') as f:
            f.write(f"{n};{ratio}\n")
            

if __name__ == "__main__":
    writer = Csv_writer(10,3,2,100)
    writer.write(10,0.001)
    writer.write(12,0.213123)