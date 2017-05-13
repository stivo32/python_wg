input = raw_input()
exception = None
if input == '0':
    exception = IndexError()
elif input == '1':
    exception = AttributeError()
elif input == '2':
    message = raw_input('Input message for your Exception\n')
    exception = Exception(message)
try:
    raise exception
except IndexError:
    raise
except AttributeError:
    print 'Hello Python!'
except Exception as e:
    print type(e).__name__, e

