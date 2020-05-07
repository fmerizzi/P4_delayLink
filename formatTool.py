f = open("dataArrival.csv","r")
w = open("dataArrival_final.csv","w") 
x = f.readline()
test = x.split(",")
counter = 0
for line in test:
	counter = counter + 1
	w.write(line + ",")
	if(counter == 2):
		w.write("\n")
		counter = 0

f.close();
w.close();
