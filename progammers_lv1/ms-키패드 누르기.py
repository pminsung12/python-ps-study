#keypad=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
def numToIndex(n):
    num=str(n)
    if num=='1':
        return (0,0)
    elif num=='2':
        return (0,1)
    elif num=='3':
        return (0,2)
    elif num=='4':
        return (1,0)
    elif num=='5':
        return (1,1)
    elif num=='6':
        return (1,2)
    elif num=='7':
        return (2,0)
    elif num=='8':
        return (2,1)
    elif num=='9':
        return (2,2)
    elif num=='*':
        return (3,0)
    elif num=='0':
        return (3,1)
    elif num=='#':
        return (3,2)

def solution(numbers, hand):
    answer = ''
    lx,ly=3,0
    rx,ry=3,2
    for num in numbers:
        if num==1 or num==4 or num==7:
            #print("147")
            answer+='L'
            lx,ly=numToIndex(num)
            continue
        if num==3 or num==6 or num==9:
            #print("369")
            rx,ry=numToIndex(num)
            answer+='R'
            continue
            
        nx,ny=numToIndex(num)
        if abs(nx-lx)+abs(ny-ly) < abs(nx-rx)+abs(ny-ry):
            #print("<")
            answer+='L'
            lx,ly=nx,ny
        elif abs(nx-lx)+abs(ny-ly) > abs(nx-rx)+abs(ny-ry):
            #print(">")
            answer+='R'
            rx,ry=nx,ny
        else:
            if hand=='left':
                #print("left")
                answer+='L'
                lx,ly=nx,ny
            else:
                #print("right")
                answer+='R'
                rx,ry=nx,ny
        
    return answer