import winsound as ws
import time as tm

M = {'A':'._','B':'_...','C':'_._.','D':'_..','E':'.','F':'.._.','G':'__.','H':'....','I':'..','J':'.___','K':'_._','L':'._..','M':'__','N':'_.','O':'___','P':'.__.','Q':'__._','R':'._.','S':'...','T':'_','U':'.._','V':'..._','W':'.__','X':'_.._','Y':'_.__','Z':'__..','0':'_____','1':'.____','2':'..___','3':'...__','4':'...._','5':'.....','6':'_....','7':'__...','8':'___..','9':'____.','.':'._._._',',':'__..__',':':'___...','?':'..__..','=':'_..._','-':'_...._','(':'_.__.',')':'_.__._','\"':'._.._.','\'':'.____.','/':'_.._.','@':'.__._.','!':'_._.__',' ':' / '}

flag = True

while flag:
    s2 = ''
    s = input("write a message to converte to morse: ")
    s = s.upper()
    for i in s:
        s2 += M[i]
        s2 += ' '
    print("morse code: ",s2)
    for j in s2:
        if j == '.':
            ws.Beep(1000,200)
            tm.sleep(0.01)
        elif j == '_':
            ws.Beep(1000,600)
            tm.sleep(0.01)
        elif j == ' ':
            tm.sleep(0.5)
        elif j == '/':
            tm.sleep(2)
    f = input("continue? (Y/N) ")
    if f == 'N' or f == 'n':
        flag = False
