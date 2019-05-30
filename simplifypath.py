# this problem was asked by microsoft and facebook
# Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....
#
# Here is some info on Unix file system paths:
#
# / is the root directory; the path should always start with it even if it isn't there in the given path;
# / is also used as a directory separator; for example,
# /code/fights denotes a fights subfolder in the code folder in the root directory;
# this also means that // stands for "change the current directory to the current directory"
# . is used to mark the current directory;
# .. is used to mark the parent directory; if the current directory is root already, .. does nothing.

# when I first encountered this problem, I realized that we want to focus on what's between the dashes
# and not the dashes themselves, so I focused on what was inside of the parentheses. I then thought of
# how we could keep track of where we were in the file system in an easy way. Since we will really
# just be focusing on the elements that were just put into the datastructure, you could think of using a
# stack, which will work, it will just require some difference with how you choose to reassemble the information
# because python does everything with lists and you can treat them like a deque, I decided to use a list
# because it will allow me to push and pop, as well as allow me to iterate in the direction that will
# be easy to concatinate all of the strings together.

# the last step to this problem is realizing that we can push and pop on and off of this datastructure
# with very simple rules. First, we must split the string at '/' and iterate over all of the strings
# Next, we must make the conditions for the strings we encounter. If we encounter a '..', we must pop
# off the current director IF THERE IS ONE IN THE DS. If the current directory is 'root' (we will assume
# this is when the list is empty) then you do not pop. Next, if we encounter '.' or '', we want to do nothing
# well, this is really trivial to take care of so I will leave that alone. Lastly, we want to append
# the directory if it's anything. So to do this, we will use if/elif statements. The one trick that I use
# is in the second elif statement, I check to see if the directory is not '.' or '', meaning it must
# be anything else within the set of possibilities. Awesome! We did it

def simplifyPath(path):
    npath = []
    for d in path.split('/'):
        if d == '..':
            if npath: npath.pop()
        elif not(d == '' or d == '.'):
            npath.append(d)
    return '/' + '/'.join(npath)


# test
p = '/home/a/./x/../b//c/'
print(simplifyPath(p))