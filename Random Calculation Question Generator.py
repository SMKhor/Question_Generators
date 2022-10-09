import random

def question_1 (x,y):
    print("x =", x)
    print("y =", y)
    answer = input("If an audio track is x seconds long recorded in stereo, samples at y Khz with a sample depth of 32 bits, what is the file size of this audio recording in MB (2.d.p): ")
    correct = x*y*1000*32*2/8/1024/1024
    if float(answer) == round(correct,2):
        print("That is correct!")
    else:
        print("That is incorrect, the correct answer is:", round(correct,2))

def question_2 (x,y):
    print("x =", x)
    print("y =", y)
    answer = input("If an audio track is x seconds long recorded in stereo, samples at y Khz with a sample depth of 16 bits, what is the file size of this audio recording in MB (2.d.p): ")
    correct = x*y*1000*16*2/8/1024/1024
    if float(answer) == round(correct,2):
        print("That is correct!")
    else:
        print("That is incorrect, the correct answer is:", round(correct,2))

def question_3 (x,y,z):
    print("x =", x)
    print("y =", y)
    print("z =", z)
    answer = input("A 32 bit colour image is x inches by y inches in size with the resolution of z dots per inch. Calculate the storage requirements for this image in MB (2.d.p): ")
    correct = x*y*z*4/1024/1024
    if float(answer) == round(correct,2):
        print("That is correct!")
    else:
        print("That is incorrect, the correct answer is:", round(correct,2))

def question_4 (x,y,z):
    print("x =", x)
    print("y =", y)
    print("z =", z)
    answer = input("A 24 bit colour image is x inches by y inches in size with the resolution of z dots per inch. Calculate the storage requirements for this image in MB (2.d.p): ")
    correct = x*y*z*3/1024/1024
    if float(answer) == round(correct,2):
        print("That is correct!")
    else:
        print("That is incorrect, the correct answer is:", round(correct,2))

def question_5 (x,y,z):
    print("x =", x)
    print("y =", y)
    print("z =", z)
    answer = input("A 8 bit colour image is x inches by y inches in size with the resolution of z dots per inch. Calculate the storage requirements for this image in MB (2.d.p): ")
    correct = x*y*z*1/1024/1024
    if float(answer) == round(correct,2):
        print("That is correct!")
    else:
        print("That is incorrect, the correct answer is:", round(correct,2))

def question_6 (x):
    print("x =", x)
    answer = input("If I write x characters in a text file in ASCII string, how much KB is needed? (2.d.p): ")
    correct = x*1/1024
    if float(answer) == round(correct,2):
        print("That is correct!")
    else:
        print("That is incorrect, the correct answer is:", round(correct,2))

def question_7 (x):
    print("x =", x)
    answer = input("If I write x characters in a text file in unicode characters, how much KB is needed? (2.d.p): ")
    correct = x*2/1024
    if float(answer) == round(correct,2):
        print("That is correct!")
    else:
        print("That is incorrect, the correct answer is:", round(correct,2))

def question_8 (x,y):
    print("x =", x)
    print("y =", y)
    answer = input("Calculate the amount of megapixels a pixel resolution of x by y is to 2.d.p: ")
    correct = x*y/1000000
    if float(answer) == round(correct,2):
        print("That is correct!")
    else:
        print("That is incorrect, the correct answer is:", round(correct,2))

while True:
    print("Generated question:")
    choice = random.randint(1,8)
    if choice == 1:
        x = random.randint(30,600)
        y = random.randint(20,100)
        question_1(x, y)

    if choice == 2:
        x = random.randint(30,600)
        y = random.randint(20,100)
        question_2(x, y)

    if choice == 3:
        x = random.randint(100,1000)
        y = random.randint(100,1000)
        z = random.randint(200,2000)
        question_3(x, y, z)

    if choice == 4:
        x = random.randint(100,1000)
        y = random.randint(100,1000)
        z = random.randint(200,2000)
        question_4(x, y, z)

    if choice == 5:
        x = random.randint(100,1000)
        y = random.randint(100,1000)
        z = random.randint(200,2000)
        question_5(x, y, z)

    if choice == 6:
        x = random.randint(1000,10000)
        question_6(x)

    if choice == 7:
        x = random.randint(1000,10000)
        question_7(x)

    if choice == 8:
        x = random.randint(1000,10000)
        y = random.randint(1000,10000)
        question_8(x,y)
