from typing import Dict

class DAG:
    def _init_(self, x: str, lb: str = '_', lt: 'DAG' = None, rt: 'DAG' = None):
        self.label = lb
        self.data = x
        self.left = lt
        self.right = rt

if _name_ == '_main_':
    n = 6
    st = [
        "A=b[0]",
        "B=A+c",
        "C=a/d",
        "D=B*C",
        "E=c+d",  
        "F=D-E"
    ]
    labelDAGNode: Dict[str, DAG] = {}
    
    for i in range(5):
        stTemp = st[i]
        for j in range(5):
            tempLabel = stTemp[0]
            tempLeft = stTemp[2]
            tempData = stTemp[3]
            tempRight = stTemp[4]
            leftPtr = None
            rightPtr = None
            
            if tempLeft not in labelDAGNode:
                leftPtr = DAG(tempLeft)
            else:
                leftPtr = labelDAGNode[tempLeft]
                
            if tempRight not in labelDAGNode:
                rightPtr = DAG(tempRight)
            else:
                rightPtr = labelDAGNode[tempRight]
            
            nn = DAG(tempData, tempLabel, leftPtr, rightPtr)
            labelDAGNode[tempLabel] = nn

    print("Label      ptr      leftPtr       rightPtr")
for i in range(n):
    if st[i][0] in labelDAGNode:
        x = labelDAGNode[st[i][0]]
        if x.data == '[':
            print(f"{st[i][0]}            []            ", end="")
        else:
            print(f"{st[i][0]}            {x.data}            ", end="")
        if x.left.label == '_':
            print(x.left.data, end="")
        else:
            print(x.left.label, end="")
        print("          ", end="")
        if x.right.label == '_':
            print(x.right.data)
        else:
            print(x.right.label)
    else:
        print(f"{st[i][0]}            {st[i][1]}            _             _")

