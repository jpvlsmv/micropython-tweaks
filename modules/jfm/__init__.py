def main():
    """Entry point for the application script"""
    print("Call your main application code here")

# Utility functions
def cat(x):
    import uio
    print(uio.open(x).read())

def noexport():
    print("This is not exported from the module")

# __name__ = "jfm" #(vs micropython-jfm)

if __name__ != "__main__":
    __all__ = [ "cat" ]
