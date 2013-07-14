formatter = "%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True,False,True,False)

# again depends on the later "#"
print formatter %(formatter,formatter,formatter,formatter)