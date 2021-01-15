from rx import range

test = range(0, 11)
test.subscribe(
    lambda x: print("The value is {0}".format(x)),
    on_error=lambda e: print("Error : {0}".format(e)),
    on_completed=lambda: print("Job Done!")
)
