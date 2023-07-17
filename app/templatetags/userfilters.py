from django import template
register=template.Library()

@register.filter()
def swap(data):
    return data.swapcase()

@register.filter()
def remove(data,arg):
    return data.replace(arg,'')

@register.filter()
def count(data,args):
    c=0
    for i in range(len(data)):
        if data[i:i+len(args):]==args:
            c+=1
    return c

@register.filter()
def lower(data):
    str=''
    for i in range(len(data)):
        if i==0:
            str+=data[i]
        elif i==len(data)-1:
            str+=data[i]
        else:
            str+=data[i].lower()
    return str
        
    #if len(data)<3:
        #return data
    #s=data[0:1]
    #s1=data[1:-1].lower()
    #s2=data[-1:]
    #return s+s1+s2
    

#register.filter('count',count)
#register.filter('swap',swap)
#register.filter('remove',remove)
