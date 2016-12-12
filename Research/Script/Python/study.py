
import sys

#print "hello python"
print sys.argv[0]
#print sys.argv[1]

object = sys.argv[1]
type = sys.argv[2]

output = ('- (' + type + ' *)' + object + ' ' + '{\n' +
          '   if (!_' + object + ') {\n\n' +
          '   }\n' +
          '   return _' + object + ';\n}')

#output_stype2 =

print output

#string = ("aaa\n" +
#          type +
#          "bbb")
#
#print string
