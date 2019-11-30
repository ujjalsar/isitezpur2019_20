

def myfunction():
    status = True
    fp1 = None
    try:
        mydata = [100,200,300]
        print(mydata[1])
        fp1 = open("some_file.txt")    
        return status
        a = 100
        b = 0
        print(a/b)
    except ZeroDivisionError as er1:
        print("error first block", er1)
        print("closing file")
        fp1.close()
    except (FileNotFoundError, IndexError) as er:
        print("error second block",er)
        status = False
    except Exception as e3:
        print("general error block",e3)
        status = False
    else:
        print("all is well")
        status = False
    finally:
        print("closing file pointer")
        if fp1:
            fp1.close()
    
    return status

#call_status = myfunction()
#print(call_status)




def add(a,b):
    return a+b


def module_name():
    print("file name is file_ops.py module namespace is \" ",__name__, "\"")


module_name()
    
    