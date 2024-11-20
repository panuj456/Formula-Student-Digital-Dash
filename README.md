Hi Nick and any of you lads who have stumbled across this, 

Basically I've tried to do research on why the issue we have
which is the CAN not being able to update data whilst the app window is open. 
We know the app window can update values when closed and re opened multiple times. 
Therefore, the issue is with the line app.exec() which blocks the processes (acting like sleep), 
then once the app is closed it runs again (try placing the app.exec() outside of the while loop and run it, 
you should see after app is closed the CAN runs normally). 

The best methodology to follow going forward is how people got animation to work and to just ignore player input perhaps.
Anyway, back on topic, after reading many forums I believe I will have to learn how to perform threading in pyqt5, 
it is a little out of my scope. Basically what threading does is creates sort of a channel for things to 
update in the background whilst the app window runs. Really weird and I cant really get my head around it right now, 
and I probably will need a lot of help. If you can find a better solution lmk cause my brain is ded rn and i need sleep.

I've left some solutions in the main.py file commented out just use the ''' to encapsulate any code you dont wanna use. 
In essence, use the sudo python receive.py line in the CMD for working and live data reading of CAN. 
Use sudo python main.py for the code relating to the GUI and all this window app talk in the same CMD.

TLDR: pyqt is great for the most part, app.exec() is being a pain, so no matter how code ordered and looped, 
it will always be a cockblock unless we do threading which I must skillmaxx.

Panu
