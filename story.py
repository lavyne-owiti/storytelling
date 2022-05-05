import random
when = ["There was this day","Do you remeber that time","A few years back","yesterday","Today morning","I remember when"]
who =['a friend of mine','when that guy','I met a young girl','I saw a cat','a bird','my grandmother']
name =['Fluke','Janice','Happy','Kiding','Sparor','Pacifica']
residence =['Maldives','Seychelles','Hawai','Bahamas','Paris','Ireland']
went =['club','market','hotel','Beach','Homes','Ranch']
happend =['drunk a lot fluids ','shopped for friuts','bought the house','bred the horses','ate a five course meal','enjoyed the sun']
print(random.choice(when)+','+random.choice(who)+' who lived in '+ random.choice(residence)+ ' and liked going to the '+random.choice(went)+','+ random.choice(happend)+'.')