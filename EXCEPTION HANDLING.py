#exception run time error

#try / except (CORE CONCEPT)

# try:
    # risky code
# except:
    # runs if error occurs


try:
    10/0
except:
    print("error")



try:
    10/0
except ZeroDivisionError:
    print("only enter positive no :")


try:
    a=int(input())
except ZeroDivisionError:
    print("error")
except ValueError:
    print("value error")
    
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("No error, result =", x)



try:
    x = 10 / 0
except:
    print("Error")
finally:
    print("Done")


try:
    x = 10 / 0
except Exception:
    print("General error")
except ZeroDivisionError:
    print("Zero division")




try:
    x = int("abc") / 0
except (ValueError, ZeroDivisionError):
    print("Handled")


try:
    a = [1, 2, 3]
    print(a[5])
except IndexError:
    print("Index problem")



try:
    print(int("abc"))
except Exception:
    print("General")
except ValueError:
    print("Value")



try:
    print(int("abc"))
except ValueError:
    print("Value")
except Exception:
    print("General")

try:
    x = int("10")
    print(x / 2)
except ValueError:
    print("Invalid")





#raise Keyword (Manually throw error)

    x=int(input())
    if x<0:
        raise ValueError("negative Error")


try:
    x = -10
    if x < 0:
        raise ValueError("Negative")
except ValueError as e:
    print("Error:", e)


#tricky

try:
    print("A")
except:
    print("B")
else:
    print("C")
finally:
    print("D")





    
try:
    raise TypeError("Wrong")
except ValueError:
    print("Value")
finally:
    print("Finish")














