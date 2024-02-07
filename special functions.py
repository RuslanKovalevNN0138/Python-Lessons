import math

def negative(n:int):
    """
    used for filters of positive and negative numbers
    """
    return n<0

def positive(n:int):
    """
    used for filters of positive and negative numbers
    """
    return n>=0

if __name__=="__main__":

    nums=[3,2,3,4,2,-1,-2,-3,4,5,11,-10]
    
    # filters of pos and neg numbers
    # for num array
    pos_nums=list(filter(positive,nums))
    neg_nums=list(filter(negative,nums))
    print("positive nums:\n",pos_nums)
    print("negative nums:\n",neg_nums)

    nums_1=[2,-3,4,-7,8,9]
    squares_1=[i*i for i in nums_1]
    print("squares_1:\n",squares_1)
    
    squares_2=map(lambda num: num**2,nums_1)
    squares_2=list(squares_2)
    print("squares_2:\n",squares_2)

    for ind,(num_1,square_1) in enumerate(zip(nums_1,squares_1)):
        print("square of {} is {}".format(nums_1[ind],squares_1[ind]))

    
