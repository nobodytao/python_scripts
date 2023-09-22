
#Add verification of the entered IP address. An address is considered correct if it:
# consists of 4 numbers (not letters or other symbols)
#numbers separated by a dot
#each number between 0 and 255
#If the address is set incorrectly, display the message: "Invalid IP address".
#---------------------------------------------------------------- -----------------------
#Indicate the ownership of the address:
#"unicast" - if the first byte is in the range 1-223
#"multicast" - if the first byte is in the range 224-239
#"local broadcast" - if the IP address is 255.255.255.255
#"unassigned" - if the IP address is 0.0.0.0
#"unused" - in all other cases

# Solution: iterate through characters until there is not a number,
# and any other character

isOk=False
isOctetsOk=False
ip = input('Enter an IP address in the format 10.10.0.1: ')

while (isOk==False) or (isOctetsOk == False):

     prev_lett=''
     prev_dots_count=1
     isOk=True
     isOctetsOk=True

     for lett in ip:
         if lett.isdigit():
             prev_dots_count = 1
             #print(lett)
         elif lett != '.':
             print ('Error: IP address contains characters other than numbers and dot')
             isOk=False
         elif ((lett == '.') and (prev_lett == '.')):
             prev_dots_count += 1
             print ('Error: {} dots in a row'.format(prev_dots_count))
             isOk=False
         prev_lett=lett

     if(ip.startswith(".")):
         print('Error: IP address starts with a dot, first octet not entered')
         isOk=False

     if(ip.endswith(".")):
         print('Error: IP address ends with dot, last octet not entered')
         isOk=False
       
     if isOk:
         IPlist=ip.split('.')

         if (len(IPlist) != 4):
             isOctetsOk=False
             print ("Error: Not enough dot-separated octets = {}". format(len(IPlist)))
 
         for octet in IPlist:
             if not(int(octet) in range(0,256)):
                 isOctetsOk=False
                 print('Octet {} is not between 0 and 255'.format(octet))
         if isOctetsOk:
             if int(IPlist[0]) in range(1,223):
                 print(ip,' "unicast"')
             elif int(IPlist[0]) in range(224,239):
                 print(ip,'"multicast"')
             elif ip=='255.255.255.255':
                 print(ip,'"local broadcast"')
             elif ip=='0.0.0.0':
                 print(ip,'"unassigned"')
             else:
                 print(ip,'"unused"')
     if isOk == False or isOctetsOk == False:
         print('Wrong IP address!')
         ip=input('Enter IP address again: ')