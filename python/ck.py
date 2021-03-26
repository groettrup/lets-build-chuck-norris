from ctypes import *

# Load the dll using a relative path
handle = cdll.LoadLibrary(r"build/default/bin/chucknorris.dll")
# set the response type of the init function
handle.chuck_norris_init.restype = c_void_p
# set the response type of the get_fact function
handle.chuck_norris_get_fact.restype = c_char_p
# set the arguments of the get_fact function
handle.chuck_norris_get_fact.argtypes = [c_void_p]
ck = handle.chuck_norris_init()
fact_as_bytes = handle.chuck_norris_get_fact(ck)
fact_text = fact_as_bytes.decode("UTF-8")
print(fact_text)