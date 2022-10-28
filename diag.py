from socket import J1939_EE_INFO_NONE
from diagrams import Diagram , Cluster,Edge
from diagrams.generic import os
from diagrams.programming import language
from diagrams.custom import Custom


with Diagram("whos doing what", show=False, direction="TB"):

    with Cluster("people"):
        WC1 = Custom("tom","pcb.png")
        WC2 = Custom("dick","gaffa.png")
        WC3 = Custom("harry","Atari-Logo.png") 
        W1  = os.Android("worker3")
        W2  = os.Android("worker4")
        W3  = os.Android("worker5")
        W4  = os.Android("worker6")
        W5  = os.Android("worker7") 

    with Cluster("Al Jobs"):
        cpp = language.Cpp("")
        python = language.Python("")
        js = language.JavaScript("")

    
    J1 = os.Centos("one")
    J2 = os.Centos("two")        
    J3 = os.Centos("two")
    J4 = os.Centos("two")
    J5 = os.Centos("two") 

    WC1 - Edge(color="red") -  cpp
    WC2 >> cpp
    WC3 >> python
    WC1 >> js
    W1 - J1
    W1 - J2
    W1 - J3
    W1 - J4
    W1 - J5
    W2 - J1
    W2 - J2
    W2 - J3
    W2 - J4
    W2 - J5


