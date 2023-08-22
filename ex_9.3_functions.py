#You have file config_sw1.txt:

'''
Current configuration : 2033 bytes
!
! Last configuration change at 13:11:59 UTC Thu Feb 25 2016
!
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname sw1
!
!
!
!
! 
!
!
!
!
!
!
interface FastEthernet0/0
 switchport mode access
 switchport access vlan 10
!
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100,200
 switchport mode trunk
 duplex auto
!
interface FastEthernet0/2
 switchport mode access
 switchport access vlan 20
 duplex auto
!         
interface FastEthernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100,300,400,500,600
 duplex auto
 switchport mode trunk
!         
interface FastEthernet1/0
 switchport mode access
 switchport access vlan 20
!
interface FastEthernet1/1
 switchport mode access
 switchport access vlan 30
 duplex auto
!
interface FastEthernet1/2
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 400,500,600
 switchport mode trunk
 duplex auto
!
interface FastEthernet1/3
 duplex auto
!
interface Vlan100
 ip address 10.0.100.1 255.255.255.0
!
!
alias configure sh do sh 
alias exec ospf sh run | s ^router ospf
alias exec bri show ip int bri | exc unass
alias exec id show int desc
alias exec top sh proc cpu sorted | excl 0.00%__0.00%__0.00%
alias exec c conf t
alias exec diff sh archive config differences nvram:startup-config system:running-config
alias exec shcr sh run | s ^crypto
alias exec desc sh int desc | ex down
alias exec bgp sh run | s ^router bgp
alias exec xc sh xconnect all
alias exec vc sh mpls l2tr vc
!
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input all
!
end
'''

#You have to get from this file 2 dictionaries:

#First dictionary 'Access' have to be like this:
#{"FastEthernet0/12": 10,
# "FastEthernet0/14": 11,
# "FastEthernet0/16": 17}

#Second dictionary 'Trunk' have to be like this:
#{"FastEthernet0/1": [10, 20],
# "FastEthernet0/2": [11, 30],
# "FastEthernet0/4": [17]}

#If you find smth like this:
#interface FastEthernet0/20
# switchport mode access
# duplex auto
#Then "FastEthernet0/20": 1

dict_acc={}
dict_trunk={}

def get_int_vlan_map(file_name):
    with open('config_sw1.txt','r') as config_file:
        fileline=''
        while not(fileline.startswith('end')):
            dictkey = None
            isAccess = None
            isTrunk = None
            isDuplex = None
            fileline = config_file.readline()
            if fileline.startswith('interface FastEthernet'):
                isAccess = False
                isTrunk = False
                isDuplex = False
                dictkey=fileline.strip().strip('interface ')
                vlanlist=[]
                while not(fileline.startswith('!')):
                    fileline = config_file.readline()
                    if fileline.find('vlan') > 0:
                        vlanlist=fileline.strip().split(' vlan ').pop(-1).split(',')
                        for vlanlistindex in range(len(vlanlist)):
                            vlanlist[vlanlistindex]=int(vlanlist[vlanlistindex])
                    if fileline.find('switchport mode trunk') > 0:
                        isTrunk = True
                        break
                    if fileline.find('switchport mode access') > 0:
                        isAccess = True
                    if fileline.find('duplex auto') > 0:
                        isDuplex = True
            if isAccess and isDuplex:
                dict_acc[dictkey] = 1
            elif isAccess:
                dict_acc[dictkey] = int(vlanlist[0])
            elif isTrunk:
                dict_trunk[dictkey] = vlanlist

    return dict_acc, dict_trunk

        
print(get_int_vlan_map('config_sw1.txt'))