def main():
    speed=int(input("Enter your speed")) #user is supposed to enter speed
    limit=int(input("Enter the limit")) #user is supposed to enter limit
    
    if 90>speed>=limit: #if the speed is greater than the limit but less than 90
        over_lim=speed-limit #This is to calculate each mph over the limit
        Fine=50+(5*over_lim)#This to calculate the fine
        print("Your total fine is",Fine)
    
    elif speed>=90:#if speed is greater than 90
        over_lim=speed-limit
        Fine2=50+(5*over_lim)+200
        print("Your total fine is",Fine2)

    else:
        print("Your speed was legal") #if the speed is less than the limit then it is legal speed
main()
