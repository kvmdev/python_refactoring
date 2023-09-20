def forThird():
    print( 'Will end' )

def forSecond():
    print( 'Results so far' )
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()

def forFirst():
    while True:
                print( 'Please enter your rating from 1 to 5' )
                point = input()
                if point.isdecimal():
                    point = int(point)
                    if  point <= 0 or point > 5: # 0以下または5より大きいという条件式
                        print( 'Please enter from 1 to 5' )
                        point = input()
                    else:
                        print( 'Please enter your comment' )
                        comment = input()
                        post = f'Point: {point} comment: {comment}'
                        file_pc = open("data.txt", 'a')
                        file_pc.write( f'{ post } \n' )
                        file_pc.close()
                        break
                else:
                    print( 'Please enter the evaluation points in numbers.' )

def ask():
    while True:
        print( 'Please select the process you want to perform' )
        print( '1: Enter rating points and comments' )
        print( '2: Check the results so far' )
        print( '3: Finish' )

        num = input('Enter a number from 1 to 3: ')

        if num.isdecimal():
            num = int(num)

            if num == 1:
                forFirst()
            if num == 2:
                forSecond()
            if num == 3:
                forThird()
                break
            else:
                print( 'Please enter from 1 to 3' )