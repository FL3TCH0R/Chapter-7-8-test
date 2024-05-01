def main():
    sum=0 
    count=0
    while True:
        n=int(input("Enter a number"))
        if n==999: #this is the setinel value of the loop, if this is entered the loop stops
            break
        sum=sum+n #for each iteration you are adding every number you input together
        count=count+1 #this is to count how many numbers were entered
    print("Average is",sum/count) #This line will evaluate the final average if the sentinel value was entered
main()
