
numbers = [input('Enter a number: ') for i in range(4)]
even = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 == 1]

print 'All even', even

if even:
    print 'Min even:', min(even)	
    
else:
    print 'No even numbers input'
    

print 'All odd`s', odds 
if odds:
    print  'Max odd`s:', max(odds)	
   
else:
    print 'No odd numbers input'

input('Press Enter to continue...')  
