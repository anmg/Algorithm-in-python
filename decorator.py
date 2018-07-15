
#send para
def logging(level):
    #func
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print "[{level}]: enter funtion {func}()".format(level = level, func = func.__name__)
            
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print "say {}!".format(something)

@logging(level='DEBUG')
def do(something):
    print "do {}...".format(something)

if __name__ == '__main__':
    say('hello')
    do("my work")
