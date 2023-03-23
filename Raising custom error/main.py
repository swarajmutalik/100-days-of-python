a = int(input("Enter any value between 5 and 9"))

# using the raise keyword we can raise an error

if(a<5 or a>9):
    raise ValueError("Value should be betweeen 5 and 9")
