# -*- coding: cp1252 -*-
#Dieses Modul beinhaltet alle Sprechphasen des Explainscreens.
#Format:
#Array[0]: Gesicht von Joey. 0 Normal, 1 Mund auf,  2 Mund auf/Augenbraue
#Array[1]: Bild, welches gezeigt werden soll. none -> Kein Bild
#Array[2]: Text, der draufgeschrieben werden soll.
def get_option(identifier):
   if identifier==0:
      return [0, "none", "Hey. Ich bin Joy.%new%Nett, dass du auch hier bist.%new%Nutze die Pfeiltasten um weiter zu kommen."];
   elif identifier==1:
      return [1, "none", "Ich habe mal wieder etwas angestellt.%new%Nun muss ich von unserem Hausmeister entkommen.%new%Willst du mir dabei helfen?"];
   elif identifier==2:
      return [1, "models/game/explains/jump.png", "Hlilf mir, über Gegenstände zu springen,%new%indem du die Leertaste drückst."];
   elif identifier==3:
      return [2, "models/game/explains/item.png", "Manchmal schweben Items in der Luft.%new%Sammel sie ein, denn du wirst%new%sie brauchen."];
   elif identifier==4:
      return [0, "models/game/explains/uhr.png", "Du kannst zwischen deinen Items%new%mit den Pfeiltasten navigieren. Das ist die Uhr.%new%Sie verlangsamert die Spielgeschwindigkeit."];
   elif identifier==5:
      return [1, "models/game/explains/riegel.png", "Das ist ein Riegel. Wenn du mal%new%irgendwo stecken bleibst, setze ihn ein.%new%Er wird mich nach vorne boosten."];
   elif identifier==6:
      return [0, "models/game/explains/apfel.png", "Das ist der Apfel. Ich bin ein Mensch und%new%nun ja. Hungrig werde ich auch mal.%new%Fülle damit meine Jumps auf."];
   elif identifier==7:
      return [2, "models/game/explains/jumps.png", "Wenn wir schon davon sprechen.%new%Hier siehst du die Anzahl an Sprüngen,%new%die du übrig hast. Wähle weise."];
   elif identifier==8:
      return [1, "models/game/explains/zeit.png", "Das ist deine Spielzeit. Je länger du rennst,%new%desto größer wird sie."];
   elif identifier==9:
      return [2, "models/game/explains/difficulty.png", "Noch eine Sache. Wenn du dich wie ein Profi fühlst,%new%nutze die Taste D, um die Schwierigkeit%new%zu verändern."];
   elif identifier==10:
      return [1, "none", "Wenn du das Tutorial neustarten willst,%new%drücke einfach die Taste T."];
   elif identifier==11:
      return [0, "none", "Nun bist du bereit.%new%Ich wünsche dir viel Spaß."];
   elif identifier >11:
      return True;
   else:
      return False;
